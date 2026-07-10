import re
from funasr import AutoModel

from voice.stt.base import BaseSTT


class SenseVoiceSTT(BaseSTT):

    def __init__(self):

        print("Loading SenseVoice...")

        self.model = AutoModel(
            model="iic/SenseVoiceSmall",
            trust_remote_code=True,
            device="cpu"
        )

        print("SenseVoice Ready.")

    def transcribe(self, audio_path):

        result = self.model.generate(
            input=audio_path,
            batch_size_s=300
        )

        if not result:
            return ""

        text = result[0].get("text", "")

        # Remove SenseVoice tags like <|HAPPY|>, <|Speech|>, etc.
        text = re.sub(r"<\|.*?\|>", "", text)

        return text.strip()