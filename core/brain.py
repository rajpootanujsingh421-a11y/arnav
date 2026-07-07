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
        
        self.skill_manager.register(MemorySkill(self.memory))
        self.skill_manager.register(ConversationSkill(self.memory))
        self.skill_manager.register(SystemSkill())
        self.skill_manager.register(EmotionSkill(self.memory))
        self.skill_manager.register(MemoryInspectorSkill(self.memory))
        
    def think(self, user_input):
        self.memory.short.add("user", user_input)
        
        last_message = self.context.get_last_message()

        if last_message:
            print("[Context]", last_message)
        
        try:
            response = self.skill_manager.execute(user_input)
            
            if response:
                self.memory.short.add("assistant", response)
                return response
        
        except Exception as e:
            print(f"[Skill Error] {e}")
            return "Oops! Something went wrong while processing your request."
        
        try:
            intent = self.intent.detect(user_input)
            response = self.router.execute(intent)
            
        except Exception as e:
            print(f"[Router Error] {e}")
            response = "Sorry, I couldn't process that request."
            
        if response == "Sorry, I don't understand that command.":
                prompt = self.prompt_builder.build(user_input)
                response = self.provider.generate(prompt)
            
        self.memory.short.add("assistant", response)

        return response
    