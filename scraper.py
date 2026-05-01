#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🎵 Spotify Clone Generator - النسخة الكاملة
Cloudinary: so2_mk
Collection: dmla61v7n
"""

import os
from pathlib import Path

# ==================== الإعدادات ====================
CLOUD_NAME = "so2_mk"
COLLECTION_URL = "https://collection.cloudinary.com/dmla61v7n"
GITHUB_USER = "Jasmin28v-cloud"

print(f"""
╔══════════════════════════════════════════════╗
║   🎵 Spotify Clone - النسخة الكاملة       ║
║   ☁️ Cloudinary: {CLOUD_NAME}                    ║
║   📎 Collection: dmla61v7n                  ║
╚══════════════════════════════════════════════╝
""")

# ==================== إنشاء المجلدات ====================
print("📁 إنشاء المجلدات...")
folders = [
    ".github/workflows",
    "static/css",
    "static/js",
    "static/images",
    "static/fonts",
    "templates",
    "scripts",
    "data"
]
for folder in folders:
    Path(folder).mkdir(parents=True, exist_ok=True)
    print(f"  ✅ {folder}")

# ==================== GitHub Actions ====================
print("\n⚙️  إنشاء .github/workflows/main.yml...")

main_yml = f"""name: 🎵 Deploy Spotify Clone

on:
  push:
    branches: [ main, master ]
  workflow_dispatch:

permissions:
  contents: write
  pages: write
  id-token: write

env:
  CLOUD_NAME: {CLOUD_NAME}
  COLLECTION_URL: {COLLECTION_URL}

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{{{ steps.deployment.outputs.page_url }}}}
    
    steps:
    - uses: actions/checkout@v4
    
    - uses: actions/configure-pages@v4
    
    - name: 🐍 Setup Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.10'
    
    - name: 🎵 Build Site
      run: |
        echo "🎵 Building Spotify Clone..."
        echo "☁️ Cloudinary: ${{{{ env.CLOUD_NAME }}}}"
        echo "📎 Collection: ${{{{ env.COLLECTION_URL }}}}"
        python scraper.py
        echo ""
        echo "📁 Created files:"
        ls -la static/
    
    - uses: actions/upload-pages-artifact@v3
      with:
        path: './static'
    
    - name: 🚀 Deploy
      id: deployment
      uses: actions/deploy-pages@v4
    
    - name: 🎉 Success
      run: echo "🎉 https://${{{{ github.repository_owner }}}}.github.io/${{{{ github.event.repository.name }}}}/"
