from voice.tts_engine import TTSEngine

tts = TTSEngine()

path = tts.generate(
    "Hello Anuj. I am Arnav."
)

print(path)