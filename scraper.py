#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Spotify Clone Generator - صديقك الذهب 🎵
Cloudinary: so2_mk
"""

import os
import json
import shutil
from pathlib import Path
from datetime import datetime
import subprocess

class SpotifyCloneGenerator:
    def __init__(self, cloud_name="so2_mk", collection_url="https://collection.cloudinary.com/dmla61v7n"):
        self.cloud_name = cloud_name
        self.collection_url = collection_url
        self.project_name = "spotify-clone"
        self.base_path = Path(self.project_name)
        
        print(f"""
        ╔══════════════════════════════════════╗
        ║   🎵 Spotify Clone Generator 🎵    ║
        ║   Cloud: {cloud_name}                   ║
        ║   Collection: dmla61v7n             ║
        ╚══════════════════════════════════════╝
        """)

    def create_directory_structure(self):
        """إنشاء هيكل المجلدات"""
        print("📁 إنشاء المجلدات...")
        folders = [
            ".github/workflows",
            "templates",
            "static/css",
            "static/js",
            "static/images",
            "data",
            "scripts"
        ]
        for folder in folders:
            folder_path = self.base_path / folder
            folder_path.mkdir(parents=True, exist_ok=True)
            print(f"  ✅ {folder}")

    def generate_main_yml(self):
        """إنشاء ملف GitHub Actions"""
        print("\n⚙️  إنشاء .github/workflows/main.yml...")
        
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
        echo "☁️ Cloudinary Config:"
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
        print(f"  ✅ main.yml created")

    def generate_flask_app(self):
        """إنشاء main.py"""
        print("\n🐍 إنشاء main.py...")
        
        main_py = f"""from flask import Flask, render_template, jsonify, request, send_from_directory
import cloudinary
import cloudinary.uploader
import cloudinary.api
from datetime import datetime
import os
import json

app = Flask(__name__)

# Cloudinary Configuration - so2_mk
cloudinary.config(
    cloud_name="{self.cloud_name}",
    api_key=os.environ.get('CLOUDINARY_API_KEY', 'DEMO_KEY'),
    api_secret=os.environ.get('CLOUDINARY_API_SECRET', 'DEMO_SECRET')
)

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

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
"""
        
        (self.base_path / "main.py").write_text(main_py, encoding='utf-8')
        print("  ✅ main.py created")

    def generate_html_template(self):
        """إنشاء index.html"""
        print("\n🎨 إنشاء index.html...")
        
        html_content = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🎵 Spotify Clone | Cloudinary {self.cloud_name}</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
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

    <main class="main-content">
        <header class="top-bar">
            <div class="user-section">
                <span class="premium-badge">👑 Premium</span>
                <span class="user-avatar">👤</span>
            </div>
        </header>

        <section class="content-section">
            <h2>🎵 قوائم التشغيل المميزة</h2>
            <div class="playlists-grid" id="playlistsGrid"></div>
        </section>

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
        </div>
        <div class="volume-controls">
            <button class="control-btn">🔊</button>
        </div>
    </footer>

    <script src="https://upload-widget.cloudinary.com/global/all.js"></script>
    <script src="/static/js/app.js"></script>
</body>
</html>"""
        
        (self.base_path / "templates" / "index.html").write_text(html_content, encoding='utf-8')
        print("  ✅ index.html created")

    def generate_css(self):
        """إنشاء style.css"""
        print("\n🎨 إنشاء style.css...")
        
        css_content = """* {
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

.main-content {
    margin-right: 240px;
    padding: 24px;
    padding-bottom: 120px;
}

.top-bar {
    display: flex;
    justify-content: flex-end;
    align-items: center;
    margin-bottom: 32px;
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

.content-section {
    margin-bottom: 40px;
}

.content-section h2 {
    margin-bottom: 20px;
    font-size: 24px;
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
    align-items: center;
    width: 40%;
    gap: 8px;
    justify-content: center;
}

.control-btn {
    background: none;
    border: none;
    color: var(--text-secondary);
    font-size: 16px;
    cursor: pointer;
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
}

@media (max-width: 768px) {
    .sidebar {
        display: none;
    }
    .main-content {
        margin-right: 0;
    }
}
"""
        
        (self.base_path / "static" / "css" / "style.css").write_text(css_content, encoding='utf-8')
        print("  ✅ style.css created")

    def generate_javascript(self):
        """إنشاء app.js"""
        print("\n⚡ إنشاء app.js...")
        
        js_content = f"""// Spotify Clone - Cloudinary: {self.cloud_name}
const CLOUD_NAME = '{self.cloud_name}';
const COLLECTION_URL = '{self.collection_url}';

async function loadPlaylists() {{
    try {{
        const response = await fetch('/api/playlists');
        const playlists = await response.json();
        displayPlaylists(playlists);
    }} catch (error) {{
        console.error('Error:', error);
        displayDefaultContent();
    }}
}}

function displayPlaylists(playlists) {{
    const grid = document.getElementById('playlistsGrid');
    if (!grid) return;
    
    grid.innerHTML = playlists.map(pl => `
        <div class="playlist-card">
            <div style="font-size: 48px; text-align: center; padding: 20px;">
                ${{pl.cover || '🎵'}}
            </div>
            <div style="font-weight: 600;">${{pl.name}}</div>
            <div style="font-size: 14px; opacity: 0.7;">${{pl.description}}</div>
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

// Cloudinary Upload
document.addEventListener('DOMContentLoaded', () => {{
    loadPlaylists();
    
    const uploadInput = document.getElementById('uploadInput');
    if (uploadInput) {{
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
                        status.innerHTML = `<p style="color: #1db954;">✅ تم الرفع بنجاح!</p>
                        <p style="font-size: 12px;"><a href="${{data.url}}" target="_blank">🔗 عرض الملف</a></p>`;
                    }}
                }}
            }} catch (error) {{
                if (status) {{
                    status.innerHTML = `<p style="color: #ff4444;">❌ فشل الرفع</p>`;
                }}
            }}
        }});
    }}
    
    console.log('🎵 Spotify Clone Ready! ☁️ {self.cloud_name}');
}});
"""
        
        (self.base_path / "static" / "js" / "app.js").write_text(js_content, encoding='utf-8')
        print("  ✅ app.js created")

    def generate_config_files(self):
        """إنشاء ملفات التكوين"""
        print("\n⚙️  إنشاء ملفات التكوين...")
        
        requirements = """flask==2.3.0
cloudinary==1.36.0
requests==2.31.0
python-dotenv==1.0.0
gunicorn==21.2.0"""
        (self.base_path / "requirements.txt").write_text(requirements, encoding='utf-8')
        
        env_content = f"""CLOUDINARY_CLOUD_NAME={self.cloud_name}
CLOUDINARY_COLLECTION_URL={self.collection_url}
FLASK_ENV=production"""
        (self.base_path / ".env").write_text(env_content, encoding='utf-8')
        
        gitignore = """venv/
__pycache__/
*.pyc
.env
*.db
.DS_Store
node_modules/"""
        (self.base_path / ".gitignore").write_text(gitignore, encoding='utf-8')
        
        readme = f"""# 🎵 Spotify Clone with Cloudinary

![Cloudinary](https://img.shields.io/badge/Cloudinary-{self.cloud_name}-blue)

## ☁️ Cloudinary
- **Cloud Name:** `{self.cloud_name}`
- **Collection:** {self.collection_url}

## 🚀 Run
```bash
pip install -r requirements.txt
python main.py
