from providers.gemini_provider import GeminiProvider

class ProviderManager:

    def __init__(self):
        self.provider = GeminiProvider()

    def generate(self, prompt: str):
        return self.provider.generate(prompt)