# Vocaly — Django Text to Voice

A free text-to-speech website built with **Django, Python, HTML and CSS**.

## No eSpeak/eSpeak-NG required

This version does **not** require eSpeak, eSpeak-NG, FFmpeg, or any other system-level
voice program.

The server uses the Python package `edge-tts` to generate MP3 speech.

You only need Python and the Python packages in `requirements.txt`.

## Setup

### Windows

Open Command Prompt/PowerShell in this project folder:

```powershell
py -m venv .venv
.venv\Scripts\activate
py -m pip install -r requirements.txt
py manage.py migrate
py manage.py runserver
```

Then open:

http://127.0.0.1:8000/

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then open:

http://127.0.0.1:8000/

## How it works

1. User enters text.
2. Django receives the text.
3. Python's `edge-tts` package requests speech generation.
4. Django saves the generated MP3 in `media/voice/`.
5. The page provides an audio player and a free download button.

## Important

Because `edge-tts` uses an online speech service, the computer running Django needs an
internet connection when generating audio.

No API key or paid subscription is required for this project.

## Included voices

English (US), English (UK), English (Australia), English (India), Hindi, Tamil, Telugu,
Malayalam, Kannada, Bengali, French, German, Spanish, Italian and Portuguese.

## Production notes

For a public deployment, add rate limiting, input abuse protection, cleanup of old audio
files, HTTPS, a production WSGI server, and appropriate hosting/storage configuration.
