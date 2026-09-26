import asyncio
from pathlib import Path
import uuid

import edge_tts
from django.conf import settings


class TTSError(RuntimeError):
    pass


VOICES = {
    "en": "en-US-JennyNeural",
    "en-us": "en-US-JennyNeural",
    "en-gb": "en-GB-SoniaNeural",
    "en-au": "en-AU-NatashaNeural",
    "en-in": "en-IN-NeerjaNeural",
    "hi": "hi-IN-SwaraNeural",
    "ta": "ta-IN-PallaviNeural",
    "te": "te-IN-ShrutiNeural",
    "ml": "ml-IN-SobhanaNeural",
    "kn": "kn-IN-SapnaNeural",
    "bn": "bn-IN-TanishaaNeural",
    "fr": "fr-FR-DeniseNeural",
    "de": "de-DE-KatjaNeural",
    "es": "es-ES-ElviraNeural",
    "it": "it-IT-ElsaNeural",
    "pt": "pt-BR-FranciscaNeural",
}


def _generate(text: str, voice: str, output_path: Path):
    communicator = edge_tts.Communicate(text, voice)
    asyncio.run(communicator.save(str(output_path)))


def synthesize_to_mp3(text: str, voice: str = "en") -> Path:
    text = text.strip()
    if not text:
        raise TTSError("Please enter some text.")

    max_length = getattr(settings, "MAX_TEXT_LENGTH", 5000)
    if len(text) > max_length:
        raise TTSError(f"Text is too long. Maximum length is {max_length} characters.")

    selected_voice = VOICES.get(voice, VOICES["en"])

    output_dir = Path(settings.MEDIA_ROOT) / "voice"
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / f"voice_{uuid.uuid4().hex}.mp3"

    try:
        _generate(text, selected_voice, output_path)
    except Exception as exc:
        output_path.unlink(missing_ok=True)
        raise TTSError(
            "The voice could not be generated. Please check your internet connection "
            "and try again."
        ) from exc

    if not output_path.exists() or output_path.stat().st_size == 0:
        output_path.unlink(missing_ok=True)
        raise TTSError("The speech service returned an empty audio file.")

    return output_path
