from core.intent import IntentDetector
from core.router import CommandRouter    
from memory.memory_manager import MemoryManager     
from skills.skill_manager import SkillManager
from skills.memory_skill import MemorySkill 
from skills.conversation_skill import ConversationSkill

class Brain:
    def __init__(self):
        
        self.intent = IntentDetector()
        self.router = CommandRouter()
        self.memory = MemoryManager()
        self.skill_manager = SkillManager()
        
        self.skill_manager.register(MemorySkill(self.memory))
        self.skill_manager.register(ConversationSkill())    
        
    def think(self, user_input):
        self.memory.short.add("user", user_input)
        
        response = self.skill_manager.execute(user_input)

        if response:
            self.memory.short.add("assistant", response)
            return response
        
        intent = self.intent.detect(user_input)
        response =  self.router.execute(intent)
        
        self.memory.short.add("assistant", response)
        
        print(self.memory.short.get())
        
        return response
        
    