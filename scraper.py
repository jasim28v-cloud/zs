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
    
    - name: Build Site
      run: |
        echo "🎵 Building Spotify Clone..."
        echo "☁️ Cloudinary: ${{{{ env.CLOUD_NAME }}}}"
        echo "📎 Collection: ${{{{ env.COLLECTION_URL }}}}"
        mkdir -p static
        cp -r templates/* static/ 2>/dev/null || true
        ls -la static/
    
    - uses: actions/upload-pages-artifact@v3
      with:
        path: './static'
    
    - name: Deploy
      id: deployment
      uses: actions/deploy-pages@v4
    
    - name: Success
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
        <!-- Logo -->
        <div class="sidebar-logo">
            <svg class="spotify-logo" viewBox="0 0 24 24" width="40" height="40">
                <path fill="#1db954" d="M12 0C5.4 0 0 5.4 0 12s5.4 12 12 12 12-5.4 12-12S18.66 0 12 0zm5.521 17.34c-.24.359-.66.48-1.021.24-2.82-1.74-6.36-2.101-10.561-1.141-.418.122-.779-.179-.899-.539-.12-.421.18-.78.54-.9 4.56-1.021 8.52-.6 11.64 1.32.42.18.479.659.301 1.02zm1.44-3.3c-.301.42-.841.6-1.262.3-3.239-1.98-8.159-2.58-11.939-1.38-.479.12-1.02-.12-1.14-.6-.12-.48.12-1.021.6-1.141C9.6 9.9 15 10.561 18.72 12.84c.361.181.54.78.241 1.2zm.12-3.36C15.24 8.4 8.82 8.16 5.16 9.301c-.6.179-1.2-.181-1.38-.721-.18-.601.18-1.2.72-1.381 4.26-1.26 11.28-1.02 15.721 1.621.539.3.719 1.02.419 1.56-.299.421-1.02.599-1.559.3z"/>
            </svg>
            <span class="logo-text">Spotify</span>
        </div>

        <!-- Navigation -->
        <nav class="sidebar-nav">
            <ul class="nav-list">
                <li class="nav-item active">
                    <svg class="nav-icon" viewBox="0 0 24 24"><path fill="currentColor" d="M13.5 1.515a3 3 0 0 0-3 0L3 5.845a2 2 0 0 0-1 1.732V21a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1v-6h4v6a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V7.577a2 2 0 0 0-1-1.732l-7.5-4.33z"/></svg>
                    <span>الرئيسية</span>
                </li>
                <li class="nav-item">
                    <svg class="nav-icon" viewBox="0 0 24 24"><path fill="currentColor" d="M10.533 1.279c-5.18 0-9.407 4.14-9.407 9.279s4.226 9.279 9.407 9.279c2.234 0 4.29-.77 5.907-2.058l4.353 4.353a1 1 0 1 0 1.414-1.414l-4.344-4.344a9.157 9.157 0 0 0 2.077-5.816c0-5.14-4.226-9.28-9.407-9.28zm0 2c4.132 0 7.407 3.28 7.407 7.279s-3.275 7.279-7.407 7.279-7.407-3.28-7.407-7.279S6.4 3.28 10.533 3.28z"/></svg>
                    <span>بحث</span>
                </li>
                <li class="nav-item">
                    <svg class="nav-icon" viewBox="0 0 24 24"><path fill="currentColor" d="M14.5 2.134a1 1 0 0 1 1 0l6 3.464a1 1 0 0 1 .5.866V21a1 1 0 0 1-1 1h-6a1 1 0 0 1-1-1V3a1 1 0 0 1 .5-.866zM16 4.732V20h4V7.041l-4-2.309zM3 22a1 1 0 0 1-1-1V3a1 1 0 0 1 2 0v18a1 1 0 0 1-1 1zm6 0a1 1 0 0 1-1-1V3a1 1 0 0 1 2 0v18a1 1 0 0 1-1 1z"/></svg>
                    <span>مكتبتك</span>
                </li>
            </ul>
        </nav>

        <!-- Playlists Section -->
        <div class="sidebar-section">
            <div class="sidebar-actions">
                <button class="btn-create-playlist" title="إنشاء قائمة تشغيل">
                    <svg viewBox="0 0 24 24" width="20" height="20"><path fill="currentColor" d="M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18zm-1 5h2v3h3v2h-3v3h-2v-3H8v-2h3V8z"/></svg>
                    <span>إنشاء قائمة تشغيل</span>
                </button>
                <button class="btn-liked-songs" title="الأغاني المفضلة">
                    <svg viewBox="0 0 24 24" width="20" height="20"><path fill="currentColor" d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>
                    <span>الأغاني المفضلة</span>
                </button>
            </div>
            <div class="sidebar-divider"></div>
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

        <!-- Cloudinary Section -->
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
        <!-- Top Header -->
        <header class="top-header">
            <div class="header-nav">
                <button class="nav-btn prev-btn" title="رجوع">
                    <svg viewBox="0 0 24 24" width="24" height="24"><path fill="currentColor" d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"/></svg>
                </button>
                <button class="nav-btn next-btn" title="التالي">
                    <svg viewBox="0 0 24 24" width="24" height="24"><path fill="currentColor" d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg>
                </button>
            </div>
            <div class="header-actions">
                <a href="{COLLECTION_URL}" target="_blank" class="btn-cloudinary-header">
                    ☁️ Cloudinary
                </a>
                <button class="btn-premium">استكشف Premium</button>
                <button class="btn-install">تثبيت التطبيق</button>
                <div class="user-avatar">
                    <img src="https://i.pravatar.cc/40?img=68" alt="User" class="avatar-img">
                    <span>مستخدم</span>
                    <svg viewBox="0 0 24 24" width="16" height="16"><path fill="currentColor" d="M7 10l5 5 5-5z"/></svg>
                </div>
            </div>
        </header>

        <!-- Content -->
        <div class="content">
            <!-- Greeting Section -->
            <section class="greeting-section">
                <h1 class="greeting-title">
                    <span id="greetingText">مساء الخير</span> 👋
                </h1>
            </section>

            <!-- Featured Grid -->
            <section class="featured-section">
                <h2 class="section-title">🎵 استمع مجدداً</h2>
                <div class="featured-grid">
                    <div class="featured-card" style="background: linear-gradient(135deg, #006450, #1db954);">
                        <div class="featured-text">
                            <h3>Liked Songs</h3>
                            <p>432 أغنية مفضلة</p>
                        </div>
                        <div class="featured-icon">❤️</div>
                    </div>
                    <div class="featured-card" style="background: linear-gradient(135deg, #1e3264, #608de2);">
                        <div class="featured-text">
                            <h3>Daily Mix 1</h3>
                            <p>موسيقى هادئة ومنوعة</p>
                        </div>
                        <div class="featured-icon">🎧</div>
                    </div>
                    <div class="featured-card" style="background: linear-gradient(135deg, #8400e7, #b300b3);">
                        <div class="featured-text">
                            <h3>Discover Weekly</h3>
                            <p>اكتشف أغاني جديدة</p>
                        </div>
                        <div class="featured-icon">🔍</div>
                    </div>
                    <div class="featured-card" style="background: linear-gradient(135deg, #503750, #8c1932);">
                        <div class="featured-text">
                            <h3>Release Radar</h3>
                            <p>أحدث الإصدارات</p>
                        </div>
                        <div class="featured-icon">🆕</div>
                    </div>
                    <div class="featured-card" style="background: linear-gradient(135deg, #283048, #859398);">
                        <div class="featured-text">
                            <h3>Chill Lofi</h3>
                            <p>هادئ ومنعش</p>
                        </div>
                        <div class="featured-icon">🌊</div>
                    </div>
                    <div class="featured-card" style="background: linear-gradient(135deg, #ff6b6b, #ee5a24);">
                        <div class="featured-text">
                            <h3>Energy Boost</h3>
                            <p>طاقة وحماس</p>
                        </div>
                        <div class="featured-icon">⚡</div>
                    </div>
                </div>
            </section>

            <!-- Playlists Grid -->
            <section class="playlists-section">
                <div class="section-header">
                    <h2 class="section-title">🔥 قوائم التشغيل المميزة</h2>
                    <a href="#" class="show-all">عرض الكل</a>
                </div>
                <div class="playlists-grid">
                    <!-- Card 1 -->
                    <div class="playlist-card">
                        <div class="card-image" style="background: linear-gradient(135deg, #f093fb, #f5576c);">
                            <button class="play-overlay">
                                <svg viewBox="0 0 24 24" width="24" height="24"><path fill="white" d="M8 5v14l11-7z"/></svg>
                            </button>
                        </div>
                        <h3 class="card-title">Today's Top Hits</h3>
                        <p class="card-desc">Taylor Swift, The Weeknd, Billie Eilish والمزيد</p>
                    </div>

                    <!-- Card 2 -->
                    <div class="playlist-card">
                        <div class="card-image" style="background: linear-gradient(135deg, #a8edea, #fed6e3);">
                            <button class="play-overlay">
                                <svg viewBox="0 0 24 24" width="24" height="24"><path fill="white" d="M8 5v14l11-7z"/></svg>
                            </button>
                        </div>
                        <h3 class="card-title">RapCaviar</h3>
                        <p class="card-desc">Drake, Kendrick Lamar, Travis Scott</p>
                    </div>

                    <!-- Card 3 -->
                    <div class="playlist-card">
                        <div class="card-image" style="background: linear-gradient(135deg, #667eea, #764ba2);">
                            <button class="play-overlay">
                                <svg viewBox="0 0 24 24" width="24" height="24"><path fill="white" d="M8 5v14l11-7z"/></svg>
                            </button>
                        </div>
                        <h3 class="card-title">Arabic Hits 2024</h3>
                        <p class="card-desc">عمرو دياب، إليسا، نانسي عجرم</p>
                    </div>

                    <!-- Card 4 -->
                    <div class="playlist-card">
                        <div class="card-image" style="background: linear-gradient(135deg, #ffecd2, #fcb69f);">
                            <button class="play-overlay">
                                <svg viewBox="0 0 24 24" width="24" height="24"><path fill="white" d="M8 5v14l11-7z"/></svg>
                            </button>
                        </div>
                        <h3 class="card-title">Chill Vibes</h3>
                        <p class="card-desc">استرخِ مع أفضل الأغاني الهادئة</p>
                    </div>

                    <!-- Card 5 -->
                    <div class="playlist-card">
                        <div class="card-image" style="background: linear-gradient(135deg, #4facfe, #00f2fe);">
                            <button class="play-overlay">
                                <svg viewBox="0 0 24 24" width="24" height="24"><path fill="white" d="M8 5v14l11-7z"/></svg>
                            </button>
                        </div>
                        <h3 class="card-title">Workout Energy</h3>
                        <p class="card-desc">طاقة وحماس للتمارين الرياضية</p>
                    </div>

                    <!-- Card 6 -->
                    <div class="playlist-card">
                        <div class="card-image" style="background: linear-gradient(135deg, #fa709a, #fee140);">
                            <button class="play-overlay">
                                <svg viewBox="0 0 24 24" width="24" height="24"><path fill="white" d="M8 5v14l11-7z"/></svg>
                            </button>
                        </div>
                        <h3 class="card-title">Rock Classics</h3>
                        <p class="card-desc">Queen, Led Zeppelin, AC/DC</p>
                    </div>
                </div>
            </section>

            <!-- Cloudinary Section -->
            <section class="cloudinary-section">
                <h2 class="section-title">☁️ التكامل السحابي</h2>
                <div class="cloudinary-card-main">
                    <div class="cloudinary-card-left">
                        <h3>{CLOUD_NAME}</h3>
                        <p>Cloudinary Collection</p>
                        <a href="{COLLECTION_URL}" target="_blank" class="btn-view-collection">
                            عرض المجموعة <span>→</span>
                        </a>
                    </div>
                    <div class="cloudinary-card-right">
                        <div class="cloudinary-stats">
                            <div class="stat-item">
                                <span class="stat-number">☁️</span>
                                <span class="stat-label">Cloud</span>
                            </div>
                            <div class="stat-item">
                                <span class="stat-number">📁</span>
                                <span class="stat-label">Collection</span>
                            </div>
                            <div class="stat-item">
                                <span class="stat-number">✅</span>
                                <span class="stat-label">Connected</span>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- Footer -->
            <footer class="site-footer">
                <div class="footer-links">
                    <div class="footer-column">
                        <h4>الشركة</h4>
                        <a href="#">حول</a>
                        <a href="#">وظائف</a>
                        <a href="#">For the Record</a>
                    </div>
                    <div class="footer-column">
                        <h4>المجتمعات</h4>
                        <a href="#">للفنانين</a>
                        <a href="#">للمطورين</a>
                        <a href="#">الإعلانات</a>
                    </div>
                    <div class="footer-column">
                        <h4>روابط مفيدة</h4>
                        <a href="#">الدعم</a>
                        <a href="#">تطبيق الجوال</a>
                        <a href="#">مشغل الويب</a>
                    </div>
                    <div class="footer-column">
                        <h4>Cloudinary</h4>
                        <a href="{COLLECTION_URL}" target="_blank">Collection</a>
                        <a href="#">Upload Files</a>
                        <a href="#">Dashboard</a>
                    </div>
                </div>
                <div class="footer-bottom">
                    <p>© 2024 Spotify Clone | ☁️ {CLOUD_NAME}</p>
                </div>
            </footer>
        </div>
    </main>

    <!-- ========== PLAYER BAR ========== -->
    <footer class="player-bar">
        <!-- Now Playing -->
        <div class="now-playing">
            <div class="now-playing-cover">
                <img src="https://i.pravatar.cc/56?img=3" alt="Cover" class="cover-image">
            </div>
            <div class="now-playing-info">
                <span class="track-name">Blinding Lights</span>
                <span class="track-artist">The Weeknd</span>
            </div>
            <button class="like-btn" title="إضافة للمفضلة">
                <svg viewBox="0 0 24 24" width="18" height="18"><path fill="currentColor" d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>
            </button>
        </div>

        <!-- Player Controls -->
        <div class="player-controls">
            <div class="controls-buttons">
                <button class="control-btn" title="عشوائي">
                    <svg viewBox="0 0 24 24" width="16" height="16"><path fill="currentColor" d="M18.788 3.702a1 1 0 0 1 1.41-.128L22.293 5.5l-2.094 1.926a1 1 0 0 1-1.282-1.534l.707-.591H17a8 8 0 0 0-7.747 6.05 6 6 0 0 1-5.81 4.349H2v2h1.443a8 8 0 0 0 7.747-6.05 6 6 0 0 1 5.81-4.349h1.885l-.707-.591a1 1 0 0 1-.39-.812zm-9.532 8.369L5.5 8.5 3.406 10.427l3.756 3.571a1 1 0 0 1-1.282 1.534l-.707-.591A6 6 0 0 0 5 15.3v.4h2v-.4a8 8 0 0 1 2.256-5.23zM20 8.3v-.4h-2v.4a6 6 0 0 1-2.256 5.23l-1.21 1.15a1 1 0 0 0 1.373 1.454l1.21-1.15A8 8 0 0 0 20 8.3z"/></svg>
                </button>
                <button class="control-btn" title="السابق">
                    <svg viewBox="0 0 24 24" width="16" height="16"><path fill="currentColor" d="M6 6h2v12H6zm3.5 6l8.5 6V6z"/></svg>
                </button>
                <button class="play-btn-big" title="تشغيل">
                    <svg viewBox="0 0 24 24" width="24" height="24"><path fill="black" d="M8 5v14l11-7z"/></svg>
                </button>
                <button class="control-btn" title="التالي">
                    <svg viewBox="0 0 24 24" width="16" height="16"><path fill="currentColor" d="M6 18l8.5-6L6 6v12zM16 6v12h2V6h-2z"/></svg>
                </button>
                <button class="control-btn" title="تكرار">
                    <svg viewBox="0 0 24 24" width="16" height="16"><path fill="currentColor" d="M7 7h10v3l4-4-4-4v3H5v6h2V7zm10 10H7v-3l-4 4 4 4v-3h12v-6h-2v4z"/></svg>
                </button>
            </div>

            <!-- Progress Bar -->
            <div class="progress-container">
                <span class="time">1:23</span>
                <div class="progress-bar-bg">
                    <div class="progress-bar-fill" style="width: 35%;"></div>
                    <div class="progress-thumb" style="left: 35%;"></div>
                </div>
                <span class="time">3:30</span>
            </div>
        </div>

        <!-- Volume Controls -->
        <div class="volume-controls">
            <button class="control-btn" title="قائمة الانتظار">
                <svg viewBox="0 0 24 24" width="16" height="16"><path fill="currentColor" d="M15 6H3v2h12V6zm0 4H3v2h12v-2zM3 16h8v-2H3v2zM17 6v8.18c-.31-.11-.65-.18-1-.18-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3V8h3V6h-5z"/></svg>
            </button>
            <button class="control-btn" title="الجهاز المتصل">
                <svg viewBox="0 0 24 24" width="16" height="16"><path fill="currentColor" d="M2.5 3.5h19v2h-19v-2zm0 5h19v2h-19v-2zm0 5h19v2h-19v-2zm0 5h19v2h-19v-2z"/></svg>
            </button>
            <button class="control-btn volume-btn" title="كتم الصوت">
                <svg viewBox="0 0 24 24" width="16" height="16"><path fill="currentColor" d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/></svg>
            </button>
            <div class="volume-bar-bg">
                <div class="volume-bar-fill" style="width: 70%;"></div>
            </div>
        </div>
    </footer>

    <script src="js/app.js"></script>
</body>
</html>"""

with open('static/index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)
print("  ✅ static/index.html created (Spotify interface)")

# ==================== static/css/style.css ====================
print("\n🎨 إنشاء static/css/style.css...")

style_css = """/* ========== Spotify Clone Styles ========== */
:root {
    --bg-base: #000000;
    --bg-elevated: #121212;
    --bg-highlight: #1a1a1a;
    --bg-card: #181818;
    --bg-card-hover: #282828;
    --text-primary: #ffffff;
    --text-secondary: #b3b3b3;
    --text-tertiary: #727272;
    --spotify-green: #1db954;
    --spotify-green-hover: #1ed760;
    --sidebar-width: 280px;
    --player-height: 90px;
    --header-height: 64px;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
    background: var(--bg-base);
    color: var(--text-primary);
    overflow: hidden;
    height: 100vh;
    display: flex;
    flex-direction: column;
}

