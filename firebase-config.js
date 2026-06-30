// 🟣 VIOLET 2026 - Purple Glass Configuration
// Firebase: gokp-a0633 | Cloudinary: dk5kas1gc
// ✨ PREMIUM: PWA + Offline + Auto Sync

const firebaseConfig = {
    apiKey: "AIzaSyC7Bfcp9JgBQMwasEeuLlZVzM58R0l1CXE",
    authDomain: "gokp-a0633.firebaseapp.com",
    databaseURL: "https://gokp-a0633-default-rtdb.firebaseio.com",
    projectId: "gokp-a0633",
    storageBucket: "gokp-a0633.firebasestorage.app",
    messagingSenderId: "794248779449",
    appId: "1:794248779449:web:c78564c0d126c01cafed68",
    measurementId: "G-PW6B2R0F6H"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();
const db = firebase.database();

// Cloudinary Configuration
const CLOUD_NAME = "dk5kas1gc";
const UPLOAD_PRESET = "gy45_g";

// 🟣 VIOLET Settings
const ADMIN_EMAILS = ['jasim28v@gmail.com'];
const DICEBEAR_URL = "https://api.dicebear.com/7.x/big-smile/svg";
const COVER_COLORS = [
    "linear-gradient(135deg, #4c1d95, #6d28d9, #7c3aed)",
    "linear-gradient(135deg, #3b0764, #4c1d95, #6d28d9)",
    "linear-gradient(135deg, #2e1065, #3b0764, #4c1d95)",
    "linear-gradient(135deg, #8b5cf6, #7c3aed, #6d28d9)",
    "linear-gradient(135deg, #a855f7, #8b5cf6, #7c3aed)",
    "linear-gradient(135deg, #0a0812, #1a1030, #8b5cf6)"
];

// 🟣 App Info
const APP_NAME = "VIOLET";
const APP_VERSION = "2026.1";
const PRIMARY_COLOR = "#7c3aed";
const SECONDARY_COLOR = "#a855f7";

// 💾 Offline Storage - IndexedDB
const offlineDB = indexedDB.open('VIOLET_Offline', 1);
offlineDB.onupgradeneeded = function(event) {
    const db = event.target.result;
    if (!db.objectStoreNames.contains('videos')) {
        db.createObjectStore('videos', { keyPath: 'id' });
    }
    if (!db.objectStoreNames.contains('users')) {
        db.createObjectStore('users', { keyPath: 'uid' });
    }
    if (!db.objectStoreNames.contains('pendingLikes')) {
        db.createObjectStore('pendingLikes', { keyPath: 'videoId', autoIncrement: false });
    }
};

// 🌐 Network Detection
let isOnline = navigator.onLine;
window.addEventListener('online', () => { isOnline = true; syncPendingActions(); });
window.addEventListener('offline', () => { isOnline = false; });

// 🔄 Sync pending actions when online
async function syncPendingActions() {
    if (!auth.currentUser) return;
    const db_ = await new Promise((resolve, reject) => {
        const request = indexedDB.open('VIOLET_Offline', 1);
        request.onsuccess = (event) => resolve(event.target.result);
        request.onerror = (event) => reject(event.target.error);
    });
    
    const tx = db_.transaction(['pendingLikes'], 'readwrite');
    const store = tx.objectStore('pendingLikes');
    const allPending = await new Promise((resolve) => {
        const request = store.getAll();
        request.onsuccess = () => resolve(request.result);
    });
    
    for (const pending of allPending) {
        try {
            const ref = db.ref('videos/' + pending.videoId);
            const snap = await ref.get();
            const video = snap.val();
            if (video) {
                let likes = video.likes || 0;
                let likedBy = video.likedBy || {};
                if (!likedBy[auth.currentUser.uid]) {
                    likes++;
                    likedBy[auth.currentUser.uid] = true;
                    await ref.update({ likes, likedBy });
                }
            }
            store.delete(pending.videoId);
        } catch(e) { console.error('Sync failed:', e); }
    }
}

console.log('🟣 %c'+APP_NAME+' v'+APP_VERSION+' Ready ✨ | PWA + Offline', 'color: #7c3aed; font-size: 16px; font-weight: bold;');
