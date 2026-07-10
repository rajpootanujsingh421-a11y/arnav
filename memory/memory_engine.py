import json
from memory.schema import MemorySchema

class MemoryEngine:
    
    def __init__(self, provider, memory):
        self.provider = provider
        self.memory = memory
        
    def learn(self, user_input: str):
        return