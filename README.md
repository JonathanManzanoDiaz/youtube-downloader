# Youtube Downloader - Jonathan Manzano Diaz

**Developed by:** Jonathan Manzano Diaz  
**Project Repository:** [Youtube Downloader GitHub](https://github.com/JonathanManzanoDiaz/youtube-downloader)

---

## 📌 About this Software
This program allows you to download YouTube videos and audio in different formats and qualities, using **yt-dlp** as the backend.

⚠️ **Note:** This software is intended for **personal use only**.  
You are responsible for complying with **YouTube's Terms of Service** and any applicable copyright laws in your country.

---

## 📜 End User License Agreement (EULA)

### 1. NO WARRANTY
The Software is provided **"AS IS"**, without any warranty of any kind.  
No guarantees are made regarding performance, reliability, or fitness for a particular purpose.

### 2. LIMITATION OF LIABILITY
The author shall **not be held liable** for any damages or issues arising from the use of this Software.

### 3. LEGAL RESPONSIBILITY
You are solely responsible for how you use the Software.  
Downloading copyrighted content without permission may violate local or international laws.

### 4. ACCEPTANCE
By using this Software, you agree to the above terms.  
If you do not agree, do not use the Software.

---

## ⚖️ Disclaimer
The author is **fully exempt from any and all responsibility** regarding the use of this Software.

---

## 🛠 Installation Guide

### 1. Clone this Repository
```bash
git clone https://github.com/JonathanManzanoDiaz/youtube-downloader.git
cd youtube-downloader
```

### 2. Install Dependencies
Make sure you have **Python 3.8+** installed.  
Then install the required libraries:
```bash
pip install -r requirements.txt
```

### 3. Install FFmpeg
This project requires **FFmpeg** for video/audio processing.

#### Windows
1. Download the latest FFmpeg build from: [FFmpeg official site](https://ffmpeg.org/download.html)  
   (or from [gyan.dev builds](https://www.gyan.dev/ffmpeg/builds/)).
2. Extract the folder.
3. Copy the `bin/` folder into the project directory, so you have:
   ```
   youtube-downloader/ffmpeg/bin/ffmpeg.exe
   youtube-downloader/ffmpeg/bin/ffprobe.exe
   ```
4. Alternatively, add FFmpeg to your **PATH** environment variable.

#### Linux (Debian/Ubuntu)
```bash
sudo apt update
sudo apt install ffmpeg
```

#### macOS (with Homebrew)
```bash
brew install ffmpeg
```

### 4. Run the Program
```bash
python main.py
```

---

## 🙏 Thank You
Thank you for installing and using **Youtube Downloader**!