"""

with open('.github/workflows/main.yml', 'w', encoding='utf-8') as f:
    f.write(main_yml)
print("  ✅ main.yml created")

# ==================== static/index.html - واجهة Spotify كاملة ====================
print("\n🎨 إنشاء static/index.html - واجهة Spotify الاحترافية...")

index_html = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🎵 Spotify - Web Player: Music for everyone</title>
    <link rel="stylesheet" href="css/style.css">
    <link rel="icon" href="https://open.spotifycdn.com/cdn/images/favicon32.b64ecc03.png">
</head>
<body>
    <!-- ========== SIDEBAR ========== -->
    <aside class="sidebar">
        <div class="sidebar-logo">
            <svg class="spotify-logo" viewBox="0 0 24 24" width="40" height="40">
                <path fill="#1db954" d="M12 0C5.4 0 0 5.4 0 12s5.4 12 12 12 12-5.4 12-12S18.66 0 12 0zm5.521 17.34c-.24.359-.66.48-1.021.24-2.82-1.74-6.36-2.101-10.561-1.141-.418.122-.779-.179-.899-.539-.12-.421.18-.78.54-.9 4.56-1.021 8.52-.6 11.64 1.32.42.18.479.659.301 1.02zm1.44-3.3c-.301.42-.841.6-1.262.3-3.239-1.98-8.159-2.58-11.939-1.38-.479.12-1.02-.12-1.14-.6-.12-.48.12-1.021.6-1.141C9.6 9.9 15 10.561 18.72 12.84c.361.181.54.78.241 1.2zm.12-3.36C15.24 8.4 8.82 8.16 5.16 9.301c-.6.179-1.2-.181-1.38-.721-.18-.601.18-1.2.72-1.381 4.26-1.26 11.28-1.02 15.721 1.621.539.3.719 1.02.419 1.56-.299.421-1.02.599-1.559.3z"/>
            </svg>
            <span class="logo-text">Spotify</span>
        </div>
        <nav class="sidebar-nav">
            <ul class="nav-list">
                <li class="nav-item active">
                    <span class="nav-icon">🏠</span>
                    <span>الرئيسية</span>
                </li>
                <li class="nav-item">
                    <span class="nav-icon">🔍</span>
                    <span>بحث</span>
                </li>
                <li class="nav-item">
                    <span class="nav-icon">📚</span>
                    <span>مكتبتك</span>
                </li>
            </ul>
        </nav>
        <div class="sidebar-section">
            <div class="playlist-list">
                <a href="#" class="playlist-link">🎧 Chill Vibes</a>
                <a href="#" class="playlist-link">🔥 Today's Top Hits</a>
                <a href="#" class="playlist-link">💪 Workout Energy</a>
                <a href="#" class="playlist-link">🌟 Arabic Hits 2024</a>
                <a href="#" class="playlist-link">🎸 Rock Classics</a>
                <a href="#" class="playlist-link">🎤 RapCaviar</a>
                <a href="#" class="playlist-link">🌙 Sleep Sounds</a>
                <a href="#" class="playlist-link">🎹 Piano Peace</a>
            </div>
        </div>
        <div class="sidebar-cloudinary">
            <div class="cloudinary-badge-sidebar">
                <span class="cloud-icon">☁️</span>
                <span class="cloud-name">{CLOUD_NAME}</span>
            </div>
            <a href="{COLLECTION_URL}" target="_blank" class="cloudinary-link">
                📎 Collection: dmla61v7n
            </a>
        </div>
    </aside>

    <!-- ========== MAIN CONTENT ========== -->
    <main class="main-content">
        <header class="top-header">
            <h1 class="greeting-title"><span id="greetingText">مساء الخير</span> 👋</h1>
        </header>
        <div class="content">
            <section class="featured-section">
                <h2 class="section-title">🎵 استمع مجدداً</h2>
                <div class="featured-grid">
                    <div class="featured-card" style="background: linear-gradient(135deg, #006450, #1db954);">
                        <div class="featured-text"><h3>Liked Songs</h3><p>432 أغنية مفضلة</p></div>
                        <div class="featured-icon">❤️</div>
                    </div>
                    <div class="featured-card" style="background: linear-gradient(135deg, #1e3264, #608de2);">
                        <div class="featured-text"><h3>Daily Mix 1</h3><p>موسيقى هادئة ومنوعة</p></div>
                        <div class="featured-icon">🎧</div>
                    </div>
                    <div class="featured-card" style="background: linear-gradient(135deg, #8400e7, #b300b3);">
                        <div class="featured-text"><h3>Discover Weekly</h3><p>اكتشف أغاني جديدة</p></div>
                        <div class="featured-icon">🔍</div>
                    </div>
                    <div class="featured-card" style="background: linear-gradient(135deg, #503750, #8c1932);">
                        <div class="featured-text"><h3>Release Radar</h3><p>أحدث الإصدارات</p></div>
                        <div class="featured-icon">🆕</div>
                    </div>
                </div>
            </section>
            <footer class="site-footer"><p>© 2024 Spotify Clone | ☁️ {CLOUD_NAME}</p></footer>
        </div>
    </main>

    <!-- ========== PLAYER BAR ========== -->
    <footer class="player-bar">
        <div class="now-playing">
            <span>🎵 Now Playing: Blinding Lights - The Weeknd</span>
        </div>
    </footer>
    <script src="js/app.js"></script>
</body>
</html>"""

