#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🎵 Spotify Clone Generator - Final Version
Cloudinary: so2_mk | Collection: dmla61v7n
"""

import os
from pathlib import Path

CLOUD_NAME = "so2_mk"
COLLECTION_URL = "https://collection.cloudinary.com/dmla61v7n"

print(f"""
╔═══════════════════════════════════╗
║  🎵 Spotify Clone Generator     ║
║  ☁️  {CLOUD_NAME}                      ║
╚═══════════════════════════════════╝
""")

# ============================================================
# إنشاء المجلدات
# ============================================================
print("📁 Creating folders...")
for folder in [".github/workflows", "static/css", "static/js"]:
    Path(folder).mkdir(parents=True, exist_ok=True)
    print(f"  ✅ {folder}")

# ============================================================
# 1. index.html
# ============================================================
print("\n🎨 Creating index.html...")
with open("index.html", "w", encoding="utf-8") as f:
    f.write(f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🎵 Spotify - Web Player</title>
    <link rel="stylesheet" href="static/css/style.css">
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🎵</text></svg>">
</head>
<body>

    <!-- ==================== SIDEBAR ==================== -->
    <aside class="sidebar">
        <div class="sidebar-logo">
            <svg viewBox="0 0 24 24" width="40" height="40"><path fill="#1db954" d="M12 0C5.4 0 0 5.4 0 12s5.4 12 12 12 12-5.4 12-12S18.66 0 12 0zm5.521 17.34c-.24.359-.66.48-1.021.24-2.82-1.74-6.36-2.101-10.561-1.141-.418.122-.779-.179-.899-.539-.12-.421.18-.78.54-.9 4.56-1.021 8.52-.6 11.64 1.32.42.18.479.659.301 1.02z"/></svg>
            <span class="logo-text">Spotify</span>
        </div>

        <nav class="sidebar-nav">
            <a href="/" class="nav-item active">🏠 <span>الرئيسية</span></a>
            <a href="#" class="nav-item">🔍 <span>بحث</span></a>
            <a href="#" class="nav-item">📚 <span>مكتبتك</span></a>
        </nav>

        <div class="sidebar-section">
            <button class="sidebar-btn">➕ إنشاء قائمة تشغيل</button>
            <button class="sidebar-btn">❤️ الأغاني المفضلة</button>
            <div class="sidebar-divider"></div>
            <div class="playlist-links">
                <a href="#">🎧 Chill Vibes</a>
                <a href="#">🔥 Today's Top Hits</a>
                <a href="#">💪 Workout Energy</a>
                <a href="#">🌟 Arabic Hits 2024</a>
                <a href="#">🎸 Rock Classics</a>
            </div>
        </div>

        <div class="cloudinary-sidebar">
            <div class="cloud-badge">☁️ {CLOUD_NAME}</div>
            <a href="{COLLECTION_URL}" target="_blank">📎 Collection</a>
        </div>
    </aside>

    <!-- ==================== MAIN CONTENT ==================== -->
    <main class="main-content">
        <header class="top-header">
            <div class="header-nav">
                <button class="nav-arrow">⬅️</button>
                <button class="nav-arrow">➡️</button>
            </div>
            <div class="header-right">
                <a href="{COLLECTION_URL}" target="_blank" class="btn-cloud">☁️ Cloudinary</a>
                <button class="btn-premium">Premium</button>
                <div class="user-area">👤 <span>مستخدم</span></div>
            </div>
        </header>

        <div class="content">
            <h1 class="greeting">👋 مساء الخير</h1>

            <!-- Featured -->
            <section class="section">
                <h2 class="section-title">🎵 استمع مجدداً</h2>
                <div class="featured-grid">
                    <div class="featured-card" style="background:linear-gradient(135deg,#006450,#1db954)"><div><h3>Liked Songs</h3><p>432 أغنية</p></div><span class="card-bg-icon">❤️</span></div>
                    <div class="featured-card" style="background:linear-gradient(135deg,#1e3264,#608de2)"><div><h3>Daily Mix 1</h3><p>موسيقى هادئة</p></div><span class="card-bg-icon">🎧</span></div>
                    <div class="featured-card" style="background:linear-gradient(135deg,#8400e7,#b300b3)"><div><h3>Discover Weekly</h3><p>اكتشف أغاني جديدة</p></div><span class="card-bg-icon">🔍</span></div>
                    <div class="featured-card" style="background:linear-gradient(135deg,#503750,#8c1932)"><div><h3>Release Radar</h3><p>أحدث الإصدارات</p></div><span class="card-bg-icon">🆕</span></div>
                    <div class="featured-card" style="background:linear-gradient(135deg,#283048,#859398)"><div><h3>Chill Lofi</h3><p>هادئ ومنعش</p></div><span class="card-bg-icon">🌊</span></div>
                    <div class="featured-card" style="background:linear-gradient(135deg,#ff6b6b,#ee5a24)"><div><h3>Energy Boost</h3><p>طاقة وحماس</p></div><span class="card-bg-icon">⚡</span></div>
                </div>
            </section>

            <!-- Playlists -->
            <section class="section">
                <div class="section-header">
                    <h2 class="section-title">🔥 قوائم التشغيل المميزة</h2>
                    <a href="#">عرض الكل</a>
                </div>
                <div class="playlists-grid" id="playlistsGrid">
                    <!-- Generated by JS -->
                </div>
            </section>

            <!-- Cloudinary -->
            <section class="section">
                <h2 class="section-title">☁️ التكامل السحابي</h2>
                <div class="cloud-card">
                    <div>
                        <h3>{CLOUD_NAME}</h3>
                        <p>Cloudinary Collection</p>
                        <a href="{COLLECTION_URL}" target="_blank" class="btn-collection">عرض المجموعة →</a>
                    </div>
                    <div class="cloud-stats">
                        <div class="stat">☁️<span>Cloud</span></div>
                        <div class="stat">📁<span>Collection</span></div>
                        <div class="stat">✅<span>Connected</span></div>
                    </div>
                </div>
            </section>
        </div>
    </main>

    <!-- ==================== PLAYER BAR ==================== -->
    <footer class="player-bar">
        <div class="now-playing">
            <div class="cover">🎵</div>
            <div class="track-info">
                <span class="track-name">Blinding Lights</span>
                <span class="track-artist">The Weeknd</span>
            </div>
            <button class="like-btn">🤍</button>
        </div>

        <div class="player-center">
            <div class="controls">
                <button>🔀</button>
                <button>⏮️</button>
                <button class="play-btn">▶️</button>
                <button>⏭️</button>
                <button>🔁</button>
            </div>
            <div class="progress-bar">
                <span>1:23</span>
                <div class="bar"><div class="fill" style="width:35%"></div></div>
                <span>3:30</span>
            </div>
        </div>

        <div class="volume">
            <button>🔊</button>
            <div class="vol-bar"><div class="vol-fill" style="width:70%"></div></div>
        </div>
    </footer>

    <script src="static/js/app.js"></script>
</body>
</html>""")
print("  ✅ index.html")

