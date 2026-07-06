from core.intent import IntentDetector
from core.router import CommandRouter    
from memory.memory_manager import MemoryManager   

class Brain:
    def __init__(self):
        
        self.intent = IntentDetector()
        self.router = CommandRouter()
        self.memory = MemoryManager()
        
    def think(self, user_input):
        
        self.memory.short.add("user", user_input)
        
        intent = self.intent.detect(user_input)
        
        response =  self.router.execute(intent)
        
        self.memory.short.add("assistant", response)
        print(self.memory.short.get())
        
        return response
        
    