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

        
        if lower.startswith("mera naam "):
            
            if "kya hai" in lower:
                return None

            name = text[10:].strip()

            if name.lower().endswith("hai"):
                name = name[:-3].strip()

            self.memory.save_name(name)

            return f"Theek hai! Main yaad rakhunga ki tumhara naam {name} hai."


        if lower in [
            "what is my name",
            "who am i",
            "mera naam kya hai",
            "mera naam kya hai?"
        ]:

            name = self.memory.get_name()

            if name:
                return f"Your name is {name}."

            return "I don't know your name yet."

        if lower in [
            "what do i like",
            "mujhe kya pasand hai"
        ]:

            likes = self.memory.get("likes")

            if likes:
                return f"You like {likes}."

            return "I don't know your preferences yet."

    
        if lower in [
            "forget my name",
            "mera naam bhool jao"
        ]:

            self.memory.forget_name()

            return "Okay, I've forgotten your name."

        return None