// 🟣 VIOLET Service Worker - PWA + Offline Mode
const CACHE_NAME = 'violet-pwa-v2';
const VIDEO_CACHE = 'violet-videos-v2';
const IMAGE_CACHE = 'violet-images-v2';

// 📋 قائمة الملفات للتخزين الدائم
const STATIC_ASSETS = [
    '/',
    '/index.html',
    '/auth.html',
    '/profile.html',
    '/upload.html',
    '/chat.html',
    '/explore.html',
    '/notifications.html',
    '/settings.html',
    '/firebase-config.js',
    '/manifest.json',
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css',
    'https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js',
    'https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js',
    'https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js'
];

// 🟣 Install - تخزين الملفات الأساسية
self.addEventListener('install', (event) => {
    console.log('🟣 VIOLET SW: Installing...');
    event.waitUntil(
        caches.open(CACHE_NAME).then((cache) => {
            console.log('🟣 Caching static assets');
            return cache.addAll(STATIC_ASSETS);
        }).then(() => {
            console.log('🟣 SW Installed!');
            return self.skipWaiting();
        })
    );
});

// 🟣 Activate - تنظيف الكاش القديم
self.addEventListener('activate', (event) => {
    console.log('🟣 VIOLET SW: Activating...');
    event.waitUntil(
        caches.keys().then((cacheNames) => {
            return Promise.all(
                cacheNames.map((cacheName) => {
                    if (cacheName !== CACHE_NAME && cacheName !== VIDEO_CACHE && cacheName !== IMAGE_CACHE) {
                        console.log('🟣 Deleting old cache:', cacheName);
                        return caches.delete(cacheName);
                    }
                })
            );
        }).then(() => {
            console.log('🟣 SW Activated!');
            return self.clients.claim();
        })
    );
});

// 🟣 Fetch - استراتيجية التخزين المؤقت
self.addEventListener('fetch', (event) => {
    const url = event.request.url;

    // 🎬 تخزين الفيديوهات مؤقتاً
    if (url.includes('cloudinary.com/video') || url.endsWith('.mp4')) {
        event.respondWith(
            caches.open(VIDEO_CACHE).then((cache) => {
                return cache.match(event.request).then((cachedResponse) => {
                    // إرجاع المخزن مؤقتاً إذا كان متوفراً
                    if (cachedResponse && !navigator.onLine) {
                        console.log('🟣 Serving cached video:', url);
                        return cachedResponse;
                    }
                    // تحميل من الشبكة وتخزينه
                    return fetch(event.request).then((networkResponse) => {
                        if (networkResponse && networkResponse.ok) {
                            cache.put(event.request, networkResponse.clone());
                        }
                        return networkResponse;
                    }).catch(() => {
                        // إذا فشل التحميل، إرجاع المخزن
                        return cachedResponse || new Response('Video unavailable offline', { status: 503 });
                    });
                });
            })
        );
        return;
    }

    // 🖼️ تخزين الصور مؤقتاً
    if (url.includes('cloudinary.com/image') || url.match(/\.(jpg|jpeg|png|gif|svg|webp)$/i)) {
        event.respondWith(
            caches.open(IMAGE_CACHE).then((cache) => {
                return cache.match(event.request).then((cachedResponse) => {
                    if (cachedResponse) return cachedResponse;
                    return fetch(event.request).then((networkResponse) => {
                        if (networkResponse && networkResponse.ok) {
                            cache.put(event.request, networkResponse.clone());
                        }
                        return networkResponse;
                    }).catch(() => cachedResponse);
                });
            })
        );
        return;
    }

    // 📄 الملفات الثابتة - Cache First
    if (STATIC_ASSETS.includes(url) || url.includes('firebase-config.js')) {
        event.respondWith(
            caches.match(event.request).then((cachedResponse) => {
                if (cachedResponse) return cachedResponse;
                return fetch(event.request).then((networkResponse) => {
                    if (networkResponse && networkResponse.ok) {
                        const clonedResponse = networkResponse.clone();
                        caches.open(CACHE_NAME).then((cache) => {
                            cache.put(event.request, clonedResponse);
                        });
                    }
                    return networkResponse;
                }).catch(() => cachedResponse);
            })
        );
        return;
    }

    // 🔄 الطلبات الأخرى - Network First مع fallback للكاش
    event.respondWith(
        fetch(event.request).then((networkResponse) => {
            return networkResponse;
        }).catch(() => {
            return caches.match(event.request).then((cachedResponse) => {
                return cachedResponse || new Response('Offline', { status: 503 });
            });
        })
    );
});

// 🔔 Push Notifications
self.addEventListener('push', (event) => {
    const data = event.data ? event.data.json() : {};
    const options = {
        body: data.body || 'تحديث جديد من VIOLET 🟣',
        icon: '/icon-192.png',
        badge: '/icon-192.png',
        vibrate: [200, 100, 200],
        tag: 'violet-notification',
        renotify: true
    };
    event.waitUntil(
        self.registration.showNotification(data.title || 'VIOLET 🟣', options)
    );
});

console.log('🟣 VIOLET Service Worker Ready!');
