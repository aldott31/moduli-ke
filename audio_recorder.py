import sounddevice as sd
from scipy.io.wavfile import write
import os
import re

def sanitize_filename(name):
    name = name.strip().lower()
    name = name.replace(" ", "-")
    name = re.sub(r'[^a-zA-Z0-9\\-]', '', name)
    return name

def record_audio(duration_sec=30):
    fs = 44100
    channels = 1  # mono
    dtype = 'int16'  # për madhësi minimale të file-it
    recordings_dir = "recordings"
    os.makedirs(recordings_dir, exist_ok=True)

    print(f"[INFO] Filloi regjistrimi për {duration_sec} sekonda...")
    audio_data = sd.rec(int(duration_sec * fs), samplerate=fs, channels=channels, dtype=dtype)
    sd.wait()
    print(f"[INFO] Regjistrimi përfundoi.")

    raw_name = input("Si doni ta emëroni këtë audio? (shembull: mbledhje ERP marketing): ")
    clean_name = sanitize_filename(raw_name)
    filename = f"{clean_name}.wav"
    filepath = os.path.join(recordings_dir, filename)

    write(filepath, fs, audio_data)
    print(f"[INFO] Audio u ruajt te: {filepath}")

if __name__ == "__main__":
    record_audio(duration_sec=30)
