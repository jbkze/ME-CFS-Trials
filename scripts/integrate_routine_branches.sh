#!/usr/bin/env bash
# Integrate the ME/CFS research-watch routine's output from claude/* branches into
# `main`, so the dashboard AND the literature archive update with no manual merge.
#
# WHY THIS EXISTS / THE BUG IT FIXES
#   The routine commits its results on a claude/* branch when it can't push to main
#   directly. Every paper-finding run writes BOTH data files and `literature/`
#   files (PDFs, summaries, BibTeX). The earlier version of this logic allow-listed
#   only the five data/generated files, so any run that added a paper tripped the
#   "non-data file -> skip" guard on its literature/ files and was silently left
#   un-merged. The allow-list below therefore treats the WHOLE literature/ tree
#   (and the routine-maintained sources list) as routine output.
#
# SAFETY
#   It copies ONLY the routine's output files from a branch onto main and NEVER
#   runs the branch's code, so it is safe even with a write token. A branch that
#   also changes development files (scripts, .github/, docs/index.html, CLAUDE.md,
#   data/schema.json, templates/ …) is recognised as a human dev branch and left
#   untouched (loud ::warning::, no delete) — never silently dropped.
#
# USAGE
#   integrate_routine_branches.sh <branch>   # one branch (push trigger)
#   integrate_routine_branches.sh --all      # sweep every claude/* branch (cron)
#
# ENV
#   REPO=owner/name        (required, for gh)
#   DEV_BRANCH=claude/...  (never touched; default below)
#   DRY_RUN=1              (print actions, don't push/delete — for local testing)
set -uo pipefail

DEV_BRANCH="${DEV_BRANCH:-claude/nice-einstein-yqeyjo}"
REPO="${REPO:-}"
DRY_RUN="${DRY_RUN:-}"

# The COMPLETE set of paths the routine is expected to write. Exact files plus the
# entire literature/ tree. Anything outside this marks the branch as development.
# Keep this in sync with ROUTINE.md "Updating the files" if the routine's output
# ever grows — that is the one maintenance point that prevents a repeat of the bug.
is_routine_output() {
  case "$1" in
    data/trials.json|data/papers.json|TRIALS.md|docs/dashboard.json|checks/CHANGELOG.md|sources/search-sources.md) return 0 ;;
    literature/*) return 0 ;;
    *) return 1 ;;
  esac
}
COPY_PATHS="data/trials.json data/papers.json TRIALS.md docs/dashboard.json checks/CHANGELOG.md sources/search-sources.md literature"

have_gh() { command -v gh >/dev/null 2>&1; }

reset_main() {
  git fetch -q origin main
  git checkout -q -B main origin/main
}

close_or_delete() {   # $1 = branch ; integrated already, so retire it
  local br="$1" closed=false n
  if [ -n "$DRY_RUN" ]; then echo "  [dry-run] would close PR / delete $br"; return 0; fi
  if have_gh; then
    for n in $(gh pr list --repo "$REPO" --head "$br" --state open --json number -q '.[].number' 2>/dev/null); do
      gh pr close "$n" --repo "$REPO" --delete-branch \
        --comment "Routine data already integrated into \`main\` by the integration workflow — closing as superseded." && closed=true || true
    done
  fi
  [ "$closed" = true ] || git push -q origin --delete "$br" 2>/dev/null || echo "  (could not delete $br — prune will)"
}

integrate_one() {   # $1 = branch
  local br="$1" sha changed dev="" f
  if [ "$br" = "$DEV_BRANCH" ]; then echo "keep (dev branch): $br"; return 0; fi
  git fetch -q origin "$br" 2>/dev/null || { echo "$br: cannot fetch; skip"; return 0; }
  sha="$(git rev-parse "origin/$br")"
  changed="$(git diff --name-only "origin/main...$sha" || true)"
  if [ -z "$changed" ]; then echo "$br: nothing new vs main -> retire"; close_or_delete "$br"; return 0; fi
  while IFS= read -r f; do
    [ -z "$f" ] && continue
    is_routine_output "$f" || dev="$dev $f"
  done <<< "$changed"
  if [ -n "$dev" ]; then
    echo "::warning title=Routine branch not auto-integrated::$br changed development files, left for manual review:$dev"
    return 0
  fi

  echo "$br: pure routine output -> integrating into main"
  reset_main
  for p in $COPY_PATHS; do
    git checkout "$sha" -- "$p" 2>/dev/null || true     # copies adds+mods, incl. new literature/ files
  done
  if git diff --cached --quiet; then
    echo "  main already current -> retire branch"
  else
    git config user.name  "github-actions[bot]"
    git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
    git commit -q -m "Integrate routine data from ${br}" \
      -m "Auto-applied so the dashboard + literature archive update without a manual merge. Source: ${br} @ ${sha}. Only data/generated/literature files are copied; the branch's code is never executed."
    if [ -n "$DRY_RUN" ]; then
      echo "  [dry-run] would push $(git rev-parse --short HEAD) to main with:"
      git show --stat --oneline HEAD | sed 's/^/    /' | head -20
      git reset -q --hard origin/main
      return 0
    fi
    git push -q origin HEAD:main || { echo "  push to main failed"; return 0; }
    echo "  integrated into main"
  fi
  close_or_delete "$br"
}

reset_main
case "${1:-}" in
  --all)
    for b in $(git ls-remote --heads origin 'claude/*' | sed 's#.*refs/heads/##'); do
      integrate_one "$b"
      reset_main      # a prior integrate may have advanced main
    done
    ;;
  "")
    echo "usage: $0 <branch>|--all" >&2; exit 2 ;;
  *)
    integrate_one "$1" ;;
esac
