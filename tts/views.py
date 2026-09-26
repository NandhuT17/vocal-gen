from django.conf import settings
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .services import TTSError, synthesize_to_mp3


VOICES = [
    ("en", "English"),
    ("en-us", "English (US)"),
    ("en-gb", "English (UK)"),
    ("en-au", "English (Australia)"),
    ("en-in", "English (India)"),
    ("hi", "Hindi"),
    ("ta", "Tamil"),
    ("te", "Telugu"),
    ("ml", "Malayalam"),
    ("kn", "Kannada"),
    ("bn", "Bengali"),
    ("fr", "French"),
    ("de", "German"),
    ("es", "Spanish"),
    ("it", "Italian"),
    ("pt", "Portuguese"),
]


def home(request):
    return render(
        request,
        "tts/index.html",
        {
            "voices": VOICES,
            "max_length": getattr(settings, "MAX_TEXT_LENGTH", 5000),
        },
    )


@require_http_methods(["POST"])
def synthesize(request):
    text = request.POST.get("text", "")
    voice = request.POST.get("voice", "en")

    allowed_voices = {code for code, _ in VOICES}
    if voice not in allowed_voices:
        voice = "en"

    try:
        audio_path = synthesize_to_mp3(text, voice)
    except TTSError as exc:
        return render(
            request,
            "tts/index.html",
            {
                "voices": VOICES,
                "max_length": getattr(settings, "MAX_TEXT_LENGTH", 5000),
                "text": text,
                "selected_voice": voice,
                "error": str(exc),
            },
            status=400,
        )

    relative = audio_path.relative_to(settings.MEDIA_ROOT).as_posix()
    return render(
        request,
        "tts/index.html",
        {
            "voices": VOICES,
            "max_length": getattr(settings, "MAX_TEXT_LENGTH", 5000),
            "text": text,
            "selected_voice": voice,
            "audio_url": f"{settings.MEDIA_URL}{relative}",
        },
    )