with open('static/index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)
print("  ✅ static/index.html created")

# ==================== static/css/style.css ====================
print("\n🎨 إنشاء static/css/style.css...")

style_css = """* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background: #000;
    color: #fff;
    display: flex;
    height: 100vh;
    overflow: hidden;
}
.sidebar {
    width: 280px;
    background: #000;
    padding: 24px 12px;
    display: flex;
    flex-direction: column;
    gap: 24px;
}
.sidebar-logo {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 0 12px;
}
.logo-text {
    font-size: 24px;
    font-weight: 700;
}
.nav-item {
    display: flex;
    align-items: center;
    gap: 16px;
    padding: 8px 12px;
    border-radius: 4px;
    cursor: pointer;
    color: #b3b3b3;
    font-weight: 600;
}
.nav-item:hover, .nav-item.active {
    color: #fff;
    background: rgba(255,255,255,0.1);
}
.playlist-link {
    display: block;
    padding: 8px 12px;
    color: #b3b3b3;
    text-decoration: none;
    font-size: 14px;
}
.playlist-link:hover {
    color: #fff;
}
.cloudinary-badge-sidebar {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 8px 12px;
    background: linear-gradient(135deg, #3b82f6, #1e40af);
    border-radius: 6px;
    font-weight: 600;
}
.cloudinary-link {
    display: block;
    margin-top: 8px;
    font-size: 12px;
    color: #b3b3b3;
    padding: 4px 12px;
}
.main-content {
    flex: 1;
    background: #121212;
    overflow-y: auto;
}
.top-header {
    padding: 16px 32px;
    background: rgba(0,0,0,0.8);
    backdrop-filter: blur(10px);
    position: sticky;
    top: 0;
    z-index: 50;
}
.greeting-title {
    font-size: 32px;
    font-weight: 700;
}
.content {
    padding: 24px 32px;
}
.section-title {
    font-size: 24px;
    font-weight: 700;
    margin-bottom: 20px;
}
.featured-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 12px;
}
.featured-card {
    height: 80px;
    border-radius: 6px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 16px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
}
.featured-icon {
    font-size: 48px;
    opacity: 0.3;
    position: absolute;
    left: -8px;
    bottom: -8px;
    transform: rotate(15deg);
}
.player-bar {
    position: fixed;
    bottom: 0;
    width: 100%;
    height: 90px;
    background: #181818;
    border-top: 1px solid #282828;
    display: flex;
    align-items: center;
    padding: 0 16px;
    z-index: 200;
}
.site-footer {
    margin-top: 40px;
    padding: 20px 0;
    color: #b3b3b3;
    font-size: 14px;
}
"""

with open('static/css/style.css', 'w', encoding='utf-8') as f:
    f.write(style_css)
print("  ✅ static/css/style.css created")

# ==================== static/js/app.js ====================
print("\n⚡ إنشاء static/js/app.js...")

app_js = f"""// Spotify Clone - Cloudinary: {CLOUD_NAME}

function updateGreeting() {{
    const hour = new Date().getHours();
    const el = document.getElementById('greetingText');
    if (!el) return;
    if (hour < 12) el.textContent = 'صباح الخير';
    else if (hour < 18) el.textContent = 'مساء الخير';
    else el.textContent = 'مساء الخير';
}}

document.addEventListener('DOMContentLoaded', () => {{
    updateGreeting();
    console.log('🎵 Spotify Clone Ready!');
    console.log('☁️ Cloudinary: {CLOUD_NAME}');
}});
"""

with open('static/js/app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)
print("  ✅ static/js/app.js created")

# ==================== ملفات إضافية ====================
Path('scripts/__init__.py').write_text('')
Path('templates/.gitkeep').write_text('')
Path('requirements.txt').write_text('flask==2.3.0\ncloudinary==1.36.0\n')
Path('README.md').write_text(f'# 🎵 Spotify Clone\n\n☁️ Cloudinary: {CLOUD_NAME}\n📎 Collection: {COLLECTION_URL}\n')

# ==================== Done ====================
print("\n" + "="*50)
print(" ✅ Spotify Clone Generated Successfully!")
print(f" ☁️ Cloudinary: {CLOUD_NAME}")
print(f" 📎 Collection: {COLLECTION_URL}")
print("="*50)
print("\n📂 Files created:")
for folder in ['static', 'templates', 'scripts', '.github']:
    for root, dirs, files in os.walk(folder):
        for file in files:
            print(f"   ✅ {root}/{file}")
