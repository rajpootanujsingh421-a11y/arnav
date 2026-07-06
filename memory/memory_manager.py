from memory.short_memory import ShortMemory
from memory.long_memory import LongMemory
from memory.emotional_memory import EmotionalMemory


class MemoryManager:

    def __init__(self):

        self.short = ShortMemory()
        self.long = LongMemory()
        self.emotional = EmotionalMemory()