# ============================================================
# 2. style.css
# ============================================================
print("\n🎨 Creating style.css...")
with open("static/css/style.css", "w", encoding="utf-8") as f:
    f.write("""*{margin:0;padding:0;box-sizing:border-box}:root{--bg:#000;--bg2:#121212;--bg3:#181818;--bg-hover:#282828;--text:#fff;--text2:#b3b3b3;--green:#1db954;--green-hover:#1ed760}body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;background:var(--bg);color:var(--text);overflow:hidden;height:100vh;display:flex}a{color:inherit;text-decoration:none}.sidebar{width:280px;height:calc(100vh - 90px);background:var(--bg);position:fixed;top:0;right:0;z-index:100;display:flex;flex-direction:column;padding:24px 12px 8px;overflow-y:auto}.sidebar-logo{display:flex;align-items:center;gap:12px;padding:0 12px 18px}.logo-text{font-size:24px;font-weight:700}.sidebar-nav{display:flex;flex-direction:column;gap:4px;padding:0 8px;margin-bottom:24px}.nav-item{display:flex;align-items:center;gap:16px;padding:8px 12px;border-radius:4px;color:var(--text2);font-weight:600;font-size:15px;transition:.2s}.nav-item:hover,.nav-item.active{color:var(--text);background:rgba(255,255,255,.1)}.sidebar-section{padding:0 8px}.sidebar-btn{display:flex;align-items:center;gap:12px;padding:8px 12px;background:0 0;border:0;color:var(--text2);font-size:14px;font-weight:600;cursor:pointer;width:100%;text-align:right;margin-bottom:4px}.sidebar-btn:hover{color:var(--text)}.sidebar-divider{height:1px;background:rgba(255,255,255,.1);margin:12px 0}.playlist-links{display:flex;flex-direction:column;gap:2px}.playlist-links a{padding:8px 12px;font-size:14px;color:var(--text2);border-radius:4px}.playlist-links a:hover{color:var(--text)}.cloudinary-sidebar{margin-top:auto;padding:16px 12px;border-top:1px solid rgba(255,255,255,.1);display:flex;flex-direction:column;gap:8px}.cloud-badge{display:flex;align-items:center;gap:8px;padding:8px 12px;background:linear-gradient(135deg,#2563eb,#1e40af);border-radius:6px;font-size:14px;font-weight:600;justify-content:center}.cloudinary-sidebar a{font-size:12px;color:var(--text2);text-align:center}.cloudinary-sidebar a:hover{color:var(--text)}.main-content{margin-right:280px;height:calc(100vh - 90px);overflow-y:auto;background:var(--bg2)}.top-header{position:sticky;top:0;z-index:50;background:rgba(0,0,0,.85);backdrop-filter:blur(10px);padding:16px 32px;display:flex;justify-content:space-between;align-items:center}.header-nav{display:flex;gap:8px}.nav-arrow{width:32px;height:32px;border-radius:50%;background:rgba(0,0,0,.7);border:0;color:var(--text);cursor:pointer;font-size:14px}.header-right{display:flex;align-items:center;gap:12px}.btn-cloud{padding:8px 16px;background:linear-gradient(135deg,#2563eb,#1d4ed8);color:#fff;border-radius:20px;font-size:14px;font-weight:600}.btn-premium{padding:8px 32px;background:var(--text);color:var(--bg);border:0;border-radius:20px;font-weight:700;cursor:pointer}.user-area{display:flex;align-items:center;gap:8px;padding:4px 12px;background:rgba(0,0,0,.7);border-radius:20px;cursor:pointer;font-size:14px}.content{padding:0 32px 40px}.greeting{font-size:32px;font-weight:700;padding:8px 0 24px}.section{margin-bottom:40px}.section-title{font-size:24px;font-weight:700;margin-bottom:20px}.section-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:20px}.section-header a{font-size:14px;font-weight:600;color:var(--text2)}.section-header a:hover{color:var(--text)}.featured-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:12px}.featured-card{height:80px;border-radius:6px;display:flex;align-items:center;justify-content:space-between;padding:16px;cursor:pointer;position:relative;overflow:hidden;transition:.2s}.featured-card:hover{filter:brightness(1.15)}.featured-card h3{font-size:16px;font-weight:700}.featured-card p{font-size:13px;opacity:.8;margin-top:4px}.card-bg-icon{font-size:48px;opacity:.25;position:absolute;left:-8px;bottom:-8px;transform:rotate(15deg)}.playlists-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(185px,1fr));gap:24px}.playlist-card{background:var(--bg3);padding:16px;border-radius:8px;cursor:pointer;transition:.3s;position:relative}.playlist-card:hover{background:var(--bg-hover)}.card-img{width:100%;aspect-ratio:1;border-radius:4px;margin-bottom:16px;display:flex;align-items:flex-end;justify-content:flex-end;padding:12px;position:relative}.card-play{width:48px;height:48px;background:var(--green);border:0;border-radius:50%;display:flex;align-items:center;justify-content:center;opacity:0;transform:translateY(8px);transition:.3s;box-shadow:0 8px 20px rgba(0,0,0,.5);cursor:pointer;font-size:20px}.playlist-card:hover .card-play{opacity:1;transform:translateY(0)}.card-play:hover{background:var(--green-hover);transform:scale(1.05)!important}.card-title{font-size:16px;font-weight:600;margin-bottom:6px}.card-desc{font-size:13px;color:var(--text2);line-height:1.5;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}.cloud-card{background:linear-gradient(135deg,#1e3a8a,#3b82f6);border-radius:12px;padding:32px;display:flex;justify-content:space-between;align-items:center}.cloud-card h3{font-size:28px;font-weight:700}.cloud-card p{font-size:16px;opacity:.8;margin-top:8px}.btn-collection{display:inline-block;margin-top:16px;padding:10px 24px;background:#fff;color:#1e3a8a;border-radius:24px;font-weight:700;transition:.2s}.btn-collection:hover{transform:scale(1.04)}.cloud-stats{display:flex;gap:24px}.stat{text-align:center;background:rgba(255,255,255,.15);padding:20px;border-radius:12px;font-size:32px}.stat span{display:block;font-size:13px;margin-top:4px;opacity:.8}.player-bar{width:100%;height:90px;background:#000;border-top:1px solid #282828;display:flex;align-items:center;justify-content:space-between;padding:0 16px;position:fixed;bottom:0;z-index:200}.now-playing{display:flex;align-items:center;gap:14px;min-width:280px;width:30%}.cover{font-size:56px}.track-info{display:flex;flex-direction:column;gap:4px;min-width:0}.track-name{font-size:14px;font-weight:500;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.track-artist{font-size:12px;color:var(--text2)}.like-btn{background:0 0;border:0;font-size:20px;cursor:pointer}.player-center{display:flex;flex-direction:column;align-items:center;gap:8px;max-width:600px;width:40%}.controls{display:flex;align-items:center;gap:16px}.controls button{background:0 0;border:0;color:var(--text2);cursor:pointer;font-size:18px}.controls button:hover{color:var(--text)}.play-btn{width:32px;height:32px;background:var(--text);border:0;border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;font-size:14px;color:#000}.progress-bar{display:flex;align-items:center;gap:8px;width:100%}.progress-bar span{font-size:11px;color:var(--text2);min-width:40px;text-align:center}.bar{flex:1;height:4px;background:#535353;border-radius:2px;cursor:pointer}.bar:hover{height:6px}.fill{height:100%;background:var(--text);border-radius:2px}.bar:hover .fill{background:var(--green)}.volume{display:flex;align-items:center;gap:8px;min-width:200px;width:30%;justify-content:flex-end}.volume button{background:0 0;border:0;color:var(--text2);cursor:pointer;font-size:18px}.vol-bar{width:93px;height:4px;background:#535353;border-radius:2px;cursor:pointer}.vol-bar:hover{height:6px}.vol-fill{height:100%;background:var(--text);border-radius:2px}.vol-bar:hover .vol-fill{background:var(--green)}@media(max-width:768px){.sidebar{display:none}.main-content{margin-right:0}.featured-grid{grid-template-columns:1fr}.playlists-grid{grid-template-columns:repeat(2,1fr)}.cloud-card{flex-direction:column;gap:24px}.now-playing{min-width:auto}.volume{display:none}}@media(max-width:480px){.playlists-grid{grid-template-columns:1fr}}::-webkit-scrollbar{width:12px}::-webkit-scrollbar-thumb{background:rgba(255,255,255,.2);border-radius:6px}::-webkit-scrollbar-thumb:hover{background:rgba(255,255,255,.4)}""")
