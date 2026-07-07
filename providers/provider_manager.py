from providers.offline_provider import OfflineProvider

class ProviderManager:

    def __init__(self):
        self.provider = OfflineProvider()

    def generate(self, prompt: str):
        return self.provider.generate(prompt)