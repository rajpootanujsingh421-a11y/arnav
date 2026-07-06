from providers.base_provider import BaseProvider


class OpenAIProvider(BaseProvider):

    def generate(self, prompt: str) -> str:
        return f"[OpenAI] {prompt}"