#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════╗
║                                                            ║
║  🟣  VIOLET 2026 - PURPLE GLASS EDITION  🟣              ║
║     Ultimate Version - 10 Files - PWA + Offline            ║
║                                                            ║
║  🔥  Firebase: gokp-a0633                                 ║
║  ☁️   Cloudinary: dk5kas1gc / gy45_g                      ║
║  👑  Admin: jasim28v@gmail.com                            ║
║  👾  Avatars: DiceBear Big Smile (Random)                  ║
║  💎  Design: Purple Glass Transparent + PWA                ║
║                                                            ║
║  ✨  PREMIUM FEATURES:                                     ║
║     • 🔔 Notification System                              ║
║     • 🎬 Compact Video Grid                               ║
║     • 🗑️  Delete Videos from Admin Panel                  ║
║     • 💾 Offline Mode (Service Worker)                    ║
║     • 🔄 Auto Sync عند توفر الإنترنت                     ║
║     • 📱 PWA (تثبيت على الشاشة الرئيسية)                  ║
║     • 💎 Glass Morphism Transparent Layers                 ║
║     • 🟣 Purple Story Rings                               ║
║     • ✨ Purple Glow Effects                               ║
║     • 🌟 Smooth In-App Viewer                              ║
║     • 📱 Floating Bottom Nav                               ║
║     • توثيق + حظر + حذف فيديوهات                          ║
║                                                            ║
╚══════════════════════════════════════════════════════════════╝
"""

import os
import sys

# ═══════════════════════════════════════════════════════════
# 🟣 CONFIGURATION - الإعدادات
# ═══════════════════════════════════════════════════════════

FIREBASE_CONFIG = {
    "apiKey": "AIzaSyC7Bfcp9JgBQMwasEeuLlZVzM58R0l1CXE",
    "authDomain": "gokp-a0633.firebaseapp.com",
    "databaseURL": "https://gokp-a0633-default-rtdb.firebaseio.com",
    "projectId": "gokp-a0633",
    "storageBucket": "gokp-a0633.firebasestorage.app",
    "messagingSenderId": "794248779449",
    "appId": "1:794248779449:web:c78564c0d126c01cafed68",
    "measurementId": "G-PW6B2R0F6H"
}

# 🟣 Cloudinary
CLOUD_NAME = "dk5kas1gc"
UPLOAD_PRESET = "gy45_g"
ADMIN_EMAILS_JS = "['jasim28v@gmail.com']"
DICEBEAR_URL = "https://api.dicebear.com/7.x/big-smile/svg"

# 🟣 Purple Glass Palette
ROSE_COLORS_JS = """[
    "linear-gradient(135deg, #4c1d95, #6d28d9, #7c3aed)",
    "linear-gradient(135deg, #3b0764, #4c1d95, #6d28d9)",
    "linear-gradient(135deg, #2e1065, #3b0764, #4c1d95)",
    "linear-gradient(135deg, #8b5cf6, #7c3aed, #6d28d9)",
    "linear-gradient(135deg, #a855f7, #8b5cf6, #7c3aed)",
    "linear-gradient(135deg, #0a0812, #1a1030, #8b5cf6)"
]"""

# ═══════════════════════════════════════════════════════════
# 🟣 UTILITY
# ═══════════════════════════════════════════════════════════

TOTAL_LINES = 0

def write(filename, content):
    global TOTAL_LINES
    os.makedirs(os.path.dirname(filename) if os.path.dirname(filename) else '.', exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    lines = content.count('\n') + 1
    TOTAL_LINES += lines
    print(f"  ✅ {filename} ({lines} سطر)")

def section(title):
    print(f"\n{'='*60}")
    print(f"  🟣 {title}")
    print(f"{'='*60}")

# ═══════════════════════════════════════════════════════════
# 🟣 1. firebase-config.js
# ═══════════════════════════════════════════════════════════

def build_config():
    return f"""// 🟣 VIOLET 2026 - Purple Glass Configuration
// Firebase: gokp-a0633 | Cloudinary: dk5kas1gc
// ✨ PREMIUM: PWA + Offline + Auto Sync

const firebaseConfig = {{
    apiKey: "{FIREBASE_CONFIG['apiKey']}",
    authDomain: "{FIREBASE_CONFIG['authDomain']}",
    databaseURL: "{FIREBASE_CONFIG['databaseURL']}",
    projectId: "{FIREBASE_CONFIG['projectId']}",
    storageBucket: "{FIREBASE_CONFIG['storageBucket']}",
    messagingSenderId: "{FIREBASE_CONFIG['messagingSenderId']}",
    appId: "{FIREBASE_CONFIG['appId']}",
    measurementId: "{FIREBASE_CONFIG['measurementId']}"
}};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();
const db = firebase.database();

// Cloudinary Configuration
const CLOUD_NAME = "{CLOUD_NAME}";
const UPLOAD_PRESET = "{UPLOAD_PRESET}";

// 🟣 VIOLET Settings
const ADMIN_EMAILS = {ADMIN_EMAILS_JS};
const DICEBEAR_URL = "{DICEBEAR_URL}";
const COVER_COLORS = {ROSE_COLORS_JS};

// 🟣 App Info
const APP_NAME = "VIOLET";
const APP_VERSION = "2026.1";
const PRIMARY_COLOR = "#7c3aed";
const SECONDARY_COLOR = "#a855f7";

// 💾 Offline Storage - IndexedDB
const offlineDB = indexedDB.open('VIOLET_Offline', 1);
offlineDB.onupgradeneeded = function(event) {{
    const db = event.target.result;
    if (!db.objectStoreNames.contains('videos')) {{
        db.createObjectStore('videos', {{ keyPath: 'id' }});
    }}
    if (!db.objectStoreNames.contains('users')) {{
        db.createObjectStore('users', {{ keyPath: 'uid' }});
    }}
    if (!db.objectStoreNames.contains('pendingLikes')) {{
        db.createObjectStore('pendingLikes', {{ keyPath: 'videoId', autoIncrement: false }});
    }}
}};

// 🌐 Network Detection
let isOnline = navigator.onLine;
window.addEventListener('online', () => {{ isOnline = true; syncPendingActions(); }});
window.addEventListener('offline', () => {{ isOnline = false; }});

// 🔄 Sync pending actions when online
async function syncPendingActions() {{
    if (!auth.currentUser) return;
    const db_ = await new Promise((resolve, reject) => {{
        const request = indexedDB.open('VIOLET_Offline', 1);
        request.onsuccess = (event) => resolve(event.target.result);
        request.onerror = (event) => reject(event.target.error);
    }});
    
    const tx = db_.transaction(['pendingLikes'], 'readwrite');
    const store = tx.objectStore('pendingLikes');
    const allPending = await new Promise((resolve) => {{
        const request = store.getAll();
        request.onsuccess = () => resolve(request.result);
    }});
    
    for (const pending of allPending) {{
        try {{
            const ref = db.ref('videos/' + pending.videoId);
            const snap = await ref.get();
            const video = snap.val();
            if (video) {{
                let likes = video.likes || 0;
                let likedBy = video.likedBy || {{}};
                if (!likedBy[auth.currentUser.uid]) {{
                    likes++;
                    likedBy[auth.currentUser.uid] = true;
                    await ref.update({{ likes, likedBy }});
                }}
            }}
            store.delete(pending.videoId);
        }} catch(e) {{ console.error('Sync failed:', e); }}
    }}
}}