print("  ✅ style.css")

# ============================================================
# 3. app.js
# ============================================================
print("\n⚡ Creating app.js...")
with open("static/js/app.js", "w", encoding="utf-8") as f:
    f.write(f"""// Spotify Clone JS - Cloudinary: {CLOUD_NAME}
console.log('🎵 Spotify Clone Ready! ☁️ {CLOUD_NAME}');

// Playlists data
const playlists = [
    {{name:'Today\\'s Top Hits',desc:'Taylor Swift, The Weeknd, Billie Eilish',color:'linear-gradient(135deg,#f093fb,#f5576c)'}},
    {{name:'RapCaviar',desc:'Drake, Kendrick Lamar, Travis Scott',color:'linear-gradient(135deg,#a8edea,#fed6e3)'}},
    {{name:'Arabic Hits 2024',desc:'عمرو دياب، إليسا، نانسي عجرم',color:'linear-gradient(135deg,#667eea,#764ba2)'}},
    {{name:'Chill Vibes',desc:'استرخِ مع أفضل الأغاني الهادئة',color:'linear-gradient(135deg,#ffecd2,#fcb69f)'}},
    {{name:'Workout Energy',desc:'طاقة وحماس للتمارين الرياضية',color:'linear-gradient(135deg,#4facfe,#00f2fe)'}},
    {{name:'Rock Classics',desc:'Queen, Led Zeppelin, AC/DC',color:'linear-gradient(135deg,#fa709a,#fee140)'}}
];

// Render playlists
const grid = document.getElementById('playlistsGrid');
if(grid){{
    grid.innerHTML = playlists.map(p => `
        <div class="playlist-card">
            <div class="card-img" style="background:${{p.color}}">
                <button class="card-play">▶️</button>
            </div>
            <h3 class="card-title">${{p.name}}</h3>
            <p class="card-desc">${{p.desc}}</p>
        </div>
    `).join('');
}}

// Click handlers
document.addEventListener('click',e=>{{
    // Like button
    if(e.target.closest('.like-btn')){{
        const btn = e.target.closest('.like-btn');
        btn.textContent = btn.textContent === '🤍' ? '💚' : '🤍';
    }}
    // Play buttons
    if(e.target.closest('.card-play')){{
        const btn = e.target.closest('.card-play');
        btn.textContent = btn.textContent === '▶️' ? '⏸️' : '▶️';
    }}
    if(e.target.closest('.play-btn')){{
        const btn = e.target.closest('.play-btn');
        btn.textContent = btn.textContent === '▶️' ? '⏸️' : '▶️';
    }}
}});
""")
print("  ✅ app.js")

