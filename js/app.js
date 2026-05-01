// Spotify Clone - Cloudinary: so2_mk

function updateGreeting() {
    const hour = new Date().getHours();
    const el = document.getElementById('greetingText');
    if (!el) return;
    if (hour < 12) el.textContent = 'صباح الخير';
    else if (hour < 18) el.textContent = 'مساء الخير';
    else el.textContent = 'مساء الخير';
}

document.addEventListener('DOMContentLoaded', () => {
    updateGreeting();
    console.log('🎵 Spotify Clone Ready!');
    console.log('☁️ Cloudinary: so2_mk');
});
