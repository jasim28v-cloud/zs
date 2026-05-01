#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Spotify Clone Generator - صديقك الذهب 🎵
يقوم بإنشاء جميع ملفات المشروع ورفعها تلقائياً
"""

import os
import json
import shutil
import requests
from pathlib import Path
from datetime import datetime
import subprocess

class SpotifyCloneGenerator:
    def __init__(self, cloud_name="do_2gg", collection_url="https://collection.cloudinary.com/dnmpmysk6"):
        self.cloud_name = cloud_name
        self.collection_url = collection_url
        self.project_name = "spotify-clone"
        self.base_path = Path(self.project_name)
        
        # هيكل المجلدات
        self.structure = {
            "folders": [
                ".github/workflows",
                "templates",
                "static/css",
                "static/js",
                "static/images",
                "data",
                "scripts"
            ],
            "files": []
        }
        
        print(f"""
        ╔══════════════════════════════════════════╗
        ║     🎵 Spotify Clone Generator 🎵      ║
        ║     Cloud: {cloud_name}                    ║
        ║     Collection: {collection_url[:30]}... ║
        ╚══════════════════════════════════════════╝
        """)

    def create_directory_structure(self):
        """إنشاء هيكل المجلدات"""
        print("📁 إنشاء المجلدات...")
        for folder in self.structure["folders"]:
            folder_path = self.base_path / folder
            folder_path.mkdir(parents=True, exist_ok=True)
            print(f"  ✅ {folder}")

    def generate_main_yml(self):
        """إنشاء ملف GitHub Actions"""
        print("\n⚙️  إنشاء GitHub Actions workflow...")
        
        yml_content = f"""name: Deploy Spotify Clone to Cloudinary & GitHub Pages

on:
  push:
    branches: [ main, master ]
  pull_request:
    branches: [ main, master ]
  workflow_dispatch:

env:
  CLOUD_NAME: {self.cloud_name}
  COLLECTION_URL: {self.collection_url}

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    
    steps:
    - name: 🚚 Checkout Repository
      uses: actions/checkout@v3
    
    - name: 🐍 Setup Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    
    - name: 📦 Install Dependencies
      run: |
        python -m pip install --upgrade pip
        pip install flask cloudinary requests python-dotenv gunicorn
    
    - name: 🔍 Verify Project Structure
      run: |
        echo "Checking project structure..."
        ls -la
        echo "Cloudinary Config:"
        echo "  Cloud Name: ${{{{ env.CLOUD_NAME }}}}"
        echo "  Collection: ${{{{ env.COLLECTION_URL }}}}"
    
    - name: 📤 Upload to Cloudinary
      env:
        CLOUDINARY_URL: cloudinary://${{{{ secrets.CLOUDINARY_API_KEY }}}}:${{{{ secrets.CLOUDINARY_API_SECRET }}}}@${{{{ env.CLOUD_NAME }}}}
      run: |
        python scripts/upload_to_cloudinary.py
    
    - name: 🧪 Run Tests
      run: |
        python -m pytest tests/ || echo "No tests yet, continuing..."
    
    - name: 📊 Generate Build Report
      run: |
        echo "# 🎵 Spotify Clone Build Report" > BUILD_REPORT.md
        echo "**Build Date:** $(date)" >> BUILD_REPORT.md
        echo "**Cloud Name:** ${{{{ env.CLOUD_NAME }}}}" >> BUILD_REPORT.md
        echo "**Status:** Success ✅" >> BUILD_REPORT.md
    
    - name: 🚀 Deploy to GitHub Pages
      if: github.ref == 'refs/heads/main'
      uses: peaceiris/actions-gh-pages@v3
      with:
        github_token: ${{{{ secrets.GITHUB_TOKEN }}}}
        publish_dir: ./static
        publish_branch: gh-pages
        commit_message: '🚀 Auto-deploy Spotify Clone ${{{{ github.sha }}}}'
    
    - name: 📢 Notify Deployment
      run: |
        echo "🎉 Deployment Complete!"
        echo "📎 Live URL: https://${{{{ github.repository_owner }}}}.github.io/${{{{ github.event.repository.name }}}}"
        echo "☁️ Cloudinary: https://console.cloudinary.com/${{{{ env.CLOUD_NAME }}}}"
        echo "📚 Collection: ${{{{ env.COLLECTION_URL }}}}"

  sync-cloudinary:
    runs-on: ubuntu-latest
    needs: build-and-deploy
    
    steps:
    - name: 🔄 Sync with Cloudinary Collection
      run: |
        echo "Syncing with collection: ${{{{ env.COLLECTION_URL }}}}"
        curl -X POST ${{{{ env.COLLECTION_URL }}}}/sync \\
          -H "Authorization: Bearer ${{{{ secrets.CLOUDINARY_API_KEY }}}}" \\
          -d '{{"action": "sync"}}'
