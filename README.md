# 🎥 Movie Subtitle Translator (تعريب الأفلام)

A modern web app to **translate `.srt` subtitle files** into Arabic and 20+ world languages with a sleek interface, real-time progress bar, and automatic download. Built using Python Flask, Bootstrap, and JavaScript.

---

## Link to translate:
https://subtitle-arabic-maker.onrender.com/

---

## 📊 Features

* 🌐 Translate subtitles between 20+ languages
* 📁 Upload `.srt` files
* ⏳ See real-time progress with percent tracker
* 🎞 Arabic-first RTL interface with language switch
* 🔄 Download translated subtitle instantly
* 🤝 Compatible with AI-based translation APIs (OpenAI, Google, etc.)

---

## 📆 Demo Screenshot

![App Screenshot](screenshots/demo.png)

---

## ♻ Folder Structure

```
project-root/
├── app.py                  # Flask backend
├── templates/
│   └── index.html          # HTML UI
├── static/                # CSS / icons / images (optional)
├── uploads/               # Translated output folder
├── requirements.txt       # Python dependencies
└── README.md
```

---

## 💻 Setup Instructions

### 1. Clone the repository:

```bash
git clone https://github.com/yourusername/movie-subtitle-translator.git
cd movie-subtitle-translator
```

### 2. Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Run the Flask app:

```bash
python app.py
```

Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 🌍 Supported Languages

You can translate between any of these:

* Arabic (العربية)
* English (English)
* Chinese (中文)
* Hindi (हिन्दी)
* Spanish (Español)
* French (Français)
* Bengali (বাংলা)
* Russian (Русский)
* Portuguese (Português)
* Urdu (اردو)
* Indonesian (Bahasa Indonesia)
* German (Deutsch)
* Japanese (日本語)
* Turkish (Türkçe)
* Vietnamese (Tiếng Việt)
* Korean (한국어)
* Tamil (தமிழ்)
* Persian (فارسی)
* Swahili (Kiswahili)
* Marathi (मराठी)

---

## 🛡 Security

* Only `.srt` files are accepted
* Uses secure file handling and file renaming
* File size limited to 2MB (can be configured in `app.py`)

---

## 🎉 Credits

Built by \[Your Name].

UI inspired by Netflix style. Open for contribution!

---

## 🌟 License

MIT License - feel free to fork, modify, and contribute.

---

## ✨ To-Do (Suggestions)

* [ ] Add automatic language detection
* [ ] Add full multilingual UI (RTL & LTR)
* [ ] Support for `.vtt` files
* [ ] Dockerize for easier deployment
* [ ] Deploy to Render or Railway

---

> © 2025 تعريب الأفلام. كل الحقوق محفوظة.
