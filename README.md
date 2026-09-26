# Vocal-Gen

A simple, clean, and free text-to-speech web application built with Django and Python.

Vocal-Gen lets users enter text, choose a voice, generate speech, listen to the result directly in the browser, and download the generated audio as an MP3 file.

## ✨ Features

- 📝 Convert text into speech
- 🎙️ Multiple voices and languages
- 🔊 Listen to generated audio directly in the browser
- ⬇️ Download generated speech as an MP3 file
- 🆓 Free to use
- 🔐 No user account required
- 📱 Responsive interface for desktop and mobile
- 🐍 Built with Django and Python
- 🎨 Simple frontend using HTML and CSS
- 🚫 No eSpeak/eSpeak-NG installation required
- 🚫 No FFmpeg installation required

## 🌍 Supported Languages

Vocal-Gen currently includes voices for:

- English
- English (US)
- English (UK)
- English (Australia)
- English (India)
- Hindi
- Tamil
- Telugu
- Malayalam
- Kannada
- Bengali
- French
- German
- Spanish
- Italian
- Portuguese

The available voices are provided through the text-to-speech service used by the application.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web framework |
| HTML | Page structure |
| CSS | Styling and responsive design |
| edge-tts | Text-to-speech generation |
| SQLite | Default Django database |

## 📁 Project Structure

```text
vocal-gen/
├── manage.py
├── requirements.txt
├── README.md
├── LICENSE
│
├── text_to_voice/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── tts/
│   ├── __init__.py
│   ├── apps.py
│   ├── urls.py
│   ├── views.py
│   └── services.py
│
├── templates/
│   └── tts/
│       └── index.html
│
├── static/
│   └── tts/
│       └── style.css
│
└── media/
    └── voice/
```

## 🚀 Getting Started

### Prerequisites

Make sure you have:

- Python 3.9 or newer
- pip
- An active internet connection

You do **not** need to install eSpeak, eSpeak-NG, FFmpeg, or any other system-level speech software.

### 1. Clone the repository

```bash
git clone https://github.com/NandhuT17/vocal-gen.git
cd vocal-gen
```

Replace the repository URL with your GitHub repository URL.

### 2. Create a virtual environment

#### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

## 🔊 How It Works

The basic workflow is:

```text
User enters text
       ↓
Selects a voice
       ↓
Django receives the request
       ↓
Python generates the speech
       ↓
MP3 audio is saved
       ↓
Browser plays the audio
       ↓
User can download the MP3
```

The application uses the `edge-tts` Python package for speech generation.

An internet connection is required when generating audio.

## ⚙️ Configuration

Important settings are located in:

```text
text_to_voice/settings.py
```

For example, the maximum text length can be configured with:

```python
MAX_TEXT_LENGTH = 5000
```

The default media directory is:

```text
media/
```

Generated audio files are stored in:

```text
media/voice/
```

## 🔒 Security Notes

This project is intended to be a simple and educational text-to-speech application.

Before deploying it publicly, consider adding:

- Rate limiting
- Request throttling
- Strong production `SECRET_KEY`
- Proper `ALLOWED_HOSTS`
- HTTPS
- Production WSGI/ASGI configuration
- Automatic cleanup of generated audio files
- File-size and request limits
- Abuse protection
- Proper production media storage

Do not use the development server for production.

## 🌐 Internet Requirement

Vocal-Gen uses `edge-tts` to generate speech, so an internet connection is required for speech generation.

The application does not require a separate API key.

## 🧹 Generated Audio

Generated MP3 files are stored locally in:

```text
media/voice/
```

If the application is deployed publicly, you should consider implementing automatic cleanup of old audio files to prevent unnecessary disk usage.

## 🤝 Contributing

Contributions are welcome!

If you'd like to improve Vocal-Gen:

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature/your-feature
```

3. Make your changes.
4. Commit your changes.

```bash
git add .
git commit -m "Add your feature"
```

5. Push your branch.

```bash
git push origin feature/your-feature
```

6. Open a Pull Request.

## 🐛 Issues

If you find a bug or have a feature request, please open an issue in the GitHub repository with:

- A clear description of the problem
- Steps to reproduce it
- Expected behavior
- Actual behavior
- Relevant error messages or screenshots

## 📄 License

This project is licensed under the **MIT License**.

You are free to use, modify, distribute, and sublicense the software, subject to the conditions of the MIT License.

See the [`LICENSE`](LICENSE) file for the complete license text.

## ⭐ Support

If you find the project useful, consider giving the repository a ⭐ on GitHub.

---

Built with Python, Django, HTML, and CSS.
