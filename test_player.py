from voice.tts_engine import TTSEngine
from voice.audio_player import AudioPlayer

tts = TTSEngine()
player = AudioPlayer()

audio = tts.generate(
    "Hello Anuj. I am Arnav."
)

player.play(audio)