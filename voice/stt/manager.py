from voice.stt.engines.sensevoice import SenseVoiceSTT
from voice.stt.engines.whisper import WhisperSTT


class STTManager:
    
    def __init__(self):

        self.sense = SenseVoiceSTT()
        self.whisper = WhisperSTT()

        self.primary = "whisper"

    def transcribe(self, audio_path):

        try:

            if self.primary == "sense":
                return self.sense.transcribe(audio_path)

            return self.whisper.transcribe(audio_path)

        except Exception as e:

            print(f"[STT] SenseVoice Error: {e}")

            print("Switching to Whisper...")

            return self.whisper.transcribe(audio_path)