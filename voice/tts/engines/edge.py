import asyncio
import edge_tts


class EdgeTTS:

    def __init__(self):

        self.voice = "hi-IN-SwaraNeural"
        self.rate = "+0%"
        self.pitch = "+0Hz"

    async def _generate(self, text, output):

        communicate = edge_tts.Communicate(
            text=text,
            voice=self.voice,
            rate=self.rate,
            pitch=self.pitch
        )

        await communicate.save(output)

    def generate(self, text, output="voice/audio/output.mp3"):

        asyncio.run(
            self._generate(text, output)
        )

        return output