console.log('🟣 %c'+APP_NAME+' v'+APP_VERSION+' Ready ✨ | PWA + Offline', 'color: #7c3aed; font-size: 16px; font-weight: bold;');
"""

# ═══════════════════════════════════════════════════════════
# 🟣 2. sw.js - Service Worker (PWA + Offline)
# ═══════════════════════════════════════════════════════════

def build_sw():
    return """// 🟣 VIOLET Service Worker - PWA + Offline Mode
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
"""

# ═══════════════════════════════════════════════════════════
# 🟣 3. manifest.json - PWA Manifest
# ═══════════════════════════════════════════════════════════

def build_manifest():
    return """{
    "name": "VIOLET",
    "short_name": "VIOLET",
    "description": "VIOLET - Purple Glass Edition",
    "start_url": "/index.html",
    "display": "standalone",
    "background_color": "#0a0812",
    "theme_color": "#7c3aed",
    "orientation": "portrait",
    "icons": [
        {
            "src": "/icon-192.png",
            "sizes": "192x192",
            "type": "image/png"
        },
        {
            "src": "/icon-512.png",
            "sizes": "512x512",
            "type": "image/png"
        }
    ],
    "categories": ["social", "entertainment", "video"],
    "lang": "ar",
    "dir": "rtl"
}"""

# ═══════════════════════════════════════════════════════════
# 🟣 4. auth.html
# ═══════════════════════════════════════════════════════════

def build_auth():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>🟣 VIOLET | دخول</title>
    <link rel="manifest" href="/manifest.json">
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        *{margin:0;padding:0;box-sizing:border-box}
        body{
            min-height:100vh;
            background:radial-gradient(ellipse at top, #1a1030, #0a0812, #000000);
            display:flex;align-items:center;justify-content:center;
            font-family:'Segoe UI',sans-serif;overflow:hidden;
        }
        .bg-orb{
            position:fixed;border-radius:50%;filter:blur(130px);opacity:0.2;
            animation:orbFloat 20s infinite alternate;
        }
        .bg-orb:nth-child(1){width:400px;height:400px;background:#7c3aed;top:-100px;left:-100px}
        .bg-orb:nth-child(2){width:350px;height:350px;background:#a855f7;bottom:-100px;right:-100px;animation-delay:5s}
        .bg-orb:nth-child(3){width:300px;height:300px;background:#c084fc;top:50%;left:50%;animation-delay:10s}
        @keyframes orbFloat{0%{transform:translate(0,0) scale(1)}100%{transform:translate(50px,-50px) scale(1.3)}}

        .card{
            position:relative;z-index:1;width:90%;max-width:420px;
            background:rgba(124,58,237,0.03);
            backdrop-filter:blur(40px);-webkit-backdrop-filter:blur(40px);
            border-radius:32px;padding:36px 24px;
            border:1px solid rgba(124,58,237,0.2);
            box-shadow:0 30px 70px rgba(124,58,237,0.1),inset 0 0 30px rgba(124,58,237,0.03);
            animation:fadeUp 0.8s ease;
        }
        @keyframes fadeUp{from{opacity:0;transform:translateY(40px)}to{opacity:1;transform:translateY(0)}}

        .logo{
            width:70px;height:70px;margin:0 auto 20px;
            background:linear-gradient(135deg, rgba(124,58,237,0.3), rgba(168,85,247,0.3));
            border-radius:20px;display:flex;align-items:center;justify-content:center;
            font-size:36px;border:1px solid rgba(124,58,237,0.2);
            box-shadow:0 15px 40px rgba(124,58,237,0.25);
            animation:logoGlow 3s ease-in-out infinite;
        }
        @keyframes logoGlow{0%,100%{box-shadow:0 15px 40px rgba(124,58,237,0.25)}50%{box-shadow:0 15px 60px rgba(192,132,252,0.6)}}
        h1{text-align:center;font-size:36px;font-weight:900;background:linear-gradient(to bottom, #fff, #c084fc);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:4px}
        .sub{text-align:center;color:rgba(255,255,255,0.4);font-size:13px;margin-bottom:20px}

        .tabs{display:flex;gap:4px;background:rgba(124,58,237,0.05);border-radius:40px;padding:4px;margin-bottom:24px}
        .tab{flex:1;padding:12px;background:none;border:none;color:rgba(255,255,255,0.5);cursor:pointer;border-radius:40px;font-size:14px;transition:all 0.3s;font-weight:500}
        .tab.active{background:linear-gradient(135deg, #7c3aed, #a855f7);color:#fff;box-shadow:0 8px 20px rgba(124,58,237,0.3)}

        .form{display:none;animation:fadeIn 0.4s ease}
        .form.active{display:block}
        @keyframes fadeIn{from{opacity:0}to{opacity:1}}

        input{
            width:100%;padding:15px 18px;margin:8px 0;
            border-radius:50px;background:rgba(124,58,237,0.03);
            border:1px solid rgba(124,58,237,0.15);color:#fff;
            font-size:14px;outline:none;transition:all 0.4s;
        }
        input:focus{border-color:rgba(124,58,237,0.5);box-shadow:0 0 20px rgba(124,58,237,0.1);background:rgba(124,58,237,0.06)}
        input::placeholder{color:rgba(255,255,255,0.3)}

        button{
            width:100%;padding:15px;margin-top:18px;
            background:linear-gradient(135deg, #7c3aed, #a855f7);
            border:none;border-radius:50px;color:#fff;
            font-weight:bold;font-size:15px;cursor:pointer;
            transition:all 0.3s;box-shadow:0 10px 30px rgba(124,58,237,0.3);
        }
        button:hover{transform:translateY(-2px);box-shadow:0 20px 40px rgba(124,58,237,0.5)}
        button:active{transform:scale(0.97)}
        button:disabled{opacity:0.5;pointer-events:none}

        .msg{text-align:center;color:#fca5a5;font-size:13px;margin-top:12px;min-height:20px}
        .msg.success{color:#4ade80}
    </style>
</head>
<body>
    <div class="bg-orb"></div><div class="bg-orb"></div><div class="bg-orb"></div>
    <div class="card">
        <div class="logo">🟣</div>
        <h1>VIOLET</h1>
        <p class="sub">Purple Glass 2026 ✨</p>
        <div class="tabs">
            <button class="tab active" id="tabLogin" onclick="switchTab('login')"><i class="fas fa-sign-in-alt"></i> دخول</button>
            <button class="tab" id="tabRegister" onclick="switchTab('register')"><i class="fas fa-user-plus"></i> اشتراك</button>
        </div>
        <div id="formLogin" class="form active">
            <input type="email" id="loginEmail" placeholder="📧 البريد الإلكتروني" autocomplete="email">
            <input type="password" id="loginPass" placeholder="🔒 كلمة المرور" autocomplete="current-password">
            <button id="btnLogin" onclick="doLogin()"><i class="fas fa-arrow-right-to-bracket"></i> تسجيل الدخول</button>
            <div class="msg" id="loginMsg"></div>
        </div>
        <div id="formRegister" class="form">
            <input type="text" id="regName" placeholder="👤 اسم المستخدم" autocomplete="username">
            <input type="email" id="regEmail" placeholder="📧 البريد الإلكتروني" autocomplete="email">
            <input type="password" id="regPass" placeholder="🔒 كلمة المرور (6 أحرف على الأقل)" autocomplete="new-password">
            <button id="btnRegister" onclick="doRegister()"><i class="fas fa-heart"></i> إنشاء حساب</button>
            <div class="msg" id="regMsg"></div>
        </div>
    </div>
    <script src="firebase-config.js"></script>
    <script>
        if ('serviceWorker' in navigator) {
            navigator.serviceWorker.register('/sw.js').then(() => console.log('🟣 SW Registered'));
        }
        function switchTab(type){
            document.getElementById('tabLogin').classList.remove('active');
            document.getElementById('tabRegister').classList.remove('active');
            document.getElementById('formLogin').classList.remove('active');
            document.getElementById('formRegister').classList.remove('active');
            document.getElementById('loginMsg').innerText = '';
            document.getElementById('regMsg').innerText = '';
            if(type === 'login'){
                document.getElementById('tabLogin').classList.add('active');
                document.getElementById('formLogin').classList.add('active');
            } else {
                document.getElementById('tabRegister').classList.add('active');
                document.getElementById('formRegister').classList.add('active');
            }
        }
        async function doLogin(){
            const email = document.getElementById('loginEmail').value.trim();
            const password = document.getElementById('loginPass').value;
            const msg = document.getElementById('loginMsg');
            const btn = document.getElementById('btnLogin');
            if(!email || !password){ msg.innerText = '❌ الرجاء ملء جميع الحقول'; return; }
            btn.disabled = true; btn.innerHTML = '⏳ جاري الدخول...'; msg.innerText = ''; msg.className = 'msg';
            try {
                await auth.signInWithEmailAndPassword(email, password);
                window.location.replace('index.html');
            } catch(error) {
                btn.disabled = false; btn.innerHTML = '<i class="fas fa-arrow-right-to-bracket"></i> تسجيل الدخول';
                switch(error.code) {
                    case 'auth/user-not-found': msg.innerText = '❌ لا يوجد حساب بهذا البريد'; break;
                    case 'auth/wrong-password': case 'auth/invalid-credential': msg.innerText = '❌ كلمة المرور غير صحيحة'; break;
                    case 'auth/invalid-email': msg.innerText = '❌ بريد إلكتروني غير صالح'; break;
                    case 'auth/too-many-requests': msg.innerText = '❌ محاولات كثيرة، حاول لاحقاً'; break;
                    default: msg.innerText = '❌ خطأ: ' + error.message;
                }
            }
        }
        async function doRegister(){
            const username = document.getElementById('regName').value.trim();
            const email = document.getElementById('regEmail').value.trim();
            const password = document.getElementById('regPass').value;
            const msg = document.getElementById('regMsg');
            const btn = document.getElementById('btnRegister');
            if(!username || !email || !password){ msg.innerText = '❌ الرجاء ملء جميع الحقول'; return; }
            if(username.length < 3){ msg.innerText = '❌ اسم المستخدم 3 أحرف على الأقل'; return; }
            if(password.length < 6){ msg.innerText = '❌ كلمة المرور 6 أحرف على الأقل'; return; }
            if(!email.includes('@') || !email.includes('.')){ msg.innerText = '❌ بريد إلكتروني غير صالح'; return; }
            btn.disabled = true; btn.innerHTML = '⏳ جاري إنشاء الحساب...'; msg.innerText = ''; msg.className = 'msg';
            try {
                const userCredential = await auth.createUserWithEmailAndPassword(email, password);
                const uid = userCredential.user.uid;
                const avatarUrl = DICEBEAR_URL + '?seed=' + uid;
                const coverColor = COVER_COLORS[Math.floor(Math.random() * COVER_COLORS.length)];
                const userData = {
                    username: username, email: email, bio: '',
                    website: '', location: '', contactEmail: '',
                    avatarUrl: avatarUrl, hasCustomAvatar: false,
                    coverImageUrl: '', hasCustomCover: false,
                    coverColor: coverColor, followers: {}, following: {},
                    totalLikes: 0, isVerified: false, verifiedAt: null, verifiedBy: null,
                    banned: false, createdAt: Date.now(), lastSeen: Date.now()
                };
                await db.ref('users/' + uid).set(userData);
                msg.innerText = '✅ تم إنشاء الحساب بنجاح! جاري التوجيه...';
                msg.className = 'msg success';
                setTimeout(() => { window.location.replace('index.html'); }, 800);
            } catch(error) {
                btn.disabled = false; btn.innerHTML = '<i class="fas fa-heart"></i> إنشاء حساب'; msg.className = 'msg';
                switch(error.code) {
                    case 'auth/email-already-in-use': msg.innerText = '❌ البريد الإلكتروني مستخدم بالفعل'; break;
                    case 'auth/weak-password': msg.innerText = '❌ كلمة المرور ضعيفة جداً'; break;
                    case 'auth/invalid-email': msg.innerText = '❌ بريد إلكتروني غير صالح'; break;
                    case 'auth/operation-not-allowed': msg.innerText = '❌ التسجيل غير مفعل، راجع إعدادات Firebase'; break;
                    default: msg.innerText = '❌ خطأ: ' + (error.message || 'غير معروف');
                }
            }
        }
        document.querySelectorAll('input').forEach(input => {
            input.addEventListener('keydown', function(e) {
                if(e.key === 'Enter') {
                    e.preventDefault();
                    if(document.getElementById('formLogin').classList.contains('active')) { doLogin(); }
                    else { doRegister(); }
                }
            });
        });
        auth.onAuthStateChanged(user => {
            if(user) { window.location.replace('index.html'); }
        });
        console.log('🟣 VIOLET Auth Ready');
    </script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# 🟣 5. index.html - الرئيسية (مع مشغل داخلي + Offline + PWA)
# ═══════════════════════════════════════════════════════════

def build_index():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    <title>🟣 VIOLET | الرئيسية</title>
    <link rel="manifest" href="/manifest.json">
    <meta name="theme-color" content="#7c3aed">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <link rel="apple-touch-icon" href="/icon-192.png">
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        :root{
            --glass:rgba(124,58,237,0.03);
            --border:rgba(124,58,237,0.12);
            --accent:#7c3aed;
            --accent2:#a855f7;
            --bg:#0a0812;
        }
        *{margin:0;padding:0;box-sizing:border-box}
        body{
            font-family:'Segoe UI',sans-serif;
            background:var(--bg);
            color:#fff;
            height:100vh;overflow:hidden;
            -webkit-tap-highlight-color:transparent;
            user-select:none;
        }

        #loaderScreen{
            position:fixed;inset:0;z-index:9999;
            background:radial-gradient(ellipse at top, #1a1030, #0a0812, #000000);
            display:flex;align-items:center;justify-content:center;
            flex-direction:column;gap:16px;
        }
        .spinner-big{
            width:50px;height:50px;
            border:4px solid rgba(124,58,237,0.15);
            border-top-color:var(--accent);
            border-radius:50%;
            animation:spin 0.8s linear infinite;
        }
        @keyframes spin{to{transform:rotate(360deg)}}

        #mainApp{display:none;height:100vh;position:relative}

        /* 📴 Offline Indicator */
        .offline-bar{
            position:fixed;top:0;left:0;right:0;z-index:200;
            background:rgba(239,68,68,0.9);color:#fff;text-align:center;
            padding:4px;font-size:11px;font-weight:600;
            backdrop-filter:blur(10px);
            display:none;
        }
        .offline-bar.show{display:block}

        .topbar{
            position:fixed;top:10px;left:10px;right:10px;z-index:100;
            display:flex;justify-content:space-between;align-items:center;
            padding:8px 16px;
            background:rgba(10,8,18,0.6);
            backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);
            border:1px solid var(--border);
            border-radius:50px;
            box-shadow:0 8px 32px rgba(124,58,237,0.06);
        }
        .logo-icon{
            width:34px;height:34px;
            background:linear-gradient(135deg,var(--accent),var(--accent2));
            border-radius:50%;display:flex;align-items:center;justify-content:center;
            font-weight:900;font-size:12px;
            box-shadow:0 0 20px rgba(124,58,237,0.4), 0 0 40px rgba(124,58,237,0.15);
            animation:pulseIcon 2s ease-in-out infinite;
        }
        @keyframes pulseIcon{0%,100%{box-shadow:0 0 20px rgba(124,58,237,0.4)}50%{box-shadow:0 0 35px rgba(168,85,247,0.7)}}
        .logo-text{
            font-weight:800;font-size:17px;
            background:linear-gradient(to bottom,#fff,#c084fc);
            -webkit-background-clip:text;-webkit-text-fill-color:transparent;
            margin-left:8px;
        }
        .tabs{display:flex;gap:4px;background:var(--glass);border-radius:30px;padding:3px}
        .tab{
            background:none;border:none;color:rgba(255,255,255,0.5);
            padding:7px 16px;cursor:pointer;border-radius:25px;
            font-size:13px;font-weight:500;transition:all 0.3s;
        }
        .tab.active{background:rgba(124,58,237,0.2);color:#a855f7}
        .top-icons{display:flex;gap:16px}
        .top-icon{
            background:none;border:none;color:rgba(255,255,255,0.7);
            font-size:18px;cursor:pointer;transition:all 0.3s;position:relative;
        }
        .top-icon:hover{color:var(--accent2)}
        .notif-badge{
            position:absolute;top:-4px;right:-4px;
            width:10px;height:10px;
            background:#ef4444;
            border-radius:50%;
            border:2px solid var(--bg);
            animation:badgePulse 2s ease-in-out infinite;
            display:none;
        }
        @keyframes badgePulse{0%,100%{transform:scale(1)}50%{transform:scale(1.5);box-shadow:0 0 10px #ef4444}}

        .videos-wrap{
            height:100vh;overflow-y:scroll;
            scroll-snap-type:y mandatory;
            scrollbar-width:none;-ms-overflow-style:none;
        }
        .videos-wrap::-webkit-scrollbar{display:none}
        .vid-card{height:100vh;scroll-snap-align:start;position:relative;background:#000}
        .vid-card video{width:100%;height:100%;object-fit:cover}

        .vid-info{
            position:absolute;bottom:90px;left:14px;right:80px;z-index:20;
            text-shadow:0 2px 10px rgba(0,0,0,0.8);
        }
        .author-row{display:flex;align-items:center;gap:10px;margin-bottom:6px}
        .author-avatar{
            width:50px;height:50px;border-radius:50%;overflow:hidden;
            cursor:pointer;position:relative;
            background:linear-gradient(135deg, #7c3aed, #a855f7, #c084fc);
            padding:3px;
            animation:storyRing 3s ease-in-out infinite;
        }
        @keyframes storyRing{0%,100%{box-shadow:0 0 15px rgba(124,58,237,0.35)}50%{box-shadow:0 0 25px rgba(192,132,252,0.7)}}
        .author-avatar img{width:100%;height:100%;object-fit:cover;border-radius:50%;border:2px solid var(--bg)}
        .author-name{
            font-weight:700;font-size:15px;cursor:pointer;
            display:flex;align-items:center;gap:6px;flex-wrap:wrap;
        }
        .verified-badge-main{
            background:linear-gradient(135deg, #7c3aed, #c084fc);
            color:#fff;
            font-size:10px;
            padding:2px 5px;
            border-radius:50%;
            display:inline-flex;
            align-items:center;
            justify-content:center;
            width:18px;
            height:18px;
            font-weight:bold;
            box-shadow:0 0 12px rgba(192,132,252,0.6);
        }
        .btn-follow{
            background:linear-gradient(135deg,var(--accent),var(--accent2));
            padding:5px 14px;border-radius:20px;font-size:11px;
            font-weight:700;border:none;color:#fff;cursor:pointer;
            box-shadow:0 4px 15px rgba(124,58,237,0.3);
            transition:all 0.3s;
        }
        .caption{font-size:14px;margin-bottom:5px;line-height:1.4}
        .tag{color:var(--accent2);cursor:pointer;font-weight:500}
        .music{font-size:12px;opacity:0.8;display:flex;align-items:center;gap:6px;cursor:pointer}
        .music-wave{display:flex;gap:2px;align-items:flex-end;height:16px}
        .music-wave span{width:2px;background:var(--accent2);border-radius:1px;animation:musicWave 1s ease-in-out infinite}
        .music-wave span:nth-child(1){height:8px;animation-delay:0s}
        .music-wave span:nth-child(2){height:14px;animation-delay:0.15s}
        .music-wave span:nth-child(3){height:6px;animation-delay:0.3s}
        .music-wave span:nth-child(4){height:12px;animation-delay:0.45s}
        .music-wave span:nth-child(5){height:4px;animation-delay:0.6s}
        @keyframes musicWave{0%,100%{transform:scaleY(1)}50%{transform:scaleY(1.8)}}

        .side-btns{
            position:absolute;right:14px;bottom:130px;
            display:flex;flex-direction:column;gap:22px;z-index:20;
        }
        .sbtn{
            display:flex;flex-direction:column;align-items:center;gap:3px;
            background:none;border:none;color:#fff;cursor:pointer;
            font-size:10px;transition:transform 0.15s;
        }
        .sbtn:active{transform:scale(0.85)}
        .sbtn i{font-size:28px;filter:drop-shadow(0 3px 8px rgba(0,0,0,0.5))}
        .sbtn.liked i{color:var(--accent);animation:likePop 0.4s ease}
        @keyframes likePop{0%{transform:scale(1)}50%{transform:scale(1.4)}100%{transform:scale(1)}}
        .sbtn .cnt{font-weight:700;font-size:11px}

        /* 🎬 Fullscreen Video Player */
        .fullscreen-player{position:fixed;top:0;left:0;width:100vw;height:100vh;background:#000;z-index:9999;display:flex;align-items:center;justify-content:center;opacity:0;pointer-events:none;transition:opacity 0.3s ease;flex-direction:column}
        .fullscreen-player.active{opacity:1;pointer-events:auto}
        .fullscreen-player video{max-width:100%;max-height:85vh;object-fit:contain;cursor:pointer}
        .player-controls{position:absolute;bottom:100px;left:20px;right:20px;display:flex;align-items:center;justify-content:space-between;background:rgba(10,8,18,0.6);backdrop-filter:blur(20px);border-radius:50px;padding:10px 20px;border:1px solid rgba(124,58,237,0.25);z-index:10000;color:#fff;gap:12px;flex-wrap:wrap}
        .player-controls button{background:none;border:none;color:#fff;font-size:20px;cursor:pointer;transition:color 0.2s;padding:5px}
        .player-controls button:hover{color:#c084fc}
        .progress-wrap{flex:1;display:flex;align-items:center;gap:8px;min-width:100px}
        .progress-bar{flex:1;height:4px;background:rgba(255,255,255,0.15);border-radius:4px;cursor:pointer;position:relative}
        .progress-fill{height:100%;background:linear-gradient(90deg, #7c3aed, #c084fc);border-radius:4px;width:0%}
        .close-player{position:absolute;top:20px;left:20px;background:rgba(10,8,18,0.5);backdrop-filter:blur(10px);border:1px solid rgba(124,58,237,0.35);color:#fff;width:44px;height:44px;border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;font-size:20px;z-index:10001}

        /* 🖼️ Image Lightbox */
        .image-lightbox{position:fixed;inset:0;background:rgba(10,8,18,0.96);backdrop-filter:blur(30px);z-index:9999;display:flex;align-items:center;justify-content:center;opacity:0;pointer-events:none;transition:opacity 0.3s ease;flex-direction:column}
        .image-lightbox.active{opacity:1;pointer-events:auto}
        .image-lightbox img{max-width:95vw;max-height:80vh;border-radius:16px;object-fit:contain;box-shadow:0 20px 60px rgba(124,58,237,0.2);border:1px solid rgba(124,58,237,0.15)}
        .lightbox-actions{display:flex;gap:20px;margin-top:20px;z-index:10000}
        .lightbox-actions button{background:rgba(124,58,237,0.12);border:1px solid rgba(124,58,237,0.3);color:#fff;width:48px;height:48px;border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;font-size:18px}
        .close-lightbox{position:absolute;top:20px;left:20px;background:rgba(10,8,18,0.5);backdrop-filter:blur(10px);border:1px solid rgba(124,58,237,0.35);color:#fff;width:44px;height:44px;border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;font-size:20px;z-index:10001}

        /* 📱 Bottom Nav */
        .nav-bottom{position:fixed;bottom:12px;left:12px;right:12px;display:flex;justify-content:space-around;align-items:center;padding:8px 0;background:rgba(10,8,18,0.7);backdrop-filter:blur(30px);z-index:100;border:1px solid var(--border);border-radius:40px;box-shadow:0 -8px 32px rgba(124,58,237,0.05)}
        .nav-item{display:flex;flex-direction:column;align-items:center;gap:3px;background:none;border:none;color:rgba(255,255,255,0.5);font-size:10px;cursor:pointer;text-decoration:none}
        .nav-item i{font-size:22px}
        .nav-item.active{color:var(--accent2)}
        .btn-add{width:48px;height:48px;background:linear-gradient(135deg,var(--accent),var(--accent2));border-radius:50%;display:flex;align-items:center;justify-content:center;margin-top:-30px;cursor:pointer;box-shadow:0 10px 30px rgba(124,58,237,0.5), 0 0 40px rgba(124,58,237,0.15);border:none;color:#fff;font-size:20px;z-index:101;text-decoration:none}

        .toast{position:fixed;bottom:120px;left:50%;transform:translateX(-50%);background:rgba(10,8,18,0.95);padding:12px 24px;border-radius:50px;z-index:1000;opacity:0;transition:opacity 0.3s;pointer-events:none;border:1px solid rgba(124,58,237,0.3);font-size:13px;box-shadow:0 8px 32px rgba(124,58,237,0.15)}
        .toast.show{opacity:1}

        .overlay{position:fixed;inset:0;background:rgba(10,8,18,0.97);backdrop-filter:blur(40px);z-index:400;overflow-y:auto}
        .overlay-header{display:flex;justify-content:space-between;align-items:center;padding:16px;border-bottom:1px solid var(--border);position:sticky;top:0;background:rgba(10,8,18,0.7)}
        .btn-close{background:rgba(124,58,237,0.1);border:1px solid var(--border);color:#fff;width:36px;height:36px;border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;font-size:18px}

        /* 📴 Offline Badge on Videos */
        .offline-badge{position:absolute;top:10px;left:10px;background:rgba(239,68,68,0.8);color:#fff;padding:4px 10px;border-radius:12px;font-size:10px;z-index:5;display:none}
        .offline-badge.show{display:block}
    </style>
</head>
<body>

<div id="loaderScreen">
    <div class="spinner-big"></div>
    <p style="color:rgba(255,255,255,0.5);font-size:15px">🟣 VIOLET جاري التحميل...</p>
    <p style="color:rgba(255,255,255,0.3);font-size:11px">PWA + Offline Mode</p>
</div>

<div class="offline-bar" id="offlineBar">📴 أنت غير متصل بالإنترنت - المحتوى المخزن متاح</div>

<div id="mainApp">
    <div class="topbar">
        <div style="display:flex;align-items:center">
            <div class="logo-icon">🟣</div>
            <span class="logo-text">VIOLET</span>
        </div>
        <div class="tabs">
            <button class="tab" onclick="switchFeed('following')">متابَعين</button>
            <button class="tab active" onclick="switchFeed('forYou')">لك</button>
        </div>
        <div class="top-icons">
            <i class="fas fa-search top-icon" onclick="openSearch()"></i>
            <i class="fas fa-bell top-icon" onclick="openNotifs()"><span class="notif-badge" id="notifBadge"></span></i>
        </div>
    </div>

    <div class="videos-wrap" id="videosWrap">
        <div style="display:flex;align-items:center;justify-content:center;height:100vh;color:rgba(255,255,255,0.5);flex-direction:column;gap:12px">
            <i class="fas fa-video" style="font-size:48px;opacity:0.3;color:#7c3aed"></i>
            <p>لا توجد فيديوهات بعد</p>
        </div>
    </div>

    <div class="fullscreen-player" id="fullscreenPlayer" onclick="if(event.target===this)closePlayer()">
        <button class="close-player" onclick="closePlayer()"><i class="fas fa-times"></i></button>
        <video id="fullscreenVideo" controls playsinline></video>
        <div class="player-controls">
            <button onclick="skipTime(-10)"><i class="fas fa-backward"></i></button>
            <button id="btnPlayPause" onclick="togglePlayPause()"><i class="fas fa-pause"></i></button>
            <button onclick="skipTime(10)"><i class="fas fa-forward"></i></button>
            <div class="progress-wrap">
                <span id="currentTime">0:00</span>
                <div class="progress-bar" id="progressBar" onclick="seekVideo(event)">
                    <div class="progress-fill" id="progressFill"></div>
                </div>
                <span id="duration">0:00</span>
            </div>
            <button onclick="toggleMutePlayer()"><i class="fas fa-volume-up" id="muteIcon"></i></button>
            <a id="downloadLink" href="#" download style="color:#c084fc;text-decoration:none;margin-left:10px;"><i class="fas fa-download"></i></a>
        </div>
    </div>

    <div class="image-lightbox" id="imageLightbox" onclick="if(event.target===this)closeLightbox()">
        <button class="close-lightbox" onclick="closeLightbox()"><i class="fas fa-times"></i></button>
        <img id="lightboxImage" src="" alt="صورة">
        <div class="lightbox-actions">
            <button onclick="downloadImage()"><i class="fas fa-download"></i></button>
            <button onclick="copyImageLink()"><i class="fas fa-link"></i></button>
        </div>
    </div>

    <div class="nav-bottom">
        <button class="nav-item active"><i class="fas fa-home"></i><span>الرئيسية</span></button>
        <button class="nav-item" onclick="openSearch()"><i class="fas fa-search"></i><span>بحث</span></button>
        <a href="upload.html" class="btn-add"><i class="fas fa-plus"></i></a>
        <a href="chat.html" class="nav-item"><i class="fas fa-envelope"></i><span>رسائل</span></a>
        <a href="profile.html" class="nav-item"><i class="fas fa-user"></i><span>ملفي</span></a>
    </div>

    <div id="toast" class="toast">✅ تم النسخ</div>
</div>

<script src="firebase-config.js"></script>
<script>
    let currentUser = null;
    let currentUserData = null;
    let allUsers = {};
    let allVideos = [];
    let allSounds = {};
    let isMuted = true;
    let currentFeed = 'forYou';
    let currentShareUrl = null;
    let playerVideo = null;

    // 📴 Offline Indicator
    window.addEventListener('online', () => { document.getElementById('offlineBar').classList.remove('show'); syncPendingActions(); });
    window.addEventListener('offline', () => { document.getElementById('offlineBar').classList.add('show'); });
    if (!navigator.onLine) { document.getElementById('offlineBar').classList.add('show'); }

    // 📱 PWA Install
    let deferredPrompt;
    window.addEventListener('beforeinstallprompt', (e) => {
        e.preventDefault();
        deferredPrompt = e;
        setTimeout(() => {
            if (deferredPrompt) {
                deferredPrompt.prompt();
                deferredPrompt.userChoice.then(() => { deferredPrompt = null; });
            }
        }, 3000);
    });

    // 🔄 Service Worker
    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('/sw.js').then(reg => {
            console.log('🟣 SW Registered:', reg.scope);
            reg.update();
        });
    }

    function openPlayer(url, title) {
        const player = document.getElementById('fullscreenPlayer');
        const video = document.getElementById('fullscreenVideo');
        player.classList.add('active');
        video.src = url;
        video.load();
        video.play();
        document.getElementById('downloadLink').href = url;
        document.getElementById('downloadLink').download = title || 'video.mp4';
        playerVideo = video;
        video.onloadedmetadata = () => {
            document.getElementById('duration').innerText = formatTime(video.duration);
        };
        video.ontimeupdate = () => {
            const pct = (video.currentTime / video.duration) * 100;
            document.getElementById('progressFill').style.width = pct + '%';
            document.getElementById('currentTime').innerText = formatTime(video.currentTime);
        };
    }
    window.openPlayer = openPlayer;
    function closePlayer() { const p = document.getElementById('fullscreenPlayer'); const v = document.getElementById('fullscreenVideo'); v.pause(); v.src=''; p.classList.remove('active'); }
    window.closePlayer = closePlayer;
    function togglePlayPause() { const v = document.getElementById('fullscreenVideo'); if(v.paused){v.play();document.getElementById('btnPlayPause').innerHTML='<i class="fas fa-pause"></i>';}else{v.pause();document.getElementById('btnPlayPause').innerHTML='<i class="fas fa-play"></i>';} }
    window.togglePlayPause = togglePlayPause;
    function skipTime(sec) { if(playerVideo) playerVideo.currentTime += sec; }
    window.skipTime = skipTime;
    function seekVideo(e) { if(!playerVideo) return; const bar = document.getElementById('progressBar'); const rect = bar.getBoundingClientRect(); const pct = (e.clientX - rect.left) / rect.width; playerVideo.currentTime = pct * playerVideo.duration; }
    window.seekVideo = seekVideo;
    function toggleMutePlayer() { if(playerVideo) { playerVideo.muted = !playerVideo.muted; document.getElementById('muteIcon').className = playerVideo.muted ? 'fas fa-volume-mute' : 'fas fa-volume-up'; } }
    window.toggleMutePlayer = toggleMutePlayer;

    function openLightbox(url) { const lb = document.getElementById('imageLightbox'); const img = document.getElementById('lightboxImage'); lb.classList.add('active'); img.src = url; img.setAttribute('data-url', url); }
    window.openLightbox = openLightbox;
    function closeLightbox() { const lb = document.getElementById('imageLightbox'); lb.classList.remove('active'); document.getElementById('lightboxImage').src=''; }
    window.closeLightbox = closeLightbox;
    function downloadImage() { const url = document.getElementById('lightboxImage').getAttribute('data-url'); if(url){const a=document.createElement('a');a.href=url;a.download='image.jpg';a.click();} }
    window.downloadImage = downloadImage;
    function copyImageLink() { const url = document.getElementById('lightboxImage').getAttribute('data-url'); if(url){navigator.clipboard.writeText(url).then(()=>{const t=document.getElementById('toast');t.classList.add('show');setTimeout(()=>t.classList.remove('show'),2000);});} }
    window.copyImageLink = copyImageLink;

    auth.onAuthStateChanged(async (user) => {
        if (!user) { window.location.replace('auth.html'); return; }
        currentUser = user;
        try {
            const snap = await db.ref('users/' + user.uid).get();
            if (snap.exists()) { currentUserData = { uid: user.uid, ...snap.val() }; }
        } catch(e) { console.error('Error loading user:', e); }

        db.ref('users').on('value', s => { allUsers = s.val() || {}; });
        db.ref('videos').on('value', s => {
            const data = s.val();
            if (!data) { allVideos = []; allSounds = {}; }
            else {
                allVideos = []; allSounds = {};
                Object.entries(data).forEach(([key, value]) => {
                    const video = { id: key, ...value };
                    allVideos.push(video);
                    if (video.music) { allSounds[video.music] = (allSounds[video.music] || 0) + 1; }
                });
                allVideos.sort((a, b) => (b.timestamp || 0) - (a.timestamp || 0));
            }
            renderVideos();
        });

        db.ref('notifications/' + user.uid).on('value', s => {
            const ns = s.val() || {};
            const badge = document.getElementById('notifBadge');
            if (badge) {
                const count = Object.keys(ns).length;
                badge.style.display = count > 0 ? 'block' : 'none';
                if (count > 0) {
                    badge.innerText = count;
                    badge.style.width = 'auto';
                    badge.style.padding = '2px 6px';
                    badge.style.borderRadius = '10px';
                    badge.style.fontSize = '9px';
                    badge.style.fontWeight = 'bold';
                } else {
                    badge.innerText = '';
                    badge.style.width = '10px';
                    badge.style.padding = '0';
                    badge.style.borderRadius = '50%';
                }
            }
        });

        db.ref('presence/' + user.uid).set(true);
        db.ref('presence/' + user.uid).onDisconnect().remove();
        db.ref('users/' + user.uid + '/lastSeen').set(Date.now());
        setInterval(() => { db.ref('users/' + user.uid + '/lastSeen').set(Date.now()); }, 60000);

        document.getElementById('loaderScreen').style.display = 'none';
        document.getElementById('mainApp').style.display = 'block';
    });

    async function sendNotification(toUserId, fromUsername, msg) {
        if (!currentUser) return;
        await db.ref('notifications/' + toUserId).push({
            from: fromUsername || currentUserData?.username || 'مستخدم',
            msg: msg,
            timestamp: Date.now(),
            read: false
        });
    }

    // 💾 Store video metadata offline
    async function storeVideoOffline(video) {
        try {
            const db_ = await new Promise((resolve) => {
                const req = indexedDB.open('VIOLET_Offline', 1);
                req.onsuccess = (e) => resolve(e.target.result);
            });
            const tx = db_.transaction(['videos'], 'readwrite');
            tx.objectStore('videos').put(video);
        } catch(e) {}
    }

    function renderVideos() {
        const container = document.getElementById('videosWrap');
        if (!container) return;
        let filtered = currentFeed === 'forYou' ? allVideos : allVideos.filter(v => currentUserData?.following?.[v.sender]);
        if (!filtered.length) {
            container.innerHTML = `<div style="display:flex;align-items:center;justify-content:center;height:100vh;color:rgba(255,255,255,0.5);flex-direction:column;gap:12px"><i class="fas fa-video" style="font-size:48px;opacity:0.3;color:#7c3aed"></i><p>${currentFeed === 'forYou' ? 'لا توجد فيديوهات بعد' : 'تابع مستخدمين لرؤية فيديوهاتهم'}</p>${!navigator.onLine ? '<p style="font-size:11px;opacity:0.4">📴 وضع عدم الاتصال</p>' : ''}</div>`;
            return;
        }
        container.innerHTML = '';
        filtered.forEach(video => {
            storeVideoOffline(video);
            const isLiked = video.likedBy && video.likedBy[currentUser?.uid];
            const user = allUsers[video.sender] || { username: video.senderName || 'مستخدم' };
            const isFollowing = currentUserData?.following && currentUserData.following[video.sender];
            const commentsCount = video.comments ? Object.keys(video.comments).length : 0;
            const caption = (video.description || '').replace(/#(\w+)/g, '<span class="tag">#$1</span>');
            const avatarUrl = user.avatarUrl || (DICEBEAR_URL + '?seed=' + video.sender);
            const verifiedBadgeHtml = user.isVerified ? '<span class="verified-badge-main"><i class="fas fa-check"></i></span>' : '';
            const musicHtml = video.music ? `<div class="music-wave">${[1,2,3,4,5].map(()=>'<span></span>').join('')}</div> ${video.music}` : 'Original Sound';

            const div = document.createElement('div');
            div.className = 'vid-card';
            div.innerHTML = `<video loop playsinline muted data-src="${video.url}" poster="${video.thumbnail || ''}"></video>
                <div class="vid-info">
                    <div class="author-row">
                        <div class="author-avatar" onclick="openUserProfile('${video.sender}')">
                            <img src="${avatarUrl}" alt="avatar">
                        </div>
                        <div class="author-name">
                            <span onclick="openUserProfile('${video.sender}')">@${user.username}</span>
                            ${verifiedBadgeHtml}
                            ${currentUser?.uid !== video.sender ? `<button class="btn-follow" onclick="event.stopPropagation();toggleFollow('${video.sender}', this)">${isFollowing ? '<i class="fas fa-user-check"></i> متابع' : '<i class="fas fa-user-plus"></i> متابعة'}</button>` : ''}
                        </div>
                    </div>
                    <div class="caption">${caption}</div>
                    <div class="music">${musicHtml}</div>
                </div>
                <div class="side-btns">
                    <button class="sbtn" onclick="toggleMute()"><i class="fas ${isMuted ? 'fa-volume-mute' : 'fa-volume-up'}"></i></button>
                    <button class="sbtn like-btn ${isLiked ? 'liked' : ''}" onclick="toggleLike('${video.id}', this)"><i class="fas fa-heart"></i><span class="cnt">${video.likes || 0}</span></button>
                    <button class="sbtn" onclick="openComments('${video.id}')"><i class="fas fa-comment"></i><span class="cnt">${commentsCount}</span></button>
                    <button class="sbtn" onclick="openPlayer('${video.url}', 'video.mp4')"><i class="fas fa-expand"></i></button>
                    <button class="sbtn" onclick="openShare('${video.url}')"><i class="fas fa-share"></i></button>
                </div>`;
            const videoEl = div.querySelector('video');
            videoEl.addEventListener('dblclick', e => {
                e.stopPropagation();
                const likeBtn = div.querySelector('.like-btn');
                if (likeBtn) toggleLike(video.id, likeBtn);
            });
            container.appendChild(div);
        });
        initVideoObserver();
    }

    function openUserProfile(userId) {
        if (userId === currentUser?.uid) { window.location.href = 'profile.html'; }
        else { window.location.href = 'profile.html?uid=' + userId; }
    }

    function initVideoObserver() {
        const observer = new IntersectionObserver(entries => {
            entries.forEach(entry => {
                const video = entry.target.querySelector('video');
                if (entry.isIntersecting) {
                    if (!video.src) video.src = video.dataset.src;
                    video.muted = isMuted;
                    video.play().catch(() => {});
                } else { video.pause(); }
            });
        }, { threshold: 0.65 });
        document.querySelectorAll('.vid-card').forEach(seg => observer.observe(seg));
    }

    function toggleMute() { isMuted = !isMuted; document.querySelectorAll('video').forEach(v => v.muted = isMuted); }
    function switchFeed(feed) { currentFeed = feed; document.querySelectorAll('.tab').forEach(t => t.classList.remove('active')); event.target.classList.add('active'); renderVideos(); }

    async function toggleLike(videoId, btn) {
        if (!currentUser) return;
        if (!navigator.onLine) {
            // 💾 حفظ الإعجاب محلياً للمزامنة لاحقاً
            const db_ = await new Promise((resolve) => {
                const req = indexedDB.open('VIOLET_Offline', 1);
                req.onsuccess = (e) => resolve(e.target.result);
            });
            const tx = db_.transaction(['pendingLikes'], 'readwrite');
            tx.objectStore('pendingLikes').put({ videoId, uid: currentUser.uid });
            btn.classList.add('liked');
            return;
        }
        const ref = db.ref('videos/' + videoId);
        const snap = await ref.get();
        const video = snap.val();
        if (!video) return;
        let likes = video.likes || 0;
        let likedBy = video.likedBy || {};
        if (likedBy[currentUser.uid]) { likes--; delete likedBy[currentUser.uid]; }
        else { 
            likes++; likedBy[currentUser.uid] = true;
            if (video.sender && video.sender !== currentUser.uid) {
                sendNotification(video.sender, currentUserData?.username, 'أعجب بفيديو الخاص بك ❤️');
            }
        }
        await ref.update({ likes, likedBy });
        btn.classList.toggle('liked');
        const countSpan = btn.querySelector('.cnt');
        if (countSpan) countSpan.innerText = likes;
    }

    async function toggleFollow(userId, btn) {
        if (!currentUser || currentUser.uid === userId) return;
        const userRef = db.ref('users/' + currentUser.uid + '/following/' + userId);
        const targetRef = db.ref('users/' + userId + '/followers/' + currentUser.uid);
        const snap = await userRef.get();
        if (snap.exists()) { await userRef.remove(); await targetRef.remove(); btn.innerHTML = '<i class="fas fa-user-plus"></i> متابعة'; }
        else { 
            await userRef.set(true); await targetRef.set(true); btn.innerHTML = '<i class="fas fa-user-check"></i> متابع';
            sendNotification(userId, currentUserData?.username, 'بدأ بمتابعتك 👤');
        }
    }

    function openShare(url) {
        currentShareUrl = url;
        showOverlay('📤 مشاركة', `<div onclick="copyLink()" style="display:flex;align-items:center;gap:12px;padding:14px;cursor:pointer;border-bottom:1px solid var(--border)"><i class="fas fa-link" style="color:#7c3aed;font-size:20px"></i><span>نسخ الرابط</span></div><div onclick="shareWA()" style="display:flex;align-items:center;gap:12px;padding:14px;cursor:pointer;border-bottom:1px solid var(--border)"><i class="fab fa-whatsapp" style="color:#25D366;font-size:20px"></i><span>WhatsApp</span></div><div onclick="shareTG()" style="display:flex;align-items:center;gap:12px;padding:14px;cursor:pointer"><i class="fab fa-telegram" style="color:#0088cc;font-size:20px"></i><span>Telegram</span></div>`);
    }
    window.copyLink = function() { navigator.clipboard.writeText(currentShareUrl); const t = document.getElementById('toast'); t.classList.add('show'); setTimeout(() => t.classList.remove('show'), 2000); closeOverlay(); };
    window.shareWA = function() { window.open('https://wa.me/?text=' + encodeURIComponent(currentShareUrl), '_blank'); closeOverlay(); };
    window.shareTG = function() { window.open('https://t.me/share/url?url=' + encodeURIComponent(currentShareUrl), '_blank'); closeOverlay(); };

    async function openComments(videoId) {
        if (!navigator.onLine) { showOverlay('💬 التعليقات', '<div style="text-align:center;opacity:0.5;padding:40px">📴 التعليقات غير متاحة بدون إنترنت</div>'); return; }
        const snap = await db.ref('videos/' + videoId + '/comments').get();
        const comments = snap.val() || {};
        let commentsList = '';
        Object.values(comments).reverse().forEach(c => {
            const user = allUsers[c.userId] || { username: c.username || 'مستخدم' };
            commentsList += `<div style="display:flex;gap:10px;padding:10px 0;border-bottom:1px solid rgba(124,58,237,0.1);animation:fadeIn 0.3s ease"><img src="${user.avatarUrl || (DICEBEAR_URL + '?seed=' + c.userId)}" style="width:36px;height:36px;border-radius:50%"><div><div style="font-weight:600">@${user.username}</div><div style="font-size:13px;opacity:0.8;margin-top:2px">${c.text}</div></div></div>`;
        });
        showOverlay('💬 التعليقات', commentsList + `<div style="display:flex;gap:8px;padding-top:12px"><input type="text" id="cmtInput" placeholder="أضف تعليقاً..." style="flex:1;padding:12px;border-radius:30px;background:rgba(124,58,237,0.04);border:1px solid rgba(124,58,237,0.15);color:#fff;outline:none"><button onclick="addComment('${videoId}')" style="background:linear-gradient(135deg,#7c3aed,#a855f7);border:none;color:#fff;padding:12px 20px;border-radius:30px;font-weight:700;cursor:pointer;white-space:nowrap">نشر</button></div>`);
    }
    window.addComment = async function(videoId) {
        const input = document.getElementById('cmtInput');
        if (!input || !input.value.trim()) return;
        const commentData = { userId: currentUser.uid, username: currentUserData?.username || 'مستخدم', text: input.value, timestamp: Date.now() };
        await db.ref('videos/' + videoId + '/comments').push(commentData);
        const videoSnap = await db.ref('videos/' + videoId).get();
        const video = videoSnap.val();
        if (video && video.sender !== currentUser.uid) {
            sendNotification(video.sender, currentUserData?.username, 'علق على فيديو الخاص بك 💬');
        }
        closeOverlay();
        openComments(videoId);
    };

    async function openNotifs() {
        const snap = await db.ref('notifications/' + currentUser.uid).once('value');
        const ns = snap.val() || {};
        const items = Object.values(ns).reverse();
        let notifHTML = '';
        if (!items.length) {
            notifHTML = '<div style="text-align:center;opacity:0.5;padding:40px"><i class="fas fa-bell" style="font-size:48px;color:#7c3aed;margin-bottom:12px;display:block"></i><p>لا توجد إشعارات</p></div>';
        } else {
            items.forEach(n => {
                notifHTML += `<div style="display:flex;gap:12px;padding:14px;border-bottom:1px solid rgba(124,58,237,0.1);align-items:center;animation:fadeIn 0.3s ease"><div style="width:40px;height:40px;border-radius:50%;background:rgba(124,58,237,0.12);display:flex;align-items:center;justify-content:center;font-size:18px;color:#7c3aed"><i class="fas fa-bell"></i></div><div><div style="font-weight:600">${n.from || 'مستخدم'}</div><div style="font-size:12px;opacity:0.6;margin-top:2px">${n.msg || ''}</div></div></div>`;
            });
        }
        await db.ref('notifications/' + currentUser.uid).remove();
        const badge = document.getElementById('notifBadge');
        if (badge) badge.style.display = 'none';
        showOverlay('🔔 الإشعارات', notifHTML);
    }

    function openSearch() {
        showOverlay('🔍 بحث', `<input type="text" id="searchQ" onkeyup="doSearch()" placeholder="ابحث عن مستخدمين، فيديوهات..." style="width:100%;padding:14px;border-radius:30px;background:rgba(124,58,237,0.04);border:1px solid rgba(124,58,237,0.15);color:#fff;font-size:14px;outline:none;margin-bottom:16px"><div id="searchR"></div>`);
        window.doSearch = function() {
            const query = document.getElementById('searchQ').value.toLowerCase();
            const resultsDiv = document.getElementById('searchR');
            if (!query) { resultsDiv.innerHTML = ''; return; }
            const users = Object.values(allUsers).filter(u => u.username?.toLowerCase().includes(query));
            const vids = allVideos.filter(v => (v.description || '').toLowerCase().includes(query));
            resultsDiv.innerHTML = `${users.length ? `<div style="margin-bottom:16px"><h4 style="font-size:12px;opacity:0.5;margin-bottom:8px"><i class="fas fa-users"></i> مستخدمين</h4>${users.map(u => `<div onclick="openUserProfile('${u.uid || Object.keys(allUsers).find(k=>allUsers[k]===u)}')" style="display:flex;align-items:center;gap:10px;padding:10px;cursor:pointer;border-bottom:1px solid rgba(124,58,237,0.1)"><img src="${u.avatarUrl || (DICEBEAR_URL + '?seed=' + (u.uid || u.username))}" style="width:40px;height:40px;border-radius:50%"><div>@${u.username} ${u.isVerified ? '<span class="verified-badge-main"><i class="fas fa-check"></i></span>' : ''}</div></div>`).join('')}</div>` : ''}${vids.length ? `<div><h4 style="font-size:12px;opacity:0.5;margin-bottom:8px"><i class="fas fa-video"></i> فيديوهات</h4>${vids.map(v => `<div onclick="openPlayer('${v.url}', 'video.mp4')" style="display:flex;align-items:center;gap:10px;padding:10px;cursor:pointer;border-bottom:1px solid rgba(124,58,237,0.1)"><i class="fas fa-play-circle" style="color:#7c3aed;font-size:20px"></i><span style="font-size:13px">${(v.description || 'فيديو').substring(0, 40)}</span></div>`).join('')}</div>` : ''}${!users.length && !vids.length ? '<div style="text-align:center;opacity:0.5;padding:30px">لا توجد نتائج</div>' : ''}`;
        };
        setTimeout(() => { const input = document.getElementById('searchQ'); if (input) input.focus(); }, 300);
    }

    function showOverlay(title, content) {
        const id = 'overlay_' + Date.now();
        const html = `<div id="${id}" class="overlay"><div class="overlay-header"><h3 style="font-weight:700">${title}</h3><button class="btn-close" onclick="document.getElementById('${id}').remove()"><i class="fas fa-times"></i></button></div><div style="padding:16px">${content}</div></div>`;
        document.body.insertAdjacentHTML('beforeend', html);
    }
    function closeOverlay() { document.querySelectorAll('[class="overlay"]').forEach(o => { if (o.id && o.id.startsWith('overlay_')) o.remove(); }); }

    function formatTime(seconds) {
        if (isNaN(seconds)) return '0:00';
        const m = Math.floor(seconds / 60);
        const s = Math.floor(seconds % 60);
        return m + ':' + (s < 10 ? '0' : '') + s;
    }

    console.log('🟣 VIOLET Index Ready ✨ | PWA + Offline');
</script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# 🟣 6-10. الملفات المتبقية
# ═══════════════════════════════════════════════════════════

def build_profile():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>🟣 VIOLET | ملف شخصي</title>
    <link rel="manifest" href="/manifest.json">
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        :root{--glass:rgba(124,58,237,0.04);--border:rgba(124,58,237,0.15);--accent:#7c3aed;--accent2:#a855f7;--bg:#0a0812;--card:rgba(124,58,237,0.05)}
        *{margin:0;padding:0;box-sizing:border-box}
        body{font-family:'Segoe UI',sans-serif;background:var(--bg);color:#fff;min-height:100vh;overflow-y:auto;overflow-x:hidden}
        .cover-section{position:relative;width:100%;height:260px;overflow:hidden;cursor:pointer}
        .cover-img{width:100%;height:130%;object-fit:cover;transition:transform 0.1s linear}
        .cover-gradient{position:absolute;inset:0;background:linear-gradient(to bottom, transparent 30%, rgba(10,8,18,0.4) 60%, rgba(10,8,18,0.95) 100%);pointer-events:none;z-index:1}
        .cover-glow{position:absolute;inset:0;background:radial-gradient(ellipse at center, rgba(124,58,237,0.12) 0%, transparent 70%);pointer-events:none;z-index:2}
        .cover-edit-btn{position:absolute;top:12px;left:12px;background:rgba(10,8,18,0.5);backdrop-filter:blur(15px);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:5;border:1px solid rgba(124,58,237,0.3);color:#a855f7;font-size:14px}
        .btn-back{position:fixed;top:20px;right:20px;background:rgba(10,8,18,0.5);backdrop-filter:blur(15px);width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:50;border:1px solid var(--border);color:#a855f7;font-size:16px}
        .avatar-wrap{position:relative;z-index:2;margin-top:-60px;display:flex;justify-content:center}
        .avatar-lg{width:120px;height:120px;border-radius:50%;overflow:hidden;cursor:pointer;background:linear-gradient(135deg, #7c3aed, #a855f7, #c084fc);padding:3px;box-shadow:0 0 30px rgba(124,58,237,0.35), 0 0 60px rgba(124,58,237,0.1);animation:avatarGlow 3s ease-in-out infinite}
        @keyframes avatarGlow{0%,100%{box-shadow:0 0 30px rgba(124,58,237,0.35)}50%{box-shadow:0 0 40px rgba(192,132,252,0.6)}}
        .avatar-lg img{width:100%;height:100%;object-fit:cover;border-radius:50%;border:3px solid var(--bg)}
        .badge-verified{background:linear-gradient(135deg, #7c3aed, #c084fc);color:#fff;font-size:12px;padding:3px 6px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;width:22px;height:22px;font-weight:bold;box-shadow:0 0 15px rgba(192,132,252,0.6);animation:verifyGlow 2s ease-in-out infinite}
        @keyframes verifyGlow{0%,100%{box-shadow:0 0 15px rgba(192,132,252,0.6)}50%{box-shadow:0 0 25px rgba(192,132,252,0.9)}}
        .profile-info{padding:20px 20px 10px;text-align:center}
        .username{font-size:22px;font-weight:800;margin-bottom:4px;display:flex;align-items:center;justify-content:center;gap:8px}
        .bio-text{font-size:13px;opacity:0.7;margin-bottom:8px;max-width:320px;margin-left:auto;margin-right:auto;line-height:1.5}
        .contact-info{display:flex;justify-content:center;gap:12px;flex-wrap:wrap;margin-bottom:8px;font-size:12px}
        .contact-info a{color:var(--accent2);text-decoration:none;display:flex;align-items:center;gap:5px;background:var(--card);padding:6px 14px;border-radius:20px;border:1px solid var(--border)}
        .stats-row{display:flex;justify-content:center;gap:30px;margin:15px 20px;padding:18px;background:rgba(124,58,237,0.04);backdrop-filter:blur(20px);border-radius:20px;border:1px solid var(--border);box-shadow:0 8px 32px rgba(0,0,0,0.2)}
        .stat-item{text-align:center;cursor:pointer;transition:transform 0.2s}
        .stat-item:hover{transform:scale(1.05)}
        .stat-val{font-size:20px;font-weight:700;color:var(--accent2)}
        .stat-lbl{font-size:10px;opacity:0.6;margin-top:2px}
        .action-btns{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin:0 20px 20px}
        .btn{background:rgba(124,58,237,0.06);border:1px solid var(--border);padding:10px 20px;border-radius:25px;color:#fff;cursor:pointer;font-size:13px;transition:all 0.3s;display:flex;align-items:center;gap:6px;backdrop-filter:blur(10px)}
        .btn:hover{background:rgba(124,58,237,0.15);border-color:var(--accent);box-shadow:0 0 20px rgba(124,58,237,0.2)}
        .btn-primary{background:linear-gradient(135deg,var(--accent),var(--accent2));border:none;font-weight:700;color:#fff;box-shadow:0 8px 25px rgba(124,58,237,0.35)}
        .btn-follow{background:linear-gradient(135deg,#ef4444,#dc2626);border:none;font-weight:700;color:#fff}
        .btn-follow.following{background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff}
        .section-title{font-size:16px;font-weight:700;padding:0 20px;margin-bottom:12px;display:flex;align-items:center;gap:8px}
        .videos-compact{padding:0 8px 80px}
        .video-compact-item{display:flex;gap:10px;margin-bottom:8px;background:rgba(124,58,237,0.03);border:1px solid rgba(124,58,237,0.08);border-radius:16px;padding:8px;cursor:pointer;transition:all 0.3s;backdrop-filter:blur(10px)}
        .video-compact-item:hover{background:rgba(124,58,237,0.06);border-color:var(--accent);box-shadow:0 0 20px rgba(124,58,237,0.1)}
        .video-compact-thumb{width:120px;aspect-ratio:9/16;border-radius:10px;overflow:hidden;position:relative;flex-shrink:0;background:#000}
        .video-compact-info{flex:1;min-width:0}
        .spinner{width:36px;height:36px;border:3px solid rgba(124,58,237,0.15);border-top-color:var(--accent);border-radius:50%;animation:spin 0.7s linear infinite;margin:30px auto}
        @keyframes spin{to{transform:rotate(360deg)}}
        .load-center{display:flex;align-items:center;justify-content:center;min-height:80vh;flex-direction:column;gap:12px;color:rgba(255,255,255,0.5)}
        .toast-msg{position:fixed;bottom:100px;left:50%;transform:translateX(-50%);background:rgba(10,8,18,0.95);padding:12px 24px;border-radius:30px;z-index:300;border:1px solid rgba(124,58,237,0.3);font-size:13px;opacity:0;transition:opacity 0.3s;pointer-events:none}
        .toast-msg.show{opacity:1}
        .edit-panel{position:fixed;bottom:0;left:0;right:0;background:rgba(10,8,18,0.98);backdrop-filter:blur(40px);border-top:2px solid var(--accent);border-radius:24px 24px 0 0;padding:24px 20px 40px;z-index:200;transform:translateY(100%);transition:transform 0.4s;max-height:80vh;overflow-y:auto}
        .edit-panel.show{transform:translateY(0)}
        .edit-panel h3{font-size:18px;font-weight:700;margin-bottom:20px;color:var(--accent2);text-align:center}
        .edit-panel label{display:block;font-size:12px;opacity:0.7;margin-bottom:6px;margin-top:14px}
        .edit-panel input,.edit-panel textarea{width:100%;padding:12px 16px;border-radius:14px;background:var(--card);border:1px solid var(--border);color:#fff;font-size:14px;outline:none;resize:none;font-family:'Segoe UI',sans-serif}
        .edit-actions{display:flex;gap:10px;margin-top:20px}
        .edit-actions button{flex:1;padding:12px;border-radius:25px;font-weight:700;cursor:pointer;font-size:14px}
        .btn-save{background:linear-gradient(135deg,var(--accent),var(--accent2));border:none;color:#fff}
        .btn-cancel{background:var(--card);border:1px solid var(--border);color:#fff}
        .overlay-panel{position:fixed;inset:0;background:rgba(0,0,0,0.7);z-index:150;display:none}
        .overlay-panel.show{display:block}
        .fullscreen-player{position:fixed;top:0;left:0;width:100vw;height:100vh;background:#000;z-index:9999;display:flex;align-items:center;justify-content:center;opacity:0;pointer-events:none;transition:opacity 0.3s ease;flex-direction:column}
        .fullscreen-player.active{opacity:1;pointer-events:auto}
        .fullscreen-player video{max-width:100%;max-height:85vh;object-fit:contain}
        .player-controls{position:absolute;bottom:100px;left:20px;right:20px;display:flex;align-items:center;justify-content:space-between;background:rgba(10,8,18,0.6);backdrop-filter:blur(20px);border-radius:50px;padding:10px 20px;border:1px solid rgba(124,58,237,0.25);z-index:10000;color:#fff;gap:12px;flex-wrap:wrap}
        .player-controls button{background:none;border:none;color:#fff;font-size:20px;cursor:pointer;padding:5px}
        .close-player{position:absolute;top:20px;left:20px;background:rgba(10,8,18,0.5);backdrop-filter:blur(10px);border:1px solid rgba(124,58,237,0.35);color:#fff;width:44px;height:44px;border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;font-size:20px;z-index:10001}
        .admin-panel{background:transparent;border:none;padding:0 8px;margin:0 8px 100px 8px}
        .admin-panel h3{color:#c084fc;font-size:20px;margin-bottom:20px;display:flex;align-items:center;gap:10px;font-weight:700}
        .admin-stats-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:12px;margin-bottom:24px}
        .stat-card{background:rgba(124,58,237,0.06);border:1px solid rgba(124,58,237,0.15);border-radius:16px;padding:16px;display:flex;align-items:center;gap:14px}
        .stat-icon{width:44px;height:44px;border-radius:12px;background:linear-gradient(135deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center;font-size:20px;box-shadow:0 4px 15px rgba(124,58,237,0.3)}
        .stat-info h4{font-size:12px;color:rgba(255,255,255,0.5);margin-bottom:4px;font-weight:500}
        .stat-info span{font-size:22px;font-weight:800}
        .admin-user-list-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;color:rgba(255,255,255,0.6);font-size:13px;font-weight:600;border-bottom:1px solid rgba(124,58,237,0.1);padding-bottom:8px}
        .admin-user-item{display:flex;align-items:center;justify-content:space-between;padding:10px 0;border-bottom:1px solid rgba(255,255,255,0.03);border-radius:8px;padding:8px}
        .admin-user-item:hover{background:rgba(124,58,237,0.04)}
        .admin-user-info{display:flex;align-items:center;gap:12px}
        .admin-avatar{width:40px;height:40px;border-radius:50%;background:#333;overflow:hidden;border:2px solid rgba(124,58,237,0.3)}
        .admin-avatar img{width:100%;height:100%;object-fit:cover}
        .admin-user-details h4{font-weight:600;font-size:15px;display:flex;align-items:center;gap:5px}
        .admin-user-details p{font-size:11px;color:rgba(255,255,255,0.4);margin-top:2px}
        .admin-user-actions{display:flex;gap:8px;align-items:center}
        .admin-btn{border:none;border-radius:20px;padding:8px 16px;font-size:12px;font-weight:700;cursor:pointer;transition:all 0.2s;display:flex;align-items:center;gap:5px}
        .btn-ban{background:rgba(255,255,255,0.1);color:#fff;border:1px solid rgba(255,255,255,0.1)}
        .btn-ban:hover{background:rgba(239,68,68,0.2)}
        .btn-unban{background:rgba(34,197,94,0.1);color:#4ade80;border:1px solid rgba(34,197,94,0.2)}
        .btn-verify{background:linear-gradient(135deg, #7c3aed, #c084fc);color:#fff;box-shadow:0 4px 12px rgba(124,58,237,0.3)}
        .btn-delete-video{background:rgba(239,68,68,0.1);color:#f87171;border:1px solid rgba(239,68,68,0.2)}
        .admin-video-item{display:flex;align-items:center;justify-content:space-between;padding:10px 0;border-bottom:1px solid rgba(255,255,255,0.03);border-radius:8px;padding:8px}
        .admin-video-item:hover{background:rgba(124,58,237,0.04)}
        .admin-video-info{display:flex;align-items:center;gap:12px;flex:1;min-width:0}
        .admin-video-thumb{width:50px;height:70px;border-radius:8px;overflow:hidden;background:#000;flex-shrink:0}
        .admin-video-thumb img{width:100%;height:100%;object-fit:cover}
        .admin-video-details{min-width:0}
        .admin-video-details p{font-size:12px;opacity:0.7;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
    </style>
</head>
<body>
<div class="fullscreen-player" id="fullscreenPlayer" onclick="if(event.target===this)closePlayer()">
    <button class="close-player" onclick="closePlayer()"><i class="fas fa-times"></i></button>
    <video id="fullscreenVideo" controls playsinline></video>
    <div class="player-controls">
        <button onclick="skipTime(-10)"><i class="fas fa-backward"></i></button>
        <button id="btnPlayPause" onclick="togglePlayPause()"><i class="fas fa-pause"></i></button>
        <button onclick="skipTime(10)"><i class="fas fa-forward"></i></button>
        <div class="progress-wrap"><div class="progress-bar"><div class="progress-fill" id="progressFill"></div></div></div>
        <button onclick="toggleMutePlayer()"><i class="fas fa-volume-up" id="muteIcon"></i></button>
        <a id="downloadLink" href="#" download style="color:#c084fc;text-decoration:none;margin-left:10px;"><i class="fas fa-download"></i></a>
    </div>
</div>
<div class="load-center" id="loader"><div class="spinner"></div><span>🟣 تحميل الملف...</span></div>
<div id="content" style="display:none">
    <div class="cover-section" id="coverSection" onmousemove="parallaxCover(event)">
        <img class="cover-img" id="coverImg" src="" alt="cover" style="display:none">
        <div class="cover-gradient"></div><div class="cover-glow"></div>
        <div class="cover-edit-btn" id="coverEditBtn" onclick="event.stopPropagation();document.getElementById('coverInput').click()" style="display:none"><i class="fas fa-camera"></i></div>
    </div>
    <input type="file" id="coverInput" accept="image/*" style="display:none" onchange="uploadCover(this)">
    <button class="btn-back" onclick="history.back()"><i class="fas fa-arrow-right"></i></button>
    <div class="avatar-wrap"><div class="avatar-lg" id="avatarDisplay"><img src="" alt="avatar" id="avatarImg"><div class="avatar-edit-btn" id="avatarEditBtn" onclick="event.stopPropagation();document.getElementById('avatarInput').click()" style="display:none"><i class="fas fa-camera"></i></div><div class="online-dot" id="onlineDot" style="display:none"></div></div></div>
    <input type="file" id="avatarInput" accept="image/*" style="display:none" onchange="uploadAvatar(this)">
    <div class="profile-info"><div class="username"><span id="nameDisplay"></span></div><div class="bio-text" id="bioDisplay"></div><div class="contact-info" id="contactInfo"></div><div class="last-seen" id="lastSeenDisplay"></div></div>
    <div class="stats-row">
        <div class="stat-item" onclick="showList('following')"><div class="stat-val" id="statFollowing">0</div><div class="stat-lbl">يتابع</div></div>
        <div class="stat-item" onclick="showList('followers')"><div class="stat-val" id="statFollowers">0</div><div class="stat-lbl">متابع</div></div>
        <div class="stat-item"><div class="stat-val" id="statLikes">0</div><div class="stat-lbl">إعجابات</div></div>
    </div>
    <div class="action-btns" id="actionsBar"></div>
    <div class="section-title"><i class="fas fa-video" style="color:var(--accent)"></i> الفيديوهات</div>
    <div class="videos-compact" id="videosContainer"></div>
</div>
<div class="overlay-panel" id="overlayPanel" onclick="closeEditPanel()"></div>
<div class="edit-panel" id="editPanel">
    <h3>🟣 لوحة تعديل الملف الشخصي</h3>
    <label>👤 اسم المستخدم</label><input type="text" id="editUsername" placeholder="اسم المستخدم">
    <label>📝 السيرة الذاتية</label><textarea id="editBio" placeholder="اكتب شيئاً عن نفسك..."></textarea>
    <label>🌐 الموقع الإلكتروني</label><input type="text" id="editWebsite" placeholder="https://example.com">
    <label>📧 البريد الإلكتروني</label><input type="text" id="editContactEmail" placeholder="example@email.com">
    <label>🎨 لون الغلاف</label><div id="coverColors" style="display:flex;gap:8px;flex-wrap:wrap;margin-top:8px"></div>
    <div class="edit-actions"><button class="btn-cancel" onclick="closeEditPanel()">إلغاء</button><button class="btn-save" onclick="saveProfile()"><i class="fas fa-save"></i> حفظ التغييرات</button></div>
</div>
<div class="toast-msg" id="toastMsg">✅ تم</div>
<script src="firebase-config.js"></script>
<script>
    let profileUserId=null,currentUser=null,currentUserData=null,allVideos=[],allUsers={},isOwnProfile=false,_selectedCover=null,playerVideo=null;
    if('serviceWorker' in navigator){navigator.serviceWorker.register('/sw.js')}
    function openPlayer(url,title){const p=document.getElementById('fullscreenPlayer');const v=document.getElementById('fullscreenVideo');p.classList.add('active');v.src=url;v.load();v.play();document.getElementById('downloadLink').href=url;playerVideo=v}
    window.openPlayer=openPlayer;
    function closePlayer(){const p=document.getElementById('fullscreenPlayer');const v=document.getElementById('fullscreenVideo');v.pause();v.src='';p.classList.remove('active')}
    window.closePlayer=closePlayer;
    function togglePlayPause(){const v=document.getElementById('fullscreenVideo');if(v.paused){v.play();document.getElementById('btnPlayPause').innerHTML='<i class="fas fa-pause"></i>'}else{v.pause();document.getElementById('btnPlayPause').innerHTML='<i class="fas fa-play"></i>'}}
    window.togglePlayPause=togglePlayPause;
    function skipTime(sec){if(playerVideo)playerVideo.currentTime+=sec}
    window.skipTime=skipTime;
    function toggleMutePlayer(){if(playerVideo){playerVideo.muted=!playerVideo.muted;document.getElementById('muteIcon').className=playerVideo.muted?'fas fa-volume-mute':'fas fa-volume-up'}}
    window.toggleMutePlayer=toggleMutePlayer;
    window.parallaxCover=function(event){const img=document.getElementById('coverImg');if(!img||!img.src||img.style.display==='none')return;const cover=document.getElementById('coverSection');const rect=cover.getBoundingClientRect();const y=event.clientY-rect.top;const percent=(y/rect.height-0.5)*0.15;img.style.transform=`translateY(${percent*100}px)`};
    function formatTime(seconds){if(isNaN(seconds))return'0:00';const m=Math.floor(seconds/60);const s=Math.floor(seconds%60);return m+':'+(s<10?'0':'')+s}
    auth.onAuthStateChanged(async u=>{if(!u){window.location.href='auth.html';return}currentUser=u;const params=new URLSearchParams(window.location.search);profileUserId=params.get('uid')||u.uid;isOwnProfile=(profileUserId===u.uid);const snap=await db.ref('users/'+u.uid).get();if(snap.exists())currentUserData={uid:u.uid,...snap.val()};await loadAll();await loadProfile();if(!isOwnProfile){db.ref('presence/'+profileUserId).on('value',s=>{const isOnline=s.val();const dot=document.getElementById('onlineDot');const lastSeen=document.getElementById('lastSeenDisplay');if(dot)dot.style.display=isOnline?'block':'none';if(lastSeen){const userData=allUsers[profileUserId];if(userData){lastSeen.innerHTML=isOnline?'<i class="fas fa-circle" style="color:#22c55e;font-size:8px"></i> نشط الآن':'<i class="fas fa-clock"></i> آخر ظهور: '+formatTime(userData.lastSeen)}}})}document.getElementById('loader').style.display='none';document.getElementById('content').style.display='block'});
    async function loadAll(){const us=await db.ref('users').once('value');allUsers=us.val()||{};const vs=await db.ref('videos').once('value');allVideos=Object.entries(vs.val()||{}).map(([k,v])=>({id:k,...v}))}
    async function loadProfile(){const u=allUsers[profileUserId];if(!u){document.getElementById('content').innerHTML='<div style="text-align:center;opacity:0.5;padding:100px 20px"><i class="fas fa-user-slash" style="font-size:48px;color:#7c3aed;margin-bottom:12px;display:block"></i><p>المستخدم غير موجود</p></div>';return}const badge=u.isVerified?'<span class="badge-verified"><i class="fas fa-check"></i></span>':'';document.getElementById('nameDisplay').innerHTML='@'+(u.username||'مستخدم')+' '+badge;document.getElementById('bioDisplay').innerText=u.bio||'لم تتم إضافة سيرة ذاتية بعد';const ci=document.getElementById('contactInfo');let ch='';if(u.website)ch+=`<a href="${u.website}" target="_blank"><i class="fas fa-globe"></i> ${u.website.replace('https://','').replace('http://','')}</a>`;if(u.contactEmail)ch+=`<a href="mailto:${u.contactEmail}"><i class="fas fa-envelope"></i> ${u.contactEmail}</a>`;ci.innerHTML=ch;document.getElementById('statFollowing').innerText=Object.keys(u.following||{}).length;document.getElementById('statFollowers').innerText=Object.keys(u.followers||{}).length;const uvs=allVideos.filter(v=>v.sender===profileUserId);document.getElementById('statLikes').innerText=uvs.reduce((s,v)=>s+(v.likes||0),0);const coverImg=document.getElementById('coverImg');if(u.coverImageUrl){coverImg.src=u.coverImageUrl;coverImg.style.display='block'}else{document.getElementById('coverSection').style.background=u.coverColor||COVER_COLORS[0];coverImg.style.display='none'}document.getElementById('avatarImg').src=u.avatarUrl||(DICEBEAR_URL+'?seed='+profileUserId);if(isOwnProfile){document.getElementById('avatarEditBtn').style.display='flex';document.getElementById('coverEditBtn').style.display='flex'}const vc=document.getElementById('videosContainer');vc.innerHTML='';if(!uvs.length){vc.innerHTML='<div style="text-align:center;opacity:0.5;padding:40px 20px"><i class="fas fa-video-slash" style="font-size:48px;color:#7c3aed;margin-bottom:12px;display:block"></i><p>لا توجد فيديوهات</p></div>'}else{uvs.sort((a,b)=>(b.timestamp||0)-(a.timestamp||0)).forEach(v=>{const d=document.createElement('div');d.className='video-compact-item';d.innerHTML=`<div class="video-compact-thumb" onclick="event.stopPropagation();openPlayer('${v.url}','video.mp4')">${v.thumbnail?`<img src="${v.thumbnail}" style="width:100%;height:100%;object-fit:cover">`:''}<div class="play-icon"><i class="fas fa-play"></i></div></div><div class="video-compact-info"><div class="vci-caption">${(v.description||'بدون وصف').substring(0,80)}</div><div class="vci-meta"><span><i class="fas fa-heart" style="color:#7c3aed"></i> ${v.likes||0}</span><span><i class="fas fa-comment"></i> ${v.comments?Object.keys(v.comments).length:0}</span></div></div>`;vc.appendChild(d)})}const ab=document.getElementById('actionsBar');if(isOwnProfile){ab.innerHTML=`<button class="btn btn-primary" onclick="openEditPanel()"><i class="fas fa-edit"></i> تعديل الملف</button><button class="btn" onclick="window.location.href='chat.html'"><i class="fas fa-envelope"></i> الرسائل</button><button class="btn" onclick="auth.signOut();window.location.href='auth.html'"><i class="fas fa-sign-out-alt"></i> خروج</button>`}else{const isFollowing=currentUserData?.following?.[profileUserId];ab.innerHTML=`<button class="btn btn-follow ${isFollowing?'following':''}" id="followBtn" onclick="toggleFollowUser()">${isFollowing?'<i class="fas fa-user-check"></i> متابع':'<i class="fas fa-user-plus"></i> متابعة'}</button><button class="btn btn-primary" onclick="window.location.href='chat.html?uid=${profileUserId}'"><i class="fas fa-comment"></i> مراسلة</button>`}if(isOwnProfile&&ADMIN_EMAILS.includes(currentUser?.email)){loadAdminPanel()}}
    function openEditPanel(){const u=allUsers[profileUserId]||currentUserData;document.getElementById('editUsername').value=u.username||'';document.getElementById('editBio').value=u.bio||'';document.getElementById('editWebsite').value=u.website||'';document.getElementById('editContactEmail').value=u.contactEmail||'';_selectedCover=u.coverColor||COVER_COLORS[0];const cd=document.getElementById('coverColors');cd.innerHTML=COVER_COLORS.map((c,i)=>`<div onclick="selectCover('${c.replace(/'/g,"\\\\'")}', this)" style="width:40px;height:40px;border-radius:50%;background:${c};cursor:pointer;border:3px solid ${_selectedCover===c?'#fff':'transparent'}"></div>`).join('');document.getElementById('editPanel').classList.add('show');document.getElementById('overlayPanel').classList.add('show')}
    function closeEditPanel(){document.getElementById('editPanel').classList.remove('show');document.getElementById('overlayPanel').classList.remove('show')}
    function selectCover(color,el){_selectedCover=color;document.getElementById('coverSection').style.background=color;document.getElementById('coverImg').style.display='none';document.querySelectorAll('#coverColors div').forEach(d=>d.style.borderColor='transparent');el.style.borderColor='#fff'}
    async function saveProfile(){const username=document.getElementById('editUsername').value.trim();const bio=document.getElementById('editBio').value.trim();const website=document.getElementById('editWebsite').value.trim();const contactEmail=document.getElementById('editContactEmail').value.trim();if(!username||username.length<3){showToast('❌ اسم المستخدم 3 أحرف على الأقل');return}const updates={username,bio,website,contactEmail};if(_selectedCover)updates.coverColor=_selectedCover;try{await db.ref('users/'+profileUserId).update(updates);closeEditPanel();await loadAll();await loadProfile();showToast('✅ تم حفظ التغييرات')}catch(e){showToast('❌ حدث خطأ')}}
    async function uploadAvatar(inp){const file=inp.files[0];if(!file)return;showToast('⏳ جاري رفع الصورة...');const fd=new FormData();fd.append('file',file);fd.append('upload_preset',UPLOAD_PRESET);try{const res=await fetch('https://api.cloudinary.com/v1_1/'+CLOUD_NAME+'/image/upload',{method:'POST',body:fd});const data=await res.json();if(data.secure_url){await db.ref('users/'+profileUserId).update({avatarUrl:data.secure_url,hasCustomAvatar:true});document.getElementById('avatarImg').src=data.secure_url;showToast('✅ تم تحديث الصورة')}}catch(e){showToast('❌ خطأ في الرفع')}inp.value=''}
    async function uploadCover(inp){const file=inp.files[0];if(!file)return;showToast('⏳ جاري رفع الغلاف...');const fd=new FormData();fd.append('file',file);fd.append('upload_preset',UPLOAD_PRESET);try{const res=await fetch('https://api.cloudinary.com/v1_1/'+CLOUD_NAME+'/image/upload',{method:'POST',body:fd});const data=await res.json();if(data.secure_url){await db.ref('users/'+profileUserId).update({coverImageUrl:data.secure_url,hasCustomCover:true});const ci=document.getElementById('coverImg');ci.src=data.secure_url;ci.style.display='block';document.getElementById('coverSection').style.background='none';showToast('✅ تم تحديث الغلاف')}}catch(e){showToast('❌ خطأ في الرفع')}inp.value=''}
    async function toggleFollowUser(){if(!currentUser||isOwnProfile)return;const btn=document.getElementById('followBtn');const userRef=db.ref('users/'+currentUser.uid+'/following/'+profileUserId);const targetRef=db.ref('users/'+profileUserId+'/followers/'+currentUser.uid);const snap=await userRef.get();if(snap.exists()){await userRef.remove();await targetRef.remove();btn.innerHTML='<i class="fas fa-user-plus"></i> متابعة';btn.classList.remove('following')}else{await userRef.set(true);await targetRef.set(true);btn.innerHTML='<i class="fas fa-user-check"></i> متابع';btn.classList.add('following')}await loadAll();await loadProfile()}
    function showList(type){const u=allUsers[profileUserId];const list=type==='followers'?(u?.followers||{}):(u?.following||{});const ids=Object.keys(list);if(!ids.length){alert('لا يوجد');return}const names=ids.map(id=>{const user=allUsers[id];return user?'@'+user.username:'مستخدم'}).join('\\n');alert((type==='followers'?'المتابِعون':'المتابَعون')+':\\n'+names)}
    function showToast(msg){const toast=document.getElementById('toastMsg');toast.innerText=msg;toast.classList.add('show');setTimeout(()=>toast.classList.remove('show'),2500)}
    async function loadAdminPanel(){const vc=document.getElementById('videosContainer');if(!vc)return;const op=document.getElementById('adminPanelContainer');if(op)op.remove();const ad=document.createElement('div');ad.id='adminPanelContainer';ad.className='admin-panel';const tu=Object.keys(allUsers).length;const tv=allVideos.length;const tver=Object.values(allUsers).filter(u=>u.isVerified).length;const tban=Object.values(allUsers).filter(u=>u.banned).length;ad.innerHTML=`<h3><i class="fas fa-crown"></i> لوحة تحكم الأدمن</h3><div class="admin-stats-grid"><div class="stat-card"><div class="stat-icon"><i class="fas fa-users"></i></div><div class="stat-info"><h4>المستخدمين</h4><span>${tu}</span></div></div><div class="stat-card"><div class="stat-icon" style="background:linear-gradient(135deg,#c084fc,#7c3aed)"><i class="fas fa-video"></i></div><div class="stat-info"><h4>فيديوهات</h4><span>${tv}</span></div></div><div class="stat-card"><div class="stat-icon" style="background:linear-gradient(135deg,#c084fc,#a855f7)"><i class="fas fa-check-circle"></i></div><div class="stat-info"><h4>موثقين</h4><span>${tver}</span></div></div><div class="stat-card"><div class="stat-icon" style="background:linear-gradient(135deg,#ef4444,#dc2626)"><i class="fas fa-ban"></i></div><div class="stat-info"><h4>محظورين</h4><span>${tban}</span></div></div></div><div class="admin-user-list-header"><span>📋 المستخدمين</span></div><div id="adminDynamicList"></div><div class="admin-user-list-header" style="margin-top:24px"><span>🎬 الفيديوهات</span></div><div id="adminVideosList"></div>`;vc.after(ad);loadAdminUsersList();loadAdminVideosList()}
    async function loadAdminUsersList(){const lc=document.getElementById('adminDynamicList');if(!lc)return;const ua=Object.entries(allUsers).sort(([,a],[,b])=>(b.createdAt||0)-(a.createdAt||0)).slice(0,15);lc.innerHTML=ua.map(([id,u])=>{const av=u.avatarUrl||(DICEBEAR_URL+'?seed='+id);const un=u.username||'مستخدم';const em=u.email||'';const iv=u.isVerified;const ib=u.banned;const vb=iv?'<span class="badge-verified"><i class="fas fa-check"></i></span>':'';let ab='';if(ib){ab=`<button class="admin-btn btn-unban" onclick="toggleBanUser('${id}')"><i class="fas fa-undo"></i> إلغاء الحظر</button>`}else{ab=`<button class="admin-btn btn-verify" onclick="toggleVerifyUser('${id}')">${iv?'<i class="fas fa-times-circle"></i> إلغاء':'<i class="fas fa-check-circle"></i> توثيق'}</button><button class="admin-btn btn-ban" onclick="toggleBanUser('${id}')"><i class="fas fa-ban"></i> حظر</button>`}return`<div class="admin-user-item"><div class="admin-user-info"><div class="admin-avatar"><img src="${av}"></div><div class="admin-user-details"><h4>@${un} ${vb}</h4><p>${em}</p></div></div><div class="admin-user-actions" onclick="event.stopPropagation()">${ab}</div></div>`}).join('')}
    function loadAdminVideosList(){const lc=document.getElementById('adminVideosList');if(!lc)return;const va=allVideos.sort((a,b)=>(b.timestamp||0)-(a.timestamp||0)).slice(0,20);lc.innerHTML=va.map(v=>{const u=allUsers[v.sender]||{username:v.senderName||'مستخدم'};const d=(v.description||'بدون وصف').substring(0,40);return`<div class="admin-video-item"><div class="admin-video-info"><div class="admin-video-thumb">${v.thumbnail?`<img src="${v.thumbnail}">`:''}</div><div class="admin-video-details"><p>${d}</p><span>@${u.username} · ❤️ ${v.likes||0}</span></div></div><div class="admin-user-actions"><button class="admin-btn btn-delete-video" onclick="deleteVideo('${v.id}')"><i class="fas fa-trash"></i> حذف</button></div></div>`}).join('')}
    window.deleteVideo=async function(vid){if(!confirm('هل أنت متأكد من حذف هذا الفيديو؟'))return;try{await db.ref('videos/'+vid).remove();showToast('🗑️ تم حذف الفيديو');await loadAll();await loadProfile();loadAdminVideosList()}catch(e){showToast('❌ فشل حذف الفيديو')}}
    window.toggleVerifyUser=async function(id){const snap=await db.ref('users/'+id).once('value');const data=snap.val();if(!data)return;const ns=!data.isVerified;if(!confirm(`تأكيد ${ns?'توثيق':'إلغاء توثيق'} @${data.username||'المستخدم'}؟`))return;await db.ref('users/'+id).update({isVerified:ns,verifiedAt:ns?Date.now():null,verifiedBy:ns?currentUser.uid:null});await loadAll();await loadProfile();showToast(`✅ تم ${ns?'توثيق':'إلغاء توثيق'} المستخدم`);loadAdminUsersList()}
    window.toggleBanUser=async function(id){const snap=await db.ref('users/'+id).once('value');const data=snap.val();if(!data)return;const ns=!data.banned;if(!confirm(`تأكيد ${ns?'حظر':'إلغاء حظر'} @${data.username||'المستخدم'}؟`))return;await db.ref('users/'+id).update({banned:ns,bannedAt:ns?Date.now():null,bannedBy:ns?currentUser.uid:null});await loadAll();await loadProfile();showToast(`✅ تم ${ns?'حظر':'إلغاء حظر'} المستخدم`);loadAdminUsersList()}
    console.log('🟣 VIOLET Profile Ready ✨')
</script>
</body>
</html>"""

