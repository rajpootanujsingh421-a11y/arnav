class EmotionalMemory:
    
    def __init__(self):
        self.preferences = {}

    def remember(self, key, value):
        self.preferences[key] = value

    def recall(self, key):
        return self.preferences.get(key)