from providers.provider_manager import ProviderManager

provider = ProviderManager()

response = provider.generate("Hello Arnav")

print(response)