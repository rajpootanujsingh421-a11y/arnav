from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    APP_NAME = "Arnav"
    VERSION = "0.4.0"
    STATUS = "ONLINE"
    
    OWNER = "Anuj"

    MEMORY_FILE = "data/memory.json"
    MAX_SHORT_MEMORY = 20

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    AI_MODEL = "gemini-2.5-flash"
    
    DEFAULT_LANGUAGE = "Hindi"
    ENABLE_EMOJIS = True
    
    VOICE_SAMPLE_RATE = 16000
    VOICE_CHANNELS = 1
    VOICE_RECORD_SECONDS = 5

    WHISPER_MODEL = "base"
    WHISPER_DEVICE = "cpu"
    WHISPER_COMPUTE_TYPE = "int8"

    VOICE_LANGUAGE = "hi"

    WAKE_WORD = "arnav"
    
    DEBUG = False