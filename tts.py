# tts.py

from gtts import gTTS
import os
from pydub import AudioSegment
from pydub.playback import play
import tempfile

def speak(text, language="en"):
    try:
        tts = gTTS(text=text, lang=language)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
            tts.save(f.name)
            audio = AudioSegment.from_file(f.name, format="mp3")
            play(audio)
    except Exception as e:
        print(f"[TTS ERROR]: {e}")
