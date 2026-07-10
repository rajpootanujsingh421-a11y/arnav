import sounddevice as sd
import soundfile as sf


class Recorder:

    def __init__(self,
                samplerate=16000,
                channels=1):

        self.samplerate = samplerate
        self.channels = channels

    def record(self,
                duration=4,
                filename="voice/audio/input.wav"):

        print("🎤 Listening... Speak now...")

        audio = sd.rec(
            int(duration * self.samplerate),
            samplerate=self.samplerate,
            channels=self.channels,
            dtype="float32"
        )

        sd.wait()

        sf.write(
            filename,
            audio,
            self.samplerate
        )

        print("✅ Audio Saved:", filename)

        return filename