# ============================================================
# 4. main.yml
# ============================================================
print("\n⚙️  Creating main.yml...")
with open(".github/workflows/main.yml", "w", encoding="utf-8") as f:
    f.write(f"""name: 🎵 Deploy Spotify Clone

on:
  push:
    branches: [ main, master ]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

env:
  CLOUD_NAME: {CLOUD_NAME}
  COLLECTION_URL: {COLLECTION_URL}

jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{{{ steps.deployment.outputs.page_url }}}}
    runs-on: ubuntu-latest
    steps:
      - name: 📥 Checkout
        uses: actions/checkout@v4
      
      - name: ⚙️ Setup Pages
        uses: actions/configure-pages@v4
      
      - name: 📤 Upload
        uses: actions/upload-pages-artifact@v3
        with:
          path: '.'
      
      - name: 🚀 Deploy
        id: deployment
        uses: actions/deploy-pages@v4
      
      - name: 🎉 Done
        run: |
          echo "✅ Deployed!"
          echo "☁️ Cloudinary: ${{{{ env.CLOUD_NAME }}}}"
          echo "📎 Collection: ${{{{ env.COLLECTION_URL }}}}"
          echo "🌐 URL: ${{{{ steps.deployment.outputs.page_url }}}}"
""")
print("  ✅ main.yml")

# ============================================================
# 5. main.py
# ============================================================
print("\n🐍 Creating main.py...")
with open("main.py", "w", encoding="utf-8") as f:
    f.write(f"""from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
""")
print("  ✅ main.py")

# ============================================================
# 6. requirements.txt
# ============================================================
print("\n📦 Creating requirements.txt...")
with open("requirements.txt", "w") as f:
    f.write("flask==2.3.0\ngunicorn==21.2.0\n")
print("  ✅ requirements.txt")

# ============================================================
# 7. README.md
# ============================================================
print("\n📝 Creating README.md...")
with open("README.md", "w", encoding="utf-8") as f:
    f.write(f"""# 🎵 Spotify Clone

![Status](https://img.shields.io/badge/status-live-brightgreen)
![Cloudinary](https://img.shields.io/badge/cloudinary-{CLOUD_NAME}-blue)

## ☁️ Cloudinary
- **Cloud Name:** `{CLOUD_NAME}`
- **Collection:** {COLLECTION_URL}

## 🚀 Run
```bash
pip install -r requirements.txt
python main.py