a {
    text-decoration: none;
    color: inherit;
}

/* ========== SIDEBAR ========== */
.sidebar {
    width: var(--sidebar-width);
    height: calc(100vh - var(--player-height));
    background: var(--bg-base);
    position: fixed;
    top: 0;
    right: 0;
    z-index: 100;
    display: flex;
    flex-direction: column;
    padding: 24px 12px 8px;
    overflow-y: auto;
}

.sidebar-logo {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 0 12px 18px;
    margin-bottom: 8px;
}

.logo-text {
    font-size: 24px;
    font-weight: 700;
    color: var(--text-primary);
}

/* Navigation */
.sidebar-nav {
    padding: 0 8px;
}

.nav-list {
    list-style: none;
}

.nav-item {
    display: flex;
    align-items: center;
    gap: 16px;
    padding: 8px 12px;
    border-radius: 4px;
    cursor: pointer;
    transition: all 0.2s;
    color: var(--text-secondary);
    font-weight: 600;
    font-size: 15px;
}

.nav-item:hover {
    color: var(--text-primary);
}

.nav-item.active {
    color: var(--text-primary);
    background: rgba(255, 255, 255, 0.1);
}

.nav-icon {
    width: 24px;
    height: 24px;
    flex-shrink: 0;
}

/* Sidebar Sections */
.sidebar-section {
    margin-top: 24px;
}