def build_upload():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>🟣 VIOLET | رفع فيديو</title>
    <link rel="manifest" href="/manifest.json">
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        :root{--glass:rgba(124,58,237,0.03);--border:rgba(124,58,237,0.12);--accent:#7c3aed;--accent2:#a855f7;--bg:#0a0812}
        *{margin:0;padding:0;box-sizing:border-box}
        body{font-family:'Segoe UI',sans-serif;background:var(--bg);color:#fff;min-height:100vh;overflow-y:auto}
        .header{display:flex;align-items:center;gap:12px;padding:16px;border-bottom:1px solid var(--border);background:rgba(10,8,18,0.7);backdrop-filter:blur(20px);position:sticky;top:0;z-index:10}
        .btn-back{background:rgba(124,58,237,0.1);border:1px solid var(--border);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#a855f7;cursor:pointer;font-size:16px}
        .container{max-width:500px;margin:0 auto;padding:20px}
        .dropzone{border:2px dashed rgba(124,58,237,0.3);border-radius:20px;padding:50px 20px;text-align:center;cursor:pointer;background:var(--glass);margin-bottom:20px}
        .dropzone i{font-size:48px;color:var(--accent)}
        .dropzone video{width:100%;max-height:250px;object-fit:contain;margin-top:12px;border-radius:12px;display:none}
        .form-card{background:rgba(124,58,237,0.03);border:1px solid var(--border);border-radius:20px;padding:20px}
        .form-card label{display:block;font-size:13px;opacity:0.7;margin-bottom:6px;margin-top:12px}
        .form-card textarea,.form-card input{width:100%;padding:14px 16px;border-radius:16px;background:rgba(124,58,237,0.04);border:1px solid var(--border);color:#fff;font-size:14px;outline:none;resize:none;font-family:'Segoe UI',sans-serif}
        .progress-wrap{display:none;margin:16px 0}
        .progress-bar{background:rgba(255,255,255,0.1);border-radius:30px;height:6px;overflow:hidden}
        .progress-fill{background:linear-gradient(90deg,var(--accent),var(--accent2));height:100%;border-radius:30px;width:0%}
        .btn-upload{width:100%;padding:14px;background:linear-gradient(135deg,var(--accent),var(--accent2));border:none;border-radius:30px;color:#fff;font-weight:700;font-size:15px;cursor:pointer;margin-top:16px;box-shadow:0 10px 25px rgba(124,58,237,0.3)}
        .btn-upload:disabled{opacity:0.5}
        .status{text-align:center;margin-top:12px;font-size:13px}
    </style>
</head>
<body>
<div class="header"><button class="btn-back" onclick="window.location.href='index.html'"><i class="fas fa-arrow-right"></i></button><h2><i class="fas fa-cloud-upload-alt"></i> رفع فيديو جديد</h2></div>
<div class="container">
    <div class="dropzone" onclick="document.getElementById('videoFile').click()"><i class="fas fa-cloud-upload-alt"></i><p>اضغط لاختيار فيديو</p><span style="font-size:11px;opacity:0.5">MP4 - حتى 100MB</span><video id="preview" controls></video></div>
    <input type="file" id="videoFile" accept="video/*" style="display:none" onchange="onFilePick(this)">
    <div class="form-card">
        <label><i class="fas fa-pen"></i> وصف الفيديو</label><textarea id="vidDesc" placeholder="اكتب وصفاً..."></textarea>
        <label><i class="fas fa-music"></i> الموسيقى</label><input type="text" id="vidMusic" placeholder="Original Sound">
        <div class="progress-wrap" id="progressWrap"><div class="progress-bar"><div class="progress-fill" id="progressFill"></div></div><div class="progress-text" id="progressText">0%</div></div>
        <button class="btn-upload" id="uploadBtn" onclick="upload()"><i class="fas fa-heart"></i> رفع الفيديو</button>
        <div class="status" id="status"></div>
    </div>
</div>
<script src="firebase-config.js"></script>
<script>
    if('serviceWorker' in navigator){navigator.serviceWorker.register('/sw.js')}
    let currentUser=null,currentUserData=null,selectedFile=null;
    auth.onAuthStateChanged(async u=>{if(!u)window.location.href='auth.html';currentUser=u;const snap=await db.ref('users/'+u.uid).get();if(snap.exists())currentUserData={uid:u.uid,...snap.val()}});
    function onFilePick(inp){const f=inp.files[0];if(!f||!f.type.startsWith('video/')){alert('اختر فيديو صحيح');return}if(f.size>100*1024*1024){alert('أقل من 100MB');return}selectedFile=f;const r=new FileReader();r.onload=e=>{const v=document.getElementById('preview');v.src=e.target.result;v.style.display='block'};r.readAsDataURL(f)}
    async function upload(){
        if(!selectedFile){alert('اختر فيديو');return}if(!currentUser){alert('سجل دخول');return}
        if(!navigator.onLine){alert('📴 تحتاج إنترنت للرفع');return}
        const desc=document.getElementById('vidDesc').value;const music=document.getElementById('vidMusic').value||'Original Sound';
        const pw=document.getElementById('progressWrap');pw.style.display='block';const pf=document.getElementById('progressFill');pf.style.width='0%';document.getElementById('progressText').innerText='0%';
        const st=document.getElementById('status');st.innerHTML='';const btn=document.getElementById('uploadBtn');btn.disabled=true;
        const fd=new FormData();fd.append('file',selectedFile);fd.append('upload_preset',UPLOAD_PRESET);
        const xhr=new XMLHttpRequest();xhr.open('POST','https://api.cloudinary.com/v1_1/'+CLOUD_NAME+'/video/upload');
        xhr.upload.onprogress=e=>{if(e.lengthComputable){const p=Math.round(e.loaded/e.total*100);pf.style.width=p+'%';document.getElementById('progressText').innerText=p+'%'}};
        xhr.onload=async()=>{const r=JSON.parse(xhr.responseText);await db.ref('videos/').push({url:r.secure_url,thumbnail:r.secure_url.replace('.mp4','.jpg'),description:desc,music:music,sender:currentUser.uid,senderName:currentUserData?.username,likes:0,likedBy:{},comments:{},timestamp:Date.now()});st.innerHTML='✅ تم الرفع بنجاح!';st.style.color='#4ade80';setTimeout(()=>window.location.href='index.html',1500)};
        xhr.onerror=()=>{st.innerHTML='❌ فشل الرفع';btn.disabled=false};xhr.send(fd);
    }
</script>
</body>
</html>"""

def build_chat():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>🟣 VIOLET | دردشة</title>
    <link rel="manifest" href="/manifest.json">
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        :root{--glass:rgba(124,58,237,0.03);--border:rgba(124,58,237,0.12);--accent:#7c3aed;--accent2:#a855f7;--bg:#0a0812}
        *{margin:0;padding:0;box-sizing:border-box}
        body{font-family:'Segoe UI',sans-serif;background:var(--bg);color:#fff;height:100vh;display:flex;flex-direction:column}
        .header{display:flex;align-items:center;gap:12px;padding:16px;border-bottom:1px solid var(--border);background:rgba(10,8,18,0.7);backdrop-filter:blur(20px)}
        .btn-back{background:rgba(124,58,237,0.1);border:1px solid var(--border);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#a855f7;cursor:pointer;font-size:16px}
        .msgs{flex:1;overflow-y:auto;padding:16px;display:flex;flex-direction:column;gap:8px}
        .bubble{max-width:80%;padding:10px 16px;border-radius:20px;word-break:break-word;font-size:14px;animation:msgIn 0.3s ease}
        @keyframes msgIn{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:translateY(0)}}
        .bubble.sent{background:linear-gradient(135deg,var(--accent),var(--accent2));align-self:flex-end;color:#fff}
        .bubble.received{background:rgba(124,58,237,0.06);align-self:flex-start;border:1px solid rgba(124,58,237,0.1)}
        .bubble img{max-width:200px;border-radius:12px;cursor:pointer;margin-top:4px}
        .input-bar{display:flex;gap:10px;padding:12px;background:rgba(10,8,18,0.95);backdrop-filter:blur(20px);border-top:1px solid var(--border);align-items:center}
        .input-bar input{flex:1;padding:12px 16px;border-radius:30px;background:var(--glass);border:1px solid var(--border);color:#fff;font-size:14px;outline:none}
        .btn-send{width:42px;height:42px;background:linear-gradient(135deg,var(--accent),var(--accent2));border:none;border-radius:50%;color:#fff;cursor:pointer;font-size:18px;display:flex;align-items:center;justify-content:center}
        .image-lightbox{position:fixed;inset:0;background:rgba(10,8,18,0.96);backdrop-filter:blur(30px);z-index:9999;display:flex;align-items:center;justify-content:center;opacity:0;pointer-events:none;flex-direction:column}
        .image-lightbox.active{opacity:1;pointer-events:auto}
        .image-lightbox img{max-width:95vw;max-height:80vh;border-radius:16px;object-fit:contain}
        .close-lightbox{position:absolute;top:20px;left:20px;background:rgba(10,8,18,0.5);border:1px solid rgba(124,58,237,0.35);color:#fff;width:44px;height:44px;border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;font-size:20px;z-index:10001}
        .spinner{width:32px;height:32px;border:3px solid rgba(124,58,237,0.15);border-top-color:var(--accent);border-radius:50%;animation:spin 0.7s linear infinite;margin:30px auto}
        @keyframes spin{to{transform:rotate(360deg)}}
    </style>
</head>
<body>
<div class="image-lightbox" id="imageLightbox" onclick="if(event.target===this)closeLightbox()"><button class="close-lightbox" onclick="closeLightbox()"><i class="fas fa-times"></i></button><img id="lightboxImage" src="" alt="صورة"></div>
<div id="loader" style="flex:1;display:flex;align-items:center;justify-content:center"><div class="spinner"></div></div>
<div id="chatView" style="display:none;flex:1;flex-direction:column;overflow:hidden"><div class="header"><button class="btn-back" onclick="window.location.href='index.html'"><i class="fas fa-arrow-right"></i></button><h3 id="chatName">محادثة</h3></div><div class="msgs" id="msgsList"></div><div class="input-bar"><input type="text" id="msgInput" placeholder="اكتب رسالة..." onkeydown="if(event.key==='Enter')sendMsg()"><button class="btn-send" onclick="sendMsg()"><i class="fas fa-paper-plane"></i></button></div></div>
<script src="firebase-config.js"></script>
<script>
    if('serviceWorker' in navigator){navigator.serviceWorker.register('/sw.js')}
    let currentUser=null,allUsers={},chatUserId=null;
    auth.onAuthStateChanged(async u=>{if(!u){window.location.href='auth.html';return}currentUser=u;const us=await db.ref('users').once('value');allUsers=us.val()||{};document.getElementById('loader').style.display='none';const params=new URLSearchParams(window.location.search);const targetUid=params.get('uid');if(targetUid){openChat(targetUid)}});
    async function openChat(uid){chatUserId=uid;const u=allUsers[uid];document.getElementById('chatName').innerText='@'+(u?.username||'مستخدم');document.getElementById('chatView').style.display='flex';await loadMsgs()}
    function getChatId(){return[currentUser.uid,chatUserId].sort().join('_')}
    async function loadMsgs(){const ml=document.getElementById('msgsList');ml.innerHTML='';if(!chatUserId)return;const snap=await db.ref('private_messages/'+getChatId()).once('value');const ms=snap.val()||{};Object.values(ms).sort((a,b)=>a.timestamp-b.timestamp).forEach(m=>{const sent=m.senderId===currentUser.uid;const d=document.createElement('div');d.className='bubble '+(sent?'sent':'received');d.innerHTML=m.type==='image'?`<img src="${m.imageUrl}" onclick="openLightbox('${m.imageUrl}')">`:m.text;ml.appendChild(d)});ml.scrollTop=ml.scrollHeight}
    async function sendMsg(){const inp=document.getElementById('msgInput');const txt=inp.value.trim();if(!txt||!chatUserId)return;await db.ref('private_messages/'+getChatId()).push({senderId:currentUser.uid,text:txt,type:'text',timestamp:Date.now()});inp.value='';await loadMsgs()}
    function openLightbox(url){const lb=document.getElementById('imageLightbox');lb.classList.add('active');document.getElementById('lightboxImage').src=url}
    window.openLightbox=openLightbox;
    function closeLightbox(){document.getElementById('imageLightbox').classList.remove('active')}
    window.closeLightbox=closeLightbox;
</script>
</body>
</html>"""

def build_explore():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>🟣 VIOLET | استكشاف</title>
    <link rel="manifest" href="/manifest.json">
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        :root{--accent:#7c3aed;--border:rgba(124,58,237,0.12);--bg:#0a0812}
        *{margin:0;padding:0;box-sizing:border-box}
        body{font-family:'Segoe UI',sans-serif;background:var(--bg);color:#fff;min-height:100vh;overflow-y:auto}
        .header{display:flex;align-items:center;gap:12px;padding:16px;border-bottom:1px solid var(--border);position:sticky;top:0;background:rgba(10,8,18,0.7);backdrop-filter:blur(20px);z-index:10}
        .btn-back{background:rgba(124,58,237,0.1);border:1px solid var(--border);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#a855f7;cursor:pointer;font-size:16px}
        .grid{display:grid;grid-template-columns:repeat(3,1fr);gap:2px;padding:2px}
        .thumb{aspect-ratio:9/16;background:rgba(124,58,237,0.05);display:flex;align-items:center;justify-content:center;cursor:pointer;position:relative;overflow:hidden}
        .thumb img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
        .thumb .views{position:absolute;bottom:4px;left:4px;font-size:10px;background:rgba(0,0,0,0.6);padding:2px 6px;border-radius:10px}
        .spinner{width:32px;height:32px;border:3px solid rgba(124,58,237,0.15);border-top-color:var(--accent);border-radius:50%;animation:spin 0.7s linear infinite;margin:30px auto}
        @keyframes spin{to{transform:rotate(360deg)}}
    </style>
</head>
<body>
<div class="header"><button class="btn-back" onclick="window.location.href='index.html'"><i class="fas fa-arrow-right"></i></button><h2><i class="fas fa-globe"></i> استكشاف</h2></div>
<div class="grid" id="exploreGrid"><div class="spinner" style="grid-column:1/-1"></div></div>
<script src="firebase-config.js"></script>
<script>
    if('serviceWorker' in navigator){navigator.serviceWorker.register('/sw.js')}
    let currentUser=null;
    auth.onAuthStateChanged(async u=>{if(!u){window.location.href='auth.html';return}currentUser=u;loadExplore()});
    async function loadExplore(){
        const snap=await db.ref('videos').once('value');const videos=snap.val()||{};
        const allVids=Object.entries(videos).map(([k,v])=>({id:k,...v})).sort((a,b)=>(b.likes||0)-(a.likes||0));
        const g=document.getElementById('exploreGrid');
        if(!allVids.length){g.innerHTML='<div style="text-align:center;padding:40px;grid-column:1/-1;opacity:0.5">لا توجد فيديوهات</div>';return}
        g.innerHTML=allVids.map(v=>`<div class="thumb" onclick="window.open('${v.url}','_blank')">${v.thumbnail?`<img src="${v.thumbnail}">`:''}<i class="fas fa-play"></i><span class="views"><i class="fas fa-heart"></i> ${v.likes||0}</span></div>`).join('');
    }
</script>
</body>
</html>"""

def build_notifications():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>🟣 VIOLET | إشعارات</title>
    <link rel="manifest" href="/manifest.json">
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        :root{--accent:#7c3aed;--border:rgba(124,58,237,0.12);--bg:#0a0812}
        *{margin:0;padding:0;box-sizing:border-box}
        body{font-family:'Segoe UI',sans-serif;background:var(--bg);color:#fff;min-height:100vh;overflow-y:auto}
        .header{display:flex;align-items:center;gap:12px;padding:16px;border-bottom:1px solid var(--border);position:sticky;top:0;background:rgba(10,8,18,0.7);backdrop-filter:blur(20px);z-index:10}
        .btn-back{background:rgba(124,58,237,0.1);border:1px solid var(--border);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#a855f7;cursor:pointer;font-size:16px}
        .notif-item{display:flex;gap:12px;padding:14px 16px;border-bottom:1px solid var(--border);align-items:center}
        .notif-icon{width:40px;height:40px;border-radius:50%;background:rgba(124,58,237,0.1);display:flex;align-items:center;justify-content:center;font-size:18px;color:var(--accent)}
        .spinner{width:32px;height:32px;border:3px solid rgba(124,58,237,0.15);border-top-color:var(--accent);border-radius:50%;animation:spin 0.7s linear infinite;margin:30px auto}
        @keyframes spin{to{transform:rotate(360deg)}}
    </style>
</head>
<body>
<div class="header"><button class="btn-back" onclick="window.location.href='index.html'"><i class="fas fa-arrow-right"></i></button><h2><i class="fas fa-bell"></i> الإشعارات</h2></div>
<div id="notifsList"><div class="spinner"></div></div>
<script src="firebase-config.js"></script>
<script>
    if('serviceWorker' in navigator){navigator.serviceWorker.register('/sw.js')}
    let currentUser=null;
    auth.onAuthStateChanged(async u=>{if(!u){window.location.href='auth.html';return}currentUser=u;loadNotifs()});
    async function loadNotifs(){
        const snap=await db.ref('notifications/'+currentUser.uid).once('value');const ns=snap.val()||{};
        const c=document.getElementById('notifsList');const items=Object.values(ns).reverse();
        if(!items.length){c.innerHTML='<div style="text-align:center;opacity:0.5;padding:40px"><i class="fas fa-bell" style="font-size:48px;color:#7c3aed;display:block;margin-bottom:12px"></i><p>لا توجد إشعارات</p></div>';return}
        c.innerHTML=items.map(n=>`<div class="notif-item"><div class="notif-icon"><i class="fas fa-bell"></i></div><div><div style="font-weight:600">${n.from||'مستخدم'}</div><div style="font-size:12px;opacity:0.6;margin-top:2px">${n.msg||''}</div></div></div>`).join('');
    }
</script>
</body>
</html>"""

def build_settings():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>🟣 VIOLET | إعدادات</title>
    <link rel="manifest" href="/manifest.json">
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        :root{--accent:#7c3aed;--border:rgba(124,58,237,0.12);--bg:#0a0812;--glass:rgba(124,58,237,0.03)}
        *{margin:0;padding:0;box-sizing:border-box}
        body{font-family:'Segoe UI',sans-serif;background:var(--bg);color:#fff;min-height:100vh;overflow-y:auto}
        .header{display:flex;align-items:center;gap:12px;padding:16px;border-bottom:1px solid var(--border);position:sticky;top:0;background:rgba(10,8,18,0.7);backdrop-filter:blur(20px);z-index:10}
        .btn-back{background:rgba(124,58,237,0.1);border:1px solid var(--border);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#a855f7;cursor:pointer;font-size:16px}
        .setting-item{display:flex;justify-content:space-between;align-items:center;padding:16px;border-bottom:1px solid var(--border);cursor:pointer}
        .setting-item:hover{background:var(--glass)}
        .setting-item i{color:var(--accent);font-size:18px;width:30px}
        .btn-danger{background:rgba(239,68,68,0.2);border:1px solid rgba(239,68,68,0.3);color:#f87171;padding:12px 24px;border-radius:30px;cursor:pointer;font-size:14px;margin:20px auto;display:block}
    </style>
</head>
<body>
<div class="header"><button class="btn-back" onclick="window.location.href='index.html'"><i class="fas fa-arrow-right"></i></button><h2><i class="fas fa-cog"></i> الإعدادات</h2></div>
<div style="padding:8px 0">
    <div class="setting-item" onclick="window.location.href='profile.html'"><div style="display:flex;align-items:center;gap:12px"><i class="fas fa-user"></i><span>تعديل الملف الشخصي</span></div><i class="fas fa-chevron-left" style="opacity:0.5"></i></div>
    <div class="setting-item"><div style="display:flex;align-items:center;gap:12px"><i class="fas fa-lock"></i><span>الخصوصية</span></div><i class="fas fa-chevron-left" style="opacity:0.5"></i></div>
    <div class="setting-item"><div style="display:flex;align-items:center;gap:12px"><i class="fas fa-globe"></i><span>اللغة</span></div><span style="opacity:0.5;font-size:13px">العربية</span></div>
    <div class="setting-item"><div style="display:flex;align-items:center;gap:12px"><i class="fas fa-info-circle"></i><span>حول التطبيق</span></div><span style="opacity:0.5;font-size:13px">v2026.1 🟣</span></div>
    <button class="btn-danger" onclick="if(confirm('تسجيل الخروج؟')){auth.signOut();window.location.href='auth.html'}"><i class="fas fa-sign-out-alt"></i> تسجيل الخروج</button>
</div>
<script src="firebase-config.js"></script>
<script>if('serviceWorker' in navigator){navigator.serviceWorker.register('/sw.js')}auth.onAuthStateChanged(u=>{if(!u)window.location.href='auth.html'});</script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# 🟣 MAIN
# ═══════════════════════════════════════════════════════════

def main():
    print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║  🟣  VIOLET 2026 - PURPLE GLASS PWA EDITION  🟣      ║
║     Ultimate Generator - 10 Files                        ║
║     PWA + Offline + Service Worker                       ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
    """)
    
    section("BUILDING FILES - إنشاء الملفات")
    
    write("firebase-config.js", build_config())
    write("sw.js", build_sw())
    write("manifest.json", build_manifest())
    write("auth.html", build_auth())
    write("index.html", build_index())
    write("profile.html", build_profile())
    write("upload.html", build_upload())
    write("chat.html", build_chat())
    write("explore.html", build_explore())
    write("notifications.html", build_notifications())
    write("settings.html", build_settings())
    
    print(f"""
{'='*60}
  🟣 BUILD COMPLETE - تم الإنشاء بنجاح! ✨
{'='*60}

  📊 إحصائيات:
     • {TOTAL_LINES} إجمالي عدد الأسطر
     • 10 ملفات تم إنشاؤها

  📁 الملفات:
     1. firebase-config.js   → إعدادات + Offline DB
     2. sw.js                → Service Worker (PWA)
     3. manifest.json        → PWA Manifest
     4. auth.html            → تسجيل دخول
     5. index.html           → الرئيسية + Offline
     6. profile.html         → ملف شخصي
     7. upload.html          → رفع فيديو
     8. chat.html            → دردشة
     9. explore.html         → استكشاف
     10. notifications.html  → إشعارات
     11. settings.html       → إعدادات

  🟣 المميزات الجديدة:
     • 📱 PWA (تثبيت على الشاشة الرئيسية)
     • 📴 Offline Mode كامل
     • 🔄 Service Worker للتخزين المؤقت
     • 💾 IndexedDB للبيانات المحلية
     • 🔔 إشعارات PUSH
     • 🎬 تخزين فيديوهات مؤقتاً
     • 🔄 مزامنة تلقائية عند توفر الإنترنت
     • 🟣 تصميم بنفسجي زجاجي

  🔑 بيانات الاتصال:
     • Firebase: gokp-a0633
     • Cloudinary: dk5kas1gc / gy45_g
     • Admin: jasim28v@gmail.com

  🟣 للتشغيل: python scraper.py
  🟣 VIOLET PWA + OFFLINE READY! ✨
{'='*60}
    """)

if __name__ == "__main__":
    main()
