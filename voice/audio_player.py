import pygame
import time
from pathlib import Path


class AudioPlayer:

    def __init__(self):
        pygame.mixer.init()
    def play(self, audio_path):

        audio_path = Path(audio_path)
        
        if not audio_path.exists():
            print(f"❌ Audio not found: {audio_path}")
            return

        pygame.mixer.music.load(str(audio_path))
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
        
        pygame.mixer.music.unload()