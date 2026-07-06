class MemorySkill:
    
    def __init__(self, memory):
        self.memory = memory
        
    def handle(self, user_input):
        
        text = user_input.strip()
        lower = text.lower()
        
        if lower.startswith("my name is "):
                name = text[11:].strip()
                self.memory.save_name(name)
                return f"Nice to meet you, {name}! I'll remember your name."
            
        elif lower == "what is my name":
            name = self.memory.get_name()
            
            if name:
                return f"Your name is {name}."
            return "I don't know your name yet."
        elif lower == "forget my name":
            self.memory.forget_name()
            
            return "Okay, I've forgotten your name."
        
        return None
        