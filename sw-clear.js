// Service Worker Cache Clearer
// Add this to force clear all caches and reload

if ('serviceWorker' in navigator) {
    navigator.serviceWorker.getRegistrations().then(function(registrations) {
        for(let registration of registrations) {
            registration.unregister();
            console.log('✅ Service Worker unregistered');
        }
    });
}

if ('caches' in window) {
    caches.keys().then(function(cacheNames) {
        return Promise.all(
            cacheNames.map(function(cacheName) {
                console.log('🗑️ Deleting cache:', cacheName);
                return caches.delete(cacheName);
            })
        );
    }).then(function() {
        console.log('✅ All caches cleared!');
        console.log('🔄 Reloading page...');
        window.location.reload(true);
    });
} else {
    console.log('⚠️ Cache API not supported');
    window.location.reload(true);
}

