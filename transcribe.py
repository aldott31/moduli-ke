import os
os.environ["PATH"] += os.pathsep + "C:\\ffmpeg\\bin"
import whisper

def transcribe_audio(file_path):
    model = whisper.load_model("base")  # ose "tiny", "medium", "large"
    result = model.transcribe(file_path, language="sq")
    print(f"[TRANSKRIPT për {file_path}]:\n", result["text"])

    # Ruaj transcript në .txt me të njëjtin emër
    txt_path = file_path.replace(".wav", ".txt")
    try:
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(result["text"])
        print(f"[SUKSESES] Transcript u ruajt te: {txt_path}")
    except Exception as e:
        print(f"[ERROR] Nuk mund të ruaj transcript për {file_path} → {e}")

if __name__ == "__main__":
    audio_folder = "recordings"
    if not os.path.exists(audio_folder):
        print("[ERROR] Nuk ekziston folderi recordings/")
    else:
        for filename in os.listdir(audio_folder):
            if filename.lower().endswith(".wav"):
                filepath = os.path.join(audio_folder, filename)
                transcribe_audio(filepath)
