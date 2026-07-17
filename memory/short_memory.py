class ShortMemory:
    
    def __init__(self):

        self.messages = []
        self.data = {}

    # Conversation Memory
    def add(self, role: str, content: str):

        self.messages.append({
            "role": role,
            "content": content
        })

        if len(self.messages) > 20:
            self.messages.pop(0)

    def get(self):
        return self.messages

    def clear(self):
        self.messages.clear()

    # Temporary Key-Value Memory

    def save(self, key, value):

        self.data[key] = value

    def load(self, key):

        return self.data.get(key)

    def delete(self, key):

        if key in self.data:
            del self.data[key]