# stt.py

import whisper
import tempfile
import sounddevice as sd
import numpy as np
import scipy.io.wavfile

def recognize_speech(duration=5, fs=16000, language=None):
    try:
        print("🎤 Recording...")
        audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
        sd.wait()

        if np.abs(audio).mean() < 10:
            print("🛑 Silent input.")
            return ""

        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
            scipy.io.wavfile.write(f.name, fs, audio)

            model = whisper.load_model("tiny")  # Use 'tiny' or 'base' for CPU

            # Auto language detection or manually set it
            options = {"fp16": False}
            if language:
                options["language"] = language
            result = model.transcribe(f.name, **options)

            return result["text"].strip()

    except Exception as e:
        print(f"[STT ERROR]: {e}")
        return ""
