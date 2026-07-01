// 🟢 GREEN 2026 - Emerald Glass Configuration
// Firebase: gokp-a0633 | Cloudinary: dk5kas1gc
// ✨ PREMIUM: Notifications + Compact Grid + Delete Videos

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

firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();
const db = firebase.database();

const CLOUD_NAME = "dk5kas1gc";
const UPLOAD_PRESET = "gy45_g";
const ADMIN_EMAILS = ['jasim28v@gmail.com'];
const DICEBEAR_URL = "https://api.dicebear.com/7.x/big-smile/svg";
const COVER_COLORS = [
    "linear-gradient(135deg, #064e3b, #065f46, #059669)",
    "linear-gradient(135deg, #022c22, #064e3b, #065f46)",
    "linear-gradient(135deg, #047857, #059669, #10b981)",
    "linear-gradient(135deg, #34d399, #10b981, #059669)",
    "linear-gradient(135deg, #6ee7b7, #34d399, #10b981)",
    "linear-gradient(135deg, #0a0f0b, #0a1a15, #10b981)"
];
const APP_NAME = "GREEN";
const APP_VERSION = "2026.1";
const PRIMARY_COLOR = "#059669";
const SECONDARY_COLOR = "#10b981";

console.log('🟢 %c'+APP_NAME+' v'+APP_VERSION+' Ready ✨', 'color: #059669; font-size: 16px; font-weight: bold;');
