// Service worker: makes the dashboard installable and usable offline.
// It only caches this site's own files (no personal data, nothing about the
// viewer). Pages and data are network-first, so every online visit shows the
// latest run; the cached copy is used only when the network is unavailable.
var CACHE = 'mecfs-watch-v1';
var CORE = [
  './', 'index.html', 'dashboard.json', 'manifest.webmanifest', 'icon.svg', 'icon-192.png',
  'fonts/poppins.css', 'fonts/poppins-latin-400-normal.woff2', 'fonts/poppins-latin-500-normal.woff2',
  'fonts/poppins-latin-600-normal.woff2', 'fonts/poppins-latin-700-normal.woff2', 'fonts/poppins-latin-800-normal.woff2'
];

self.addEventListener('install', function (e) {
  e.waitUntil(caches.open(CACHE).then(function (c) { return c.addAll(CORE); }).then(function () { return self.skipWaiting(); }));
});

self.addEventListener('activate', function (e) {
  e.waitUntil(caches.keys().then(function (keys) {
    return Promise.all(keys.filter(function (k) { return k !== CACHE; }).map(function (k) { return caches.delete(k); }));
  }).then(function () { return self.clients.claim(); }));
});

self.addEventListener('fetch', function (e) {
  var req = e.request;
  if (req.method !== 'GET' || new URL(req.url).origin !== self.location.origin) return;
  var isStatic = /\/fonts\/|\.woff2$|icon[-.]/.test(req.url);
  if (isStatic) {
    // Fonts and icons never change in place: cache first.
    e.respondWith(caches.match(req).then(function (hit) {
      return hit || fetch(req).then(function (res) {
        var copy = res.clone();
        caches.open(CACHE).then(function (c) { c.put(req, copy); });
        return res;
      });
    }));
    return;
  }
  // Page, data and everything else: network first, cache as offline fallback.
  e.respondWith(fetch(req).then(function (res) {
    if (res.ok) {
      var copy = res.clone();
      caches.open(CACHE).then(function (c) { c.put(req, copy); });
    }
    return res;
  }).catch(function () {
    return caches.match(req, { ignoreSearch: true }).then(function (hit) {
      return hit || caches.match('index.html');
    });
  }));
});
