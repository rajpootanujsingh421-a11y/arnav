from memory.short_memory import ShortMemory
from memory.long_memory import LongMemory
from memory.emotional_memory import EmotionalMemory


class MemoryManager:

    def __init__(self):

        self.short = ShortMemory()
        self.long = LongMemory()
        self.emotional = EmotionalMemory()
        
    def save_name(self, name):
        self.long.save("name", name)
        
    def get_name(self):
        return self.long.load("name")
        
    def forget_name(self):
        self.long.delete("name")