from core.assistant import ArnavAssistant
from voice.speech.voice_manager import VoiceManager

assistant = ArnavAssistant()

voice = VoiceManager(assistant)

voice.start()