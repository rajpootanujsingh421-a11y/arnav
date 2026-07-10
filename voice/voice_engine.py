from voice.recorder import Recorder
from voice.stt.manager import STTManager


class VoiceEngine:

    def __init__(self):

        self.recorder = Recorder()
        self.stt = STTManager()

    def listen(self):

        audio = self.recorder.record()

        text = self.stt.transcribe(audio)

        return text