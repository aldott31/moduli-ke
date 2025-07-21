from google.cloud.speech_v2 import SpeechClient
from google.cloud.speech_v2.types import cloud_speech

# TODO(developer): Update and un-comment below line
# PROJECT_ID = "your-project-id"

# Instantiates a client
client = SpeechClient()

# Reads a file as bytes
with open("C:\\Users\\HELLO\\OneDrive - Universiteti Metropolitan Tirana\\Desktop\\audio_module\\bruno.wav", "rb") as f:
    audio_content = f.read()

config = cloud_speech.RecognitionConfig(
    auto_decoding_config=cloud_speech.AutoDetectDecodingConfig(),
    language_codes=["sq-AL"],
    model="long",
)

request = cloud_speech.RecognizeRequest(
    recognizer=f"projects/{'august-vine-466609-v0'}/locations/global/recognizers/_",
    config=config,
    content=audio_content,
)

# Transcribes the audio into text
response = client.recognize(request=request)

for result in response.results:
    print(f"Transcript: {result.alternatives[0].transcript}")
