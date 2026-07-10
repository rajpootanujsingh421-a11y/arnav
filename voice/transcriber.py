from faster_whisper import WhisperModel


class Transcriber:

    def __init__(self):

        print("Loading Whisper Model...")

        self.model = WhisperModel(  
            "medium",
            device="cpu",
            compute_type="int8"
        )

        print("Whisper Ready.")

    def transcribe(self, audio_path):
    
        segments, info = self.model.transcribe(
        audio_path,
        beam_size=5,
        vad_filter=True,
        language="hi",
        condition_on_previous_text=False
        )

        text = ""

        for segment in segments:
            text += segment.text

        return text.strip()