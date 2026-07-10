from core.language import LanguageDetector

from voice.tts.engines.edge import EdgeTTS
from voice.tts.engines.kokoro import KokoroTTS


class TTSManager:

    def __init__(self):

        self.edge = EdgeTTS()
        self.kokoro = KokoroTTS()

        self.detector = LanguageDetector()

    def generate(self, text):

        language = self.detector.detect(text)

        if language == "english":
            self.edge.voice = "en-US-GuyNeural"

        else:
            self.edge.voice = "hi-IN-SwaraNeural"

        return self.edge.generate(text)