import soundfile as sf
from kokoro_onnx import Kokoro

kokoro = Kokoro(
    "models/kokoro/kokoro-v1.0.int8.onnx",
    "models/kokoro/voices-v1.0.bin"
)

text = input("You : ")

samples, sample_rate = kokoro.create(
    text=text,
    voice="af_sarah",
    speed=1.0,
    lang="en-us"
)

sf.write("output.wav", samples, sample_rate)

print("✅ Audio Generated : output.wav")