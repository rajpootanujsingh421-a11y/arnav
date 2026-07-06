from core.intent import IntentDetector
from core.router import CommandRouter    
from memory.memory_manager import MemoryManager  
from skills.memory_skill import MemorySkill 

class Brain:
    def __init__(self):
        
        self.intent = IntentDetector()
        self.router = CommandRouter()
        self.memory = MemoryManager()
        self.memory_skill = MemorySkill(self.memory)
        
    def think(self, user_input):
        response = self.memory_skill.handle(user_input)

        if response:
            return response
            
        text = user_input.strip()
        lower = text.lower()
        
        if lower.startswith("my name is "):
            name = text[11:].strip()
            self.memory.save_name(name)
            return f"Nice to meet you, {name}! I'll remember your name."

        if lower == "what is my name":
            name = self.memory.get_name()
            if name:
                return f"Your name is {name}."
            return "I don't know your name yet."

        if lower == "forget my name":
            self.memory.forget_name()
            return "Okay, I've forgotten your name."
        
        self.memory.short.add("user", user_input)
        
        intent = self.intent.detect(user_input)
        
        response =  self.router.execute(intent)
        
        self.memory.short.add("assistant", response)
        print(self.memory.short.get())
        
        return response
        
    