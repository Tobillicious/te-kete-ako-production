// EMERGENCY SERVICE WORKER KILLER - Forces cache clear
self.addEventListener('install', function(event) {
  self.skipWaiting();
});

self.addEventListener('activate', function(event) {
  event.waitUntil(
    caches.keys().then(function(cacheNames) {
      console.log('🚨 EMERGENCY: Clearing ALL caches');
      return Promise.all(
        cacheNames.map(function(cacheName) {
          console.log('Deleting cache:', cacheName);
          return caches.delete(cacheName);
        })
      );
    }).then(function() {
      console.log('✅ All caches cleared - reloading page');
      return self.clients.claim();
    }).then(function() {
      // Force reload all clients
      self.clients.matchAll().then(clients => {
        clients.forEach(client => client.navigate(client.url));
      });
    })
  );
});

// Block all fetch requests to prevent interference
self.addEventListener('fetch', function(event) {
  // Let all requests pass through
});