from voice.tts.manager import TTSManager

from voice.audio_player import AudioPlayer


class Speaker:

    def __init__(self):

        self.tts = TTSManager()
        self.player = AudioPlayer()

    def speak(self, text):

        audio = self.tts.generate(text)
        self.player.play(audio)