from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    APP_NAME = "Arnav"
    VERSION = "0.1.0"
    STATUS = "ONLINE"

    MEMORY_FILE = "data/memory.json"
    MAX_SHORT_MEMORY = 20

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")