class ResponseValidator:
    
    def validate(self, response: str):

        if not response:
            return "Sorry, I couldn't generate a response."

        replacements = {
            "As an AI language model": "As Arnav",
            "As an AI": "As Arnav",
            "I am Gemini": "I am Arnav",
            "I'm Gemini": "I'm Arnav",
            "Google AI": "Arnav",
            "language model": "assistant"
        }

        for old, new in replacements.items():
            response = response.replace(old, new)

        return response