.sidebar-actions {
    padding: 0 8px;
    display: flex;
    flex-direction: column;
    gap: 4px;
}

.btn-create-playlist,
.btn-liked-songs {
    display: flex;
    align-items: center;
    gap: 16px;
    padding: 8px 12px;
    background: none;
    border: none;
    color: var(--text-secondary);
    cursor: pointer;
    font-size: 15px;
    font-weight: 600;
    transition: color 0.2s;
    width: 100%;
    text-align: right;
}

.btn-create-playlist:hover,
.btn-liked-songs:hover {
    color: var(--text-primary);
}

.sidebar-divider {
    height: 1px;
    background: rgba(255, 255, 255, 0.1);
    margin: 12px 12px;
}

.playlist-list {
    padding: 0 8px;
    display: flex;
    flex-direction: column;
    gap: 2px;
}

.playlist-link {
    padding: 8px 12px;
    font-size: 14px;
    color: var(--text-secondary);
    border-radius: 4px;
    transition: all 0.2s;
    cursor: pointer;
}

.playlist-link:hover {
    color: var(--text-primary);
}

/* Cloudinary in Sidebar */
.sidebar-cloudinary {
    margin-top: auto;
    padding: 16px 12px;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.cloudinary-badge-sidebar {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 8px 12px;
    background: linear-gradient(135deg, #3b82f6, #1e40af);
    border-radius: 6px;
    font-size: 14px;
    font-weight: 600;
}

.cloud-icon {
    font-size: 18px;
}

.cloudinary-link {
    display: block;
    margin-top: 8px;
    font-size: 12px;
    color: var(--text-secondary);
    padding: 4px 12px;
}

.cloudinary-link:hover {
    color: var(--text-primary);
}

/* ========== MAIN CONTENT ========== */
.main-content {
    margin-right: var(--sidebar-width);
    height: calc(100vh - var(--player-height));
    overflow-y: auto;
    background: var(--bg-elevated);
    position: relative;
}

/* Header */
.top-header {
    position: sticky;
    top: 0;
    z-index: 50;
    background: rgba(0, 0, 0, 0.8);
    backdrop-filter: blur(10px);
    padding: 16px 32px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.header-nav {
    display: flex;
    gap: 8px;
}

.nav-btn {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    background: rgba(0, 0, 0, 0.7);
    border: none;
    color: var(--text-primary);
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
}

.header-actions {
    display: flex;
    align-items: center;
    gap: 12px;
}

.btn-cloudinary-header {
    padding: 8px 16px;
    background: linear-gradient(135deg, #3b82f6, #2563eb);
    color: white;
    border-radius: 20px;
    font-size: 14px;
    font-weight: 600;
    transition: opacity 0.2s;
}

.btn-cloudinary-header:hover {
    opacity: 0.8;
}

.btn-premium {
    padding: 8px 32px;
    background: var(--text-primary);
    color: var(--bg-base);
    border: none;
    border-radius: 20px;
    font-weight: 700;
    font-size: 14px;
    cursor: pointer;
    transition: transform 0.2s;
}

.btn-premium:hover {
    transform: scale(1.04);
}

.btn-install {
    padding: 8px 16px;
    background: rgba(255, 255, 255, 0.1);
    color: var(--text-primary);
    border: none;
    border-radius: 20px;
    font-weight: 600;
    font-size: 14px;
    cursor: pointer;
}

.user-avatar {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 4px 12px 4px 4px;
    background: rgba(0, 0, 0, 0.7);
    border-radius: 20px;
    cursor: pointer;
}

.avatar-img {
    width: 28px;
    height: 28px;
    border-radius: 50%;
}

/* Content */
.content {
    padding: 0 32px 40px;
}

/* Greeting */
.greeting-section {
    padding: 8px 0 24px;
}

.greeting-title {
    font-size: 32px;
    font-weight: 700;
}

/* Featured */
.featured-section {
    margin-bottom: 40px;
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
    transition: filter 0.2s;
    overflow: hidden;
    position: relative;
}

.featured-card:hover {
    filter: brightness(1.1);
}

.featured-text h3 {
    font-size: 16px;
    font-weight: 700;
}

.featured-text p {
    font-size: 13px;
    opacity: 0.8;
    margin-top: 4px;
}

.featured-icon {
    font-size: 48px;
    opacity: 0.3;
    position: absolute;
    left: -8px;
    bottom: -8px;
    transform: rotate(15deg);
}

/* Playlists Section */
.playlists-section {
    margin-bottom: 40px;
}

.section-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
}

.show-all {
    font-size: 14px;
    font-weight: 600;
    color: var(--text-secondary);
}

.show-all:hover {
    color: var(--text-primary);
}

.playlists-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(185px, 1fr));
    gap: 24px;
}

.playlist-card {
    background: var(--bg-card);
    padding: 16px;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.3s;
    position: relative;
}

.playlist-card:hover {
    background: var(--bg-card-hover);
}

.card-image {
    width: 100%;
    aspect-ratio: 1;
    border-radius: 4px;
    margin-bottom: 16px;
    position: relative;
    display: flex;
    align-items: flex-end;
    justify-content: flex-end;
    padding: 12px;
}

.play-overlay {
    width: 48px;
    height: 48px;
    background: var(--spotify-green);
    border: none;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 0;
    transform: translateY(8px);
    transition: all 0.3s;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.5);
    cursor: pointer;
}

