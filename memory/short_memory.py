class ShortMemory:
    
    def __init__(self):
        self.messages = []

    def add(self, role: str, content: str):

        self.messages.append({
            "role": role,
            "content": content
        })

        # Sirf last 20 messages rakho
        if len(self.messages) > 20:
            self.messages.pop(0)

    def get(self):
        return self.messages

    def clear(self):
        self.messages.clear()