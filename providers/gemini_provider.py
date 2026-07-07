from google import genai
from config import Config
from providers.base_provider import BaseProvider

class GeminiProvider(BaseProvider):
    def __init__(self):
        self.client = genai.Client(
            api_key=Config.GEMINI_API_KEY
        )
        
    def generate(self, prompt: str):
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        
        return response.text