.playlist-card:hover .play-overlay {
    opacity: 1;
    transform: translateY(0);
}

.play-overlay:hover {
    background: var(--spotify-green-hover);
    transform: scale(1.05) !important;
}

.card-title {
    font-size: 16px;
    font-weight: 600;
    margin-bottom: 6px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.card-desc {
    font-size: 13px;
    color: var(--text-secondary);
    line-height: 1.5;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
}

/* Cloudinary Section */
.cloudinary-section {
    margin-bottom: 40px;
}

.cloudinary-card-main {
    background: linear-gradient(135deg, #1e3a8a, #3b82f6);
    border-radius: 12px;
    padding: 32px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.cloudinary-card-left h3 {
    font-size: 28px;
    font-weight: 700;
}

.cloudinary-card-left p {
    font-size: 16px;
    opacity: 0.8;
    margin-top: 8px;
}

.btn-view-collection {
    display: inline-block;
    margin-top: 16px;
    padding: 10px 24px;
    background: white;
    color: #1e3a8a;
    border-radius: 24px;
    font-weight: 700;
    transition: transform 0.2s;
}

.btn-view-collection:hover {
    transform: scale(1.04);
}

.cloudinary-stats {
    display: flex;
    gap: 24px;
}

.stat-item {
    text-align: center;
    background: rgba(255, 255, 255, 0.15);
    padding: 20px;
    border-radius: 12px;
}

.stat-number {
    font-size: 32px;
}

.stat-label {
    font-size: 13px;
    display: block;
    margin-top: 4px;
    opacity: 0.8;
}

/* Footer */
.site-footer {
    margin-top: 60px;
    padding: 40px 0;
}

.footer-links {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 24px;
    margin-bottom: 40px;
}

.footer-column h4 {
    font-size: 14px;
    font-weight: 700;
    margin-bottom: 16px;
    color: var(--text-primary);
}

.footer-column a {
    display: block;
    font-size: 14px;
    color: var(--text-secondary);
    margin-bottom: 10px;
    transition: color 0.2s;
}

.footer-column a:hover {
    color: var(--text-primary);
}

.footer-bottom {
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    padding-top: 24px;
}

.footer-bottom p {
    font-size: 14px;
    color: var(--text-secondary);
}

/* ========== PLAYER BAR ========== */
.player-bar {
    width: 100%;
    height: var(--player-height);
    background: var(--bg-base);
    border-top: 1px solid #282828;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 16px;
    z-index: 200;
    position: fixed;
    bottom: 0;
}

/* Now Playing */
.now-playing {
    display: flex;
    align-items: center;
    gap: 14px;
    min-width: 280px;
    width: 30%;
}

.now-playing-cover {
    flex-shrink: 0;
}

.cover-image {
    width: 56px;
    height: 56px;
    border-radius: 4px;
}

.now-playing-info {
    display: flex;
    flex-direction: column;
    gap: 4px;
    min-width: 0;
}

.track-name {
    font-size: 14px;
    font-weight: 500;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.track-artist {
    font-size: 12px;
    color: var(--text-secondary);
}

.like-btn {
    background: none;
    border: none;
    color: var(--text-secondary);
    cursor: pointer;
    flex-shrink: 0;
}

.like-btn:hover {
    color: var(--text-primary);
}

/* Player Controls */
.player-controls {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 8px;
    max-width: 600px;
    width: 40%;
}

.controls-buttons {
    display: flex;
    align-items: center;
    gap: 16px;
}

.control-btn {
    background: none;
    border: none;
    color: var(--text-secondary);
    cursor: pointer;
    transition: color 0.2s;
    display: flex;
    align-items: center;
    justify-content: center;
}

.control-btn:hover {
    color: var(--text-primary);
}

.play-btn-big {
    width: 32px;
    height: 32px;
    background: var(--text-primary);
    border: none;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: transform 0.1s;
}

.play-btn-big:hover {
    transform: scale(1.06);
}

/* Progress Bar */
.progress-container {
    display: flex;
    align-items: center;
    gap: 8px;
    width: 100%;
}

.time {
    font-size: 11px;
    color: var(--text-secondary);
    min-width: 40px;
    text-align: center;
}

.progress-bar-bg {
    flex: 1;
    height: 4px;
    background: #535353;
    border-radius: 2px;
    position: relative;
    cursor: pointer;
}

.progress-bar-bg:hover {
    height: 6px;
}

.progress-bar-fill {
    height: 100%;
    background: var(--text-primary);
    border-radius: 2px;
    transition: background 0.2s;
}

.progress-bar-bg:hover .progress-bar-fill {
    background: var(--spotify-green);
}

.progress-thumb {
    width: 12px;
    height: 12px;
    background: var(--text-primary);
    border-radius: 50%;
    position: absolute;
    top: 50%;
    transform: translate(-50%, -50%);
    opacity: 0;
    transition: opacity 0.2s;
}

.progress-bar-bg:hover .progress-thumb {
    opacity: 1;
}

/* Volume Controls */
.volume-controls {
    display: flex;
    align-items: center;
    gap: 8px;
    min-width: 200px;
    width: 30%;
    justify-content: flex-end;
}

.volume-bar-bg {
    width: 93px;
    height: 4px;
    background: #535353;
    border-radius: 2px;
    cursor: pointer;
    position: relative;
}

.volume-bar-bg:hover {
    height: 6px;
}

.volume-bar-fill {
    height: 100%;
    background: var(--text-primary);
    border-radius: 2px;
}

.volume-bar-bg:hover .volume-bar-fill {
    background: var(--spotify-green);
}

/* ========== RESPONSIVE ========== */
@media (max-width: 768px) {
    .sidebar {
        display: none;
    }
    
    .main-content {
        margin-right: 0;
    }
    
    .featured-grid {
        grid-template-columns: 1fr;
    }
    
    .playlists-grid {
        grid-template-columns: repeat(2, 1fr);
    }
    
    .cloudinary-card-main {
        flex-direction: column;
        gap: 24px;
    }
    
    .footer-links {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (max-width: 480px) {
    .playlists-grid {
        grid-template-columns: 1fr;
    }
    
    .footer-links {
        grid-template-columns: 1fr;
    }
    
    .now-playing {
        min-width: auto;
        width: auto;
    }
    
    .now-playing-cover {
        width: 40px;
        height: 40px;
    }
    
    .volume-controls {
        display: none;
    }
}

/* Scrollbar */
::-webkit-scrollbar {
    width: 12px;
}

::-webkit-scrollbar-track {
    background: transparent;
}

::-webkit-scrollbar-thumb {
    background: rgba(255, 255, 255, 0.2);
}

::-webkit-scrollbar-thumb:hover {
    background: rgba(255, 255, 255, 0.4);
}
"""

with open('static/css/style.css', 'w', encoding='utf-8') as f:
    f.write(style_css)
print("  ✅ static/css/style.css created")

# ==================== static/js/app.js ====================
print("\n⚡ إنشاء static/js/app.js...")

app_js = f"""// Spotify Clone - Cloudinary: {CLOUD_NAME}

// Greeting based on time
function updateGreeting() {{
    const hour = new Date().getHours();
    const greetingText = document.getElementById('greetingText');
    if (!greetingText) return;
    
    if (hour < 12) greetingText.textContent = 'صباح الخير';
    else if (hour < 18) greetingText.textContent = 'مساء الخير';
    else greetingText.textContent = 'مساء الخير';
}}

// Like button toggle
document.addEventListener('click', (e) => {{
    if (e.target.closest('.like-btn')) {{
        const btn = e.target.closest('.like-btn');
        const svg = btn.querySelector('svg path');
        if (svg) {{
            if (svg.getAttribute('fill') === 'currentColor') {{
                svg.setAttribute('fill', '#1db954');
            }} else {{
                svg.setAttribute('fill', 'currentColor');
            }}
        }}
    }}
}});

// Play button animation
document.addEventListener('click', (e) => {{
    const playBtn = e.target.closest('.play-overlay');
    if (playBtn) {{
        const svg = playBtn.querySelector('svg path');
        if (svg) {{
            if (svg.getAttribute('d') === 'M8 5v14l11-7z') {{
                // Pause icon
                svg.setAttribute('d', 'M6 4h4v16H6V4zm8 0h4v16h-4V4z');
                playBtn.style.background = '#1ed760';
            }} else {{
                // Play icon
                svg.setAttribute('d', 'M8 5v14l11-7z');
                playBtn.style.background = '#1db954';
            }}
        }}
    }}
    
    // Main play button
    const mainPlayBtn = e.target.closest('.play-btn-big');
    if (mainPlayBtn) {{
        const svg = mainPlayBtn.querySelector('svg path');
        if (svg) {{
            if (svg.getAttribute('d') === 'M8 5v14l11-7z') {{
                svg.setAttribute('d', 'M6 4h4v16H6V4zm8 0h4v16h-4V4z');
            }} else {{
                svg.setAttribute('d', 'M8 5v14l11-7z');
            }}
        }}
    }}
}});

// Initialize
document.addEventListener('DOMContentLoaded', () => {{
    updateGreeting();
    console.log('🎵 Spotify Clone Ready!');
    console.log('☁️ Cloudinary: {CLOUD_NAME}');
    console.log('📎 Collection: {COLLECTION_URL}');
}});
"""

with open('static/js/app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)
print("  ✅ static/js/app.js created")

# ==================== main.py ====================
print("\n🐍 إنشاء main.py...")

main_py = f"""from flask import Flask, render_template, jsonify
import cloudinary
import os
from datetime import datetime

app = Flask(__name__)

cloudinary.config(
    cloud_name="{CLOUD_NAME}",
    api_key=os.environ.get('CLOUDINARY_API_KEY', ''),
    api_secret=os.environ.get('CLOUDINARY_API_SECRET', '')
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/info')
def info():
    return jsonify({{
        "cloud_name": "{CLOUD_NAME}",
        "collection": "{COLLECTION_URL}",
        "status": "running",
        "time": datetime.now().isoformat()
    }})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
"""

with open('main.py', 'w', encoding='utf-8') as f:
    f.write(main_py)
print("  ✅ main.py created")

# ==================== requirements.txt ====================
with open('requirements.txt', 'w', encoding='utf-8') as f:
    f.write("flask==2.3.0\ncloudinary==1.36.0\ngunicorn==21.2.0\n")

# ==================== README.md ====================
readme = f"""# 🎵 Spotify Clone

![Spotify Clone](static/images/preview.png)

## ☁️ Cloudinary
- **Cloud Name:** `{CLOUD_NAME}`
- **Collection:** {COLLECTION_URL}

## 🚀 Features
- 🎨 واجهة مطابقة لـ Spotify
- 🎵 مشغل موسيقى متكامل
- 📱 تصميم متجاوب
- ☁️ تكامل Cloudinary

## 🚀 Run
```bash
pip install -r requirements.txt
python main.py
