/**
 * ================================================================
 * TE KETE AKO - SERVICE WORKER
 * Progressive Web App - Offline Capability
 * ================================================================
 * Super Genius Sprint - Dimension 3: Technical Mastery
 * Agent-9 - October 16, 2025
 * ================================================================
 */

const CACHE_VERSION = 'te-kete-ako-v1.0.6-oct24-singleton-fixes';
const CACHE_STATIC = `${CACHE_VERSION}-static`;
const CACHE_DYNAMIC = `${CACHE_VERSION}-dynamic`;

// Critical assets to cache immediately
const STATIC_ASSETS = [
    '/',
    '/index.html',
    '/offline.html',
    
    // Core CSS (canonical system)
    '/css/component-library.css',
    '/css/beautiful-navigation.css',
    '/css/animations-professional.css',
    '/css/mobile-optimization.css',
    '/css/print.css',
    
    // Core JS
    '/js/te-kete-professional.js',
    
    // Core Components
    '/components/navigation-standard.html',
    '/components/footer.html',
    
    // Critical Pages
    '/login.html',
    '/resource-hub.html',
    '/lessons.html',
];

/**
 * Install Service Worker
 */
self.addEventListener('install', (event) => {
    
    event.waitUntil(
        caches.open(CACHE_STATIC)
            .then((cache) => {
                // Cache files individually to handle missing files gracefully
                return Promise.allSettled(
                    STATIC_ASSETS.map(asset => 
                        cache.add(asset).catch(err => {
                            console.warn(`[Service Worker] Failed to cache ${asset}:`, err);
                            return null; // Continue with other assets
                        })
                    )
                );
            })
            .then(() => self.skipWaiting())
            .catch((error) => {
                console.error('[Service Worker] Install failed:', error);
            })
    );
});

/**
 * Activate Service Worker
 */
self.addEventListener('activate', (event) => {
    
    event.waitUntil(
        caches.keys()
            .then((cacheNames) => {
                return Promise.all(
                    cacheNames.map((cacheName) => {
                        if (cacheName !== CACHE_STATIC && cacheName !== CACHE_DYNAMIC) {
                            return caches.delete(cacheName);
                        }
                    })
                );
            })
            .then(() => self.clients.claim())
    );
});

/**
 * Fetch Strategy: Network First, Cache Fallback
 */
self.addEventListener('fetch', (event) => {
    const { request } = event;
    const url = new URL(request.url);
    
    // Skip external requests
    if (!url.origin.includes(self.location.origin)) {
        return;
    }
    
    // Skip Supabase API calls
    if (url.hostname.includes('supabase')) {
        return;
    }
    
    event.respondWith(
        // Try network first
        fetch(request)
            .then((networkResponse) => {
                // Cache successful responses
                if (networkResponse && networkResponse.status === 200) {
                    const responseClone = networkResponse.clone();
                    
                    caches.open(CACHE_DYNAMIC)
                        .then((cache) => {
                            cache.put(request, responseClone);
                        });
                }
                
                return networkResponse;
            })
            .catch(() => {
                // Network failed, try cache
                return caches.match(request)
                    .then((cachedResponse) => {
                        if (cachedResponse) {
                            return cachedResponse;
                        }
                        
                        // If no cache, return offline page for HTML requests
                        if (request.headers.get('accept').includes('text/html')) {
                            return caches.match('/offline.html');
                        }
                        
                        // For other resources, return error
                        return new Response('Offline', {
                            status: 503,
                            statusText: 'Service Unavailable'
                        });
                    });
            })
    );
});

/**
 * Background Sync (for offline actions)
 */
self.addEventListener('sync', (event) => {
    
    if (event.tag === 'sync-progress') {
        event.waitUntil(syncProgressData());
    }
});

/**
 * Sync student progress when back online
 */
async function syncProgressData() {
    // Would sync any offline progress to Supabase
    // Implementation would go here
}

/**
 * Push Notifications (for teacher announcements)
 */
self.addEventListener('push', (event) => {
    const data = event.data ? event.data.json() : {};
    
    const options = {
        body: data.body || 'New announcement from Te Kete Ako',
        icon: '/icons/icon-192x192.png',
        badge: '/icons/badge-72x72.png',
        vibrate: [200, 100, 200],
        data: data.url || '/',
        actions: [
            { action: 'view', title: 'View' },
            { action: 'dismiss', title: 'Dismiss' }
        ]
    };
    
    event.waitUntil(
        self.registration.showNotification('Te Kete Ako', options)
    );
});

/**
 * Notification click handling
 */
self.addEventListener('notificationclick', (event) => {
    event.notification.close();
    
    if (event.action === 'view' || !event.action) {
        event.waitUntil(
            clients.openWindow(event.notification.data || '/')
        );
    }
});


