import soundfile as sf
from kokoro_onnx import Kokoro

from voice.tts.base import BaseTTS


class KokoroTTS(BaseTTS):

    def __init__(self):

        print("Loading Kokoro TTS...")

        self.kokoro = Kokoro(
            "models/kokoro/kokoro-v1.0.int8.onnx",
            "models/kokoro/voices-v1.0.bin" 
        )

        self.voice = "af_sarah"
        self.speed = 0.9
        self.language = "en-us"

        print("Kokoro Ready.")

    def speak(self, text: str):

        samples, sample_rate = self.kokoro.create(
            text=text,
            voice=self.voice,
            speed=self.speed,
            lang=self.language
        )

        output_path = "voice/audio/output.wav"

        sf.write(output_path, samples, sample_rate)

        return output_path