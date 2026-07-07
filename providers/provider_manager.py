from providers.gemini_provider import GeminiProvider
from providers.offline_provider import OfflineProvider


class ProviderManager:

    def __init__(self):
        self.gemini = GeminiProvider()
        self.offline = OfflineProvider()

    def generate(self, prompt: str):

        try:
            return self.gemini.generate(prompt)

        except Exception as e:
            print(f"[Provider Error] {e}")

            return self.offline.generate(prompt)