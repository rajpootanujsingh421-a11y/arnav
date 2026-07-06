from providers.base_provider import BaseProvider


class LocalProvider(BaseProvider):

    def generate(self, prompt: str) -> str:
        return f"[Local AI] {prompt}"
    