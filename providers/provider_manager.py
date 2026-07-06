from providers.openai_provider import OpenAIProvider


class ProviderManager:

    def __init__(self):
        self.provider = OpenAIProvider()

    def ask(self, prompt: str):

        return self.provider.generate(prompt)