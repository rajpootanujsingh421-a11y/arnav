from providers.base_provider import BaseProvider


class OfflineProvider(BaseProvider):

    def generate(self, prompt: str):

        return "I am currently running in offline mode."