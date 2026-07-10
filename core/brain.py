from core.intent import IntentDetector
from core.router import CommandRouter    
from memory.memory_manager import MemoryManager     
from skills.skill_manager import SkillManager
from skills.memory_skill import MemorySkill 
from skills.conversation_skill import ConversationSkill
from skills.system_skill import SystemSkill
from skills.emotion_skill import EmotionSkill
from skills.memory_inspector_skill import MemoryInspectorSkill
from core.context import ContextEngine
from providers.provider_manager import ProviderManager
from core.prompt_builder import PromptBuilder
from personality.personality import Personality
from core.validator import ResponseValidator
from memory.extractor import MemoryExtractor
from core.thinking_engine import ThinkingEngine
from core.response_parser import ResponseParser
from skills.automation_skill import AutomationSkill

class Brain:
    def __init__(self):
        
        self.intent = IntentDetector()
        self.router = CommandRouter()           
        self.memory = MemoryManager()
        self.context = ContextEngine(self.memory)
        self.provider = ProviderManager()
        self.skill_manager = SkillManager()
        self.personality = Personality()
        self.prompt_builder = PromptBuilder(
            self.memory,
            self.personality,
            self.context
        )
        self.validator = ResponseValidator()
        self.extractor = MemoryExtractor()  
        self.thinking = ThinkingEngine(self) 
        self.response_parser = ResponseParser()   
        
        self.skill_manager.register(MemorySkill(self.memory))
        self.skill_manager.register(ConversationSkill(self.memory))
        self.skill_manager.register(AutomationSkill())
        self.skill_manager.register(SystemSkill())
        self.skill_manager.register(EmotionSkill(self.memory))
        self.skill_manager.register(MemoryInspectorSkill(self.memory))
        

    def think(self, user_input):
    
        self.memory.short.add("user", user_input)

        memories = self.extractor.extract(user_input)

        if memories:
            self.memory.save(memories)
            
        response = self.skill_manager.execute(user_input)
        
        if response is not None:
            return response
        
        response = self.thinking.think(user_input)

        return response