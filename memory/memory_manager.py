from memory.short_memory import ShortMemory
from memory.long_memory import LongMemory
from memory.emotional_memory import EmotionalMemory


class MemoryManager:

    def __init__(self):

        self.short = ShortMemory()
        self.long = LongMemory()
        self.emotional = EmotionalMemory()
        
    def save(self, memories):
    
        for memory in memories:

            memory_type = memory.get("type")
            key = memory.get("key")
            value = memory.get("value")

            if memory_type in ("identity", "preference"):

                self.long.save(key, value)

            elif memory_type == "emotion":

                self.emotional.save(key, value)

            else:

                self.short.save(key, value)
        
    def get(self, key):
    
        value = self.long.load(key)

        if value is not None:
            return value

        value = self.short.load(key)

        if value is not None:
            return value

        return self.emotional.load(key)
    
    def save_name(self, name):
        self.long.save("name", name)
        
    def get_name(self):
        return self.long.load("name")
        
    def forget_name(self):
        self.long.delete("name")    