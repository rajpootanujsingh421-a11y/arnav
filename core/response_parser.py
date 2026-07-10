class ResponseParser:
    def parse(self, response):
        return {
            "response": response,
            "memory": None,
            "action": None,
            "emotion": None
        }