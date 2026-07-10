from abc import ABC, abstractmethod


class BaseSTT(ABC):

    @abstractmethod
    def transcribe(self, audio_path: str):
        pass