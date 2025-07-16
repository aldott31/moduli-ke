import sounddevice as sd
from scipy.io.wavfile import write
import os

def record_audio(duration_sec=30, filename="meeting_ke.wav"):
    fs = 44100  # frekuenca e mostrimit
    recordings_dir = "recordings"
    os.makedirs(recordings_dir, exist_ok=True)
    filepath = os.path.join(recordings_dir, filename)

    print(f"[INFO] Filloi regjistrimi për {duration_sec} sekonda...")
    audio_data = sd.rec(int(duration_sec * fs), samplerate=fs, channels=2)
    sd.wait()
    write(filepath, fs, audio_data)
    print(f"[INFO] Audio u ruajt te: {filepath}")

if __name__ == "__main__":
    record_audio(duration_sec=30, filename="meeting_ke.wav")