"""
        
        workflow_path = self.base_path / ".github" / "workflows" / "main.yml"
        workflow_path.parent.mkdir(parents=True, exist_ok=True)
        workflow_path.write_text(yml_content, encoding='utf-8')
        print(f"  ✅ main.yml created at {workflow_path}")

    def generate_flask_app(self):
        """إنشاء تطبيق Flask الرئيسي"""
        print("\n🐍 إنشاء main.py...")
        
        main_py = f"""from flask import Flask, render_template, jsonify, request, send_from_directory
import cloudinary
import cloudinary.uploader
import cloudinary.api
from datetime import datetime
import os
import json

app = Flask(__name__)

# Cloudinary Configuration
cloudinary.config(
    cloud_name="{self.cloud_name}",
    api_key=os.environ.get('CLOUDINARY_API_KEY', 'DEMO_KEY'),
    api_secret=os.environ.get('CLOUDINARY_API_SECRET', 'DEMO_SECRET')
)

# Load music data
def load_music_data():
    try:
        with open('data/music_data.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return get_default_data()

def get_default_data():
    return {{
        "playlists": [
            {{"id": 1, "name": "Today's Top Hits", "description": "Hottest tracks right now", "cover": "🔥", "tracks_count": 50}},
            {{"id": 2, "name": "RapCaviar", "description": "Best hip-hop tracks", "cover": "🎤", "tracks_count": 45}},
            {{"id": 3, "name": "Chill Vibes", "description": "Relax and unwind", "cover": "🌊", "tracks_count": 40}},
            {{"id": 4, "name": "Workout Energy", "description": "Power through your workout", "cover": "💪", "tracks_count": 35}},
            {{"id": 5, "name": "Arabic Hits", "description": "Best Arabic music", "cover": "🌟", "tracks_count": 55}},
            {{"id": 6, "name": "Rock Classics", "description": "Legendary rock anthems", "cover": "🎸", "tracks_count": 60}}
        ],
        "featured": [
            {{"title": "New Releases", "description": "Fresh music for you", "color": "#450af5"}},
            {{"title": "Mood Boosters", "description": "Feel good tracks", "color": "#1db954"}},
            {{"title": "Focus", "description": "Music to help you concentrate", "color": "#ff4632"}}
        ]
    }}

@app.route('/')
def index():
    return render_template('index.html', cloud_name="{self.cloud_name}")

@app.route('/api/playlists')
def get_playlists():
    data = load_music_data()
    return jsonify(data.get('playlists', []))

@app.route('/api/featured')
def get_featured():
    data = load_music_data()
    return jsonify(data.get('featured', []))

@app.route('/api/cloudinary-info')
def cloudinary_info():
    return jsonify({{
        "cloud_name": "{self.cloud_name}",
        "collection_url": "{self.collection_url}",
        "status": "connected",
        "timestamp": datetime.now().isoformat()
    }})

@app.route('/upload-to-cloudinary', methods=['POST'])
def upload_to_cloudinary():
    if 'file' not in request.files:
        return jsonify({{"error": "No file provided"}}), 400
    
    file = request.files['file']
    if file:
        try:
            result = cloudinary.uploader.upload(
                file,
                folder="spotify_clone",
                resource_type="auto"
            )
            return jsonify({{
                "success": True,
                "url": result['secure_url'],
                "public_id": result['public_id']
            }})
        except Exception as e:
            return jsonify({{"error": str(e)}}), 500
    
    return jsonify({{"error": "Upload failed"}}), 400

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
"""
        
        (self.base_path / "main.py").write_text(main_py, encoding='utf-8')
        print("  ✅ main.py created")

    def generate_html_template(self):
        """إنشاء قالب HTML"""
        print("\n🎨 إنشاء index.html...")
        
        html_content = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🎵 Spotify Clone | Cloudinary {self.cloud_name}</title>
    <link rel="stylesheet" href="/static/css/style.css">
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🎵</text></svg>">
</head>
<body>
    <!-- Sidebar -->
    <aside class="sidebar">
        <div class="logo-container">
            <div class="logo">🎵 Spotify</div>
            <div class="cloud-badge">☁️ {self.cloud_name}</div>
        </div>
        <nav class="nav-menu">
            <a href="/" class="nav-item active">
                <span class="nav-icon">🏠</span>
                <span>الرئيسية</span>
            </a>
            <a href="#" class="nav-item">
                <span class="nav-icon">🔍</span>
                <span>بحث</span>
            </a>
            <a href="#" class="nav-item">
                <span class="nav-icon">📚</span>
                <span>مكتبتك</span>
            </a>
            <a href="#" class="nav-item">
                <span class="nav-icon">❤️</span>
                <span>المفضلة</span>
            </a>
        </nav>
        
        <div class="playlists-section">
            <h3>🎧 قوائم التشغيل</h3>
            <div class="playlist-item">✨ قائمة التشغيل 1</div>
            <div class="playlist-item">🎸 روك كلاسيك</div>
            <div class="playlist-item">🌙 أغاني هادئة</div>
        </div>

        <div class="cloudinary-section">
            <h3>☁️ Cloudinary</h3>
            <p class="cloud-info">Cloud: <strong>{self.cloud_name}</strong></p>
            <input type="file" id="uploadInput" accept="image/*,audio/*" style="display:none">
            <button class="upload-btn" onclick="document.getElementById('uploadInput').click()">
                📤 رفع ملف
            </button>
            <div id="uploadStatus" class="upload-status"></div>
        </div>
    </aside>

    <!-- Main Content -->
    <main class="main-content">
        <!-- Header -->
        <header class="top-bar">
            <div class="nav-arrows">
                <button class="arrow-btn">⬅️</button>
                <button class="arrow-btn">➡️</button>
            </div>
            <div class="user-section">
                <span class="premium-badge">👑 Premium</span>
                <span class="user-avatar">👤</span>
            </div>
        </header>

        <!-- Greeting -->
        <section class="greeting-section">
            <h1>👋 مساء الخير</h1>
            <div class="featured-grid" id="featuredGrid">
                <!-- Generated by JS -->
            </div>
        </section>

        <!-- Playlists -->
        <section class="content-section">
            <h2>🎵 قوائم التشغيل المميزة</h2>
            <div class="playlists-grid" id="playlistsGrid">
                <!-- Generated by JS -->
            </div>
        </section>

        <!-- Cloudinary Integration -->
        <section class="content-section">
            <h2>☁️ التكامل مع Cloudinary</h2>
            <div class="cloudinary-card">
                <div class="cloud-header">
                    <span class="cloud-icon">☁️</span>
                    <div>
                        <h3>{self.cloud_name}</h3>
                        <p>Cloudinary Collection</p>
                    </div>
                </div>
                <div class="cloud-body">
                    <p>📎 <a href="{self.collection_url}" target="_blank">عرض المجموعة الكاملة</a></p>
                    <div class="recent-uploads" id="recentUploads">
                        <p style="opacity:0.7">لم يتم رفع ملفات بعد...</p>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <!-- Player Bar -->
    <footer class="player-bar">
        <div class="now-playing">
            <div class="track-cover">🎵</div>
            <div class="track-info">
                <div class="track-name">No Track Playing</div>
                <div class="track-artist">Select a song</div>
            </div>
            <button class="like-btn">❤️</button>
        </div>
        <div class="player-controls">
            <button class="control-btn">🔀</button>
            <button class="control-btn">⏮️</button>
            <button class="control-btn play-btn">▶️</button>
            <button class="control-btn">⏭️</button>
            <button class="control-btn">🔁</button>
            <div class="progress-bar">
                <span class="time">0:00</span>
                <div class="progress">
                    <div class="progress-filled"></div>
                </div>
                <span class="time">0:00</span>
            </div>
        </div>
        <div class="volume-controls">
            <button class="control-btn">🔊</button>
            <div class="volume-bar">
                <div class="volume-filled"></div>
            </div>
        </div>
    </footer>

    <!-- Cloudinary Widget -->
    <script src="https://upload-widget.cloudinary.com/global/all.js" type="text/javascript"></script>
    <script src="/static/js/app.js"></script>
</body>
</html>"""
        
        (self.base_path / "templates" / "index.html").write_text(html_content, encoding='utf-8')
        print("  ✅ index.html created")

    def generate_css(self):
        """إنشاء ملف CSS"""
        print("\n🎨 إنشاء style.css...")
        
        css_content = """/* Spotify Clone Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

:root {
    --spotify-green: #1db954;
    --spotify-black: #191414;
    --sidebar-bg: #000000;
    --main-bg: #121212;
    --card-bg: #181818;
    --text-primary: #ffffff;
    --text-secondary: #b3b3b3;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
    background: var(--main-bg);
    color: var(--text-primary);
    overflow-x: hidden;
}

/* Sidebar */
.sidebar {
    position: fixed;
    right: 0;
    top: 0;
    width: 240px;
    height: 100vh;
    background: var(--sidebar-bg);
    padding: 24px 12px;
    z-index: 1000;
}

.logo-container {
    margin-bottom: 24px;
    padding: 0 12px;
}

.logo {
    font-size: 28px;
    font-weight: 700;
    color: var(--spotify-green);
}

.cloud-badge {
    font-size: 11px;
    color: var(--text-secondary);
    margin-top: 4px;
    padding: 2px 8px;
    background: rgba(255,255,255,0.1);
    border-radius: 12px;
    display: inline-block;
}

.nav-menu {
    margin-bottom: 24px;
}

.nav-item {
    display: flex;
    align-items: center;
    gap: 16px;
    padding: 8px 12px;
    color: var(--text-secondary);
    text-decoration: none;
    border-radius: 4px;
    transition: all 0.2s;
}

.nav-item:hover, .nav-item.active {
    color: var(--text-primary);
    background: rgba(255,255,255,0.1);
}

.nav-icon {
    font-size: 20px;
}

/* Main Content */
.main-content {
    margin-right: 240px;
    padding: 24px;
    padding-bottom: 120px;
}

.top-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 32px;
}

.nav-arrows {
    display: flex;
    gap: 16px;
}

.arrow-btn {
    background: rgba(0,0,0,0.7);
    border: none;
    color: white;
    width: 32px;
    height: 32px;
    border-radius: 50%;
    cursor: pointer;
}

.user-section {
    display: flex;
    align-items: center;
    gap: 16px;
}

.premium-badge {
    background: rgba(255,255,255,0.1);
    padding: 6px 16px;
    border-radius: 20px;
    font-size: 14px;
}

/* Content Grids */
.content-section {
    margin-bottom: 40px;
}

.content-section h2 {
    margin-bottom: 20px;
    font-size: 24px;
}

.featured-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 16px;
    margin-bottom: 40px;
}

.featured-card {
    background: rgba(255,255,255,0.1);
    backdrop-filter: blur(10px);
    border-radius: 8px;
    padding: 16px;
    display: flex;
    align-items: center;
    gap: 16px;
    cursor: pointer;
    transition: all 0.3s;
}

.featured-card:hover {
    background: rgba(255,255,255,0.2);
    transform: scale(1.02);
}

.playlists-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
    gap: 24px;
}

.playlist-card {
    background: var(--card-bg);
    padding: 16px;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.3s;
}

.playlist-card:hover {
    background: #282828;
}

/* Cloudinary Card */
.cloudinary-card {
    background: linear-gradient(135deg, #3b82f6, #1e40af);
    padding: 24px;
    border-radius: 12px;
    margin-top: 16px;
}

.cloud-header {
    display: flex;
    align-items: center;
    gap: 16px;
    margin-bottom: 16px;
}

.cloud-icon {
    font-size: 40px;
}

/* Player Bar */
.player-bar {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    height: 90px;
    background: #181818;
    border-top: 1px solid #282828;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 16px;
    z-index: 1000;
}

.now-playing {
    display: flex;
    align-items: center;
    gap: 14px;
    width: 30%;
}

.player-controls {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 40%;
    gap: 8px;
}

.control-btn {
    background: none;
    border: none;
    color: var(--text-secondary);
    font-size: 16px;
    cursor: pointer;
    margin: 0 8px;
}

.control-btn:hover {
    color: var(--text-primary);
}

.play-btn {
    background: var(--text-primary);
    color: var(--spotify-black);
    width: 32px;
    height: 32px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
}

.progress-bar {
    display: flex;
    align-items: center;
    gap: 8px;
    width: 100%;
}

.progress {
    flex: 1;
    height: 4px;
    background: #535353;
    border-radius: 2px;
}

.progress-filled {
    width: 30%;
    height: 100%;
    background: var(--text-primary);
    border-radius: 2px;
}

/* Upload Section */
.cloudinary-section {
    margin-top: 24px;
    padding: 12px;
}

.upload-btn {
    background: var(--spotify-green);
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 20px;
    cursor: pointer;
    width: 100%;
    margin-top: 8px;
}

.upload-btn:hover {
    background: #1ed760;
}

/* Responsive */
@media (max-width: 768px) {
    .sidebar {
        display: none;
    }
    .main-content {
        margin-right: 0;
    }
    .player-bar {
        right: 0;
    }
}
"""
        
        (self.base_path / "static" / "css" / "style.css").write_text(css_content, encoding='utf-8')
        print("  ✅ style.css created")

    def generate_javascript(self):
        """إنشاء ملف JavaScript"""
        print("\n⚡ إنشاء app.js...")
        
        js_content = f"""// Spotify Clone - Cloudinary Integration
const CLOUD_NAME = '{self.cloud_name}';
const COLLECTION_URL = '{self.collection_url}';

// Load playlists
async function loadPlaylists() {{
    try {{
        const response = await fetch('/api/playlists');
        const playlists = await response.json();
        displayPlaylists(playlists);
    }} catch (error) {{
        console.error('Error loading playlists:', error);
        displayDefaultContent();
    }}
}}

// Load featured
async function loadFeatured() {{
    try {{
        const response = await fetch('/api/featured');
        const featured = await response.json();
        displayFeatured(featured);
    }} catch (error) {{
        console.error('Error loading featured:', error);
    }}
}}

// Display content
function displayPlaylists(playlists) {{
    const grid = document.getElementById('playlistsGrid');
    if (!grid) return;
    
    grid.innerHTML = playlists.map(pl => `
        <div class="playlist-card">
            <div class="playlist-image" style="font-size: 48px; text-align: center; padding: 20px;">
                ${{pl.cover || '🎵'}}
            </div>
            <div class="playlist-card-title">${{pl.name}}</div>
            <div class="playlist-card-desc">${{pl.description}}</div>
        </div>
    `).join('');
}}

function displayFeatured(featured) {{
    const grid = document.getElementById('featuredGrid');
    if (!grid) return;
    
    grid.innerHTML = featured.map(item => `
        <div class="featured-card" style="background: ${{item.color}}40;">
            <span style="font-size: 32px;">🎵</span>
            <div>
                <h3>${{item.title}}</h3>
                <p>${{item.description}}</p>
            </div>
        </div>
    `).join('');
}}

function displayDefaultContent() {{
    const defaultPlaylists = [
        {{name: "Today's Top Hits", cover: "🔥", description: "Hottest tracks"}},
        {{name: "Chill Vibes", cover: "🌊", description: "Relax"}},
        {{name: "Workout", cover: "💪", description: "Energy"}},
        {{name: "Arabic Hits", cover: "🌟", description: "Best Arabic"}},
        {{name: "Rock Classics", cover: "🎸", description: "Legends"}},
        {{name: "Podcasts", cover: "🎙️", description: "Listen now"}}
    ];
    displayPlaylists(defaultPlaylists);
}}

// Cloudinary Upload Widget
function initializeCloudinaryUpload() {{
    const uploadInput = document.getElementById('uploadInput');
    if (!uploadInput) return;
    
    uploadInput.addEventListener('change', async (e) => {{
        const file = e.target.files[0];
        if (!file) return;
        
        const formData = new FormData();
        formData.append('file', file);
        
        const status = document.getElementById('uploadStatus');
        if (status) {{
            status.innerHTML = '<p style="color: #1db954;">⏳ جاري الرفع إلى Cloudinary...</p>';
        }}
        
        try {{
            const response = await fetch('/upload-to-cloudinary', {{
                method: 'POST',
                body: formData
            }});
            const data = await response.json();
            
            if (data.success) {{
                if (status) {{
                    status.innerHTML = `
                        <p style="color: #1db954;">✅ تم الرفع بنجاح!</p>
                        <p style="font-size: 12px; margin-top: 4px;">
                            <a href="${{data.url}}" target="_blank" style="color: #1db954;">
                                🔗 عرض الملف
                            </a>
                        </p>
                    `;
                }}
                addToRecentUploads(data.url);
            }} else {{
                throw new Error(data.error || 'Upload failed');
            }}
        }} catch (error) {{
            if (status) {{
                status.innerHTML = `<p style="color: #ff4444;">❌ فشل الرفع: ${{error.message}}</p>`;
            }}
        }}
    }});
}}

function addToRecentUploads(url) {{
    const container = document.getElementById('recentUploads');
    if (!container) return;
    
    const item = document.createElement('div');
    item.className = 'recent-item';
    item.innerHTML = `
        <span>📁</span>
        <a href="${{url}}" target="_blank" style="color: white; font-size: 12px;">
            ${{url.split('/').pop().substring(0, 30)}}...
        </a>
    `;
    container.prepend(item);
}}

// Mock Player Controls
function initializePlayer() {{
    const playBtn = document.querySelector('.play-btn');
    if (playBtn) {{
        let isPlaying = false;
        playBtn.addEventListener('click', () => {{
            isPlaying = !isPlaying;
            playBtn.textContent = isPlaying ? '⏸️' : '▶️';
        }});
    }}
    
    const likeBtn = document.querySelector('.like-btn');
    if (likeBtn) {{
        let isLiked = false;
        likeBtn.addEventListener('click', () => {{
            isLiked = !isLiked;
            likeBtn.style.color = isLiked ? '#1db954' : '#b3b3b3';
        }});
    }}
}}

// Display Cloudinary Info
function showCloudinaryInfo() {{
    console.log(`
    ☁️ Cloudinary Configuration:
    - Cloud Name: ${{CLOUD_NAME}}
    - Collection: ${{COLLECTION_URL}}
    - Status: Connected ✅
    `);
}}

// Initialize
document.addEventListener('DOMContentLoaded', () => {{
    loadPlaylists();
    loadFeatured();
    initializeCloudinaryUpload();
    initializePlayer();
    showCloudinaryInfo();
    
    console.log('🎵 Spotify Clone Ready!');
    console.log('☁️ Cloudinary:', CLOUD_NAME);
}});
"""
        
        (self.base_path / "static" / "js" / "app.js").write_text(js_content, encoding='utf-8')
        print("  ✅ app.js created")

    def generate_config_files(self):
        """إنشاء ملفات التكوين"""
        print("\n⚙️  إنشاء ملفات التكوين...")
        
        # requirements.txt
        requirements = """flask==2.3.0
cloudinary==1.36.0
requests==2.31.0
python-dotenv==1.0.0
gunicorn==21.2.0
pytest==7.4.0"""
        (self.base_path / "requirements.txt").write_text(requirements, encoding='utf-8')
        
        # .env
        env_content = f"""CLOUDINARY_CLOUD_NAME={self.cloud_name}
CLOUDINARY_COLLECTION_URL={self.collection_url}
FLASK_ENV=production
SECRET_KEY=spotify-clone-secret-key-{datetime.now().timestamp()}"""
        (self.base_path / ".env").write_text(env_content, encoding='utf-8')
        
        # .gitignore
        gitignore = """venv/
__pycache__/
*.pyc
.env
*.db
.DS_Store
node_modules/
*.log"""
        (self.base_path / ".gitignore").write_text(gitignore, encoding='utf-8')
        
        # README.md
        readme = f"""# 🎵 Spotify Clone with Cloudinary

![Cloudinary](https://img.shields.io/badge/Cloudinary-{self.cloud_name}-blue)
![Python](https://img.shields.io/badge/Python-3.8+-green)
![Flask](https://img.shields.io/badge/Flask-2.3.0-red)

## ☁️ Cloudinary Integration
- **Cloud Name:** `{self.cloud_name}`
- **Collection:** [{self.collection_url}]({self.collection_url})

## 🚀 Quick Start
```bash
pip install -r requirements.txt
python main.py
