from faster_whisper import WhisperModel

from voice.stt.base import BaseSTT


class WhisperSTT(BaseSTT):

    def __init__(self):

        print("Loading Whisper Model...")

        self.model = WhisperModel(
            "small",
            device="cpu",
            compute_type="int8"
        )

        print("Whisper Ready.")

    def transcribe(self, audio_path: str):

        segments, info = self.model.transcribe(
            audio_path,
            beam_size=5,
            vad_filter=True,
            condition_on_previous_text=False
        )

        text = ""

        for segment in segments:
            text += segment.text

        return text.strip()