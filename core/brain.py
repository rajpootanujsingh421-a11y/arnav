from core.intent import IntentDetector
from core.router import CommandRouter    
from memory.memory_manager import MemoryManager     
from skills.skill_manager import SkillManager
from skills.memory_skill import MemorySkill 
from skills.conversation_skill import ConversationSkill
from skills.system_skill import SystemSkill
from skills.emotion_skill import EmotionSkill
from skills.memory_inspector_skill import MemoryInspectorSkill
from providers.provider_manager import ProviderManager
from core.prompt_builder import PromptBuilder
from personality.personality import Personality
from core.validator import ResponseValidator
from memory.extractor import MemoryExtractor
from core.thinking_engine import ThinkingEngine
from core.response_parser import ResponseParser
from skills.automation_skill import AutomationSkill
from agent.planner import Planner
from agent.executor import Executor
from agent.local_planner import LocalPlanner
from brain.offline_brain import OfflineBrain
from conversation.detector import ConversationDetector
from skills.skill_router import SkillRouter
from core.context_engine import ContextEngine
from core.context_resolver import ContextResolver

class Brain:
    def __init__(self):

        self.intent = IntentDetector()
        self.router = CommandRouter()
        self.memory = MemoryManager()
        self.provider = ProviderManager()
        self.skill_manager = SkillManager()
        self.skill_router = SkillRouter()
        self.personality = Personality()
        self.context = ContextEngine()
        self.context_resolver = ContextResolver(
            self.context
        )
        self.prompt_builder = PromptBuilder(
            self.memory,
            self.personality,
            self.context
        )

        self.validator = ResponseValidator()
        self.extractor = MemoryExtractor()
        self.thinking = ThinkingEngine(self)
        self.response_parser = ResponseParser()
        self.detector = ConversationDetector()
        self.offline = OfflineBrain(self.memory)
        self.planner = Planner(self)
        self.local_planner = LocalPlanner()
        self.executor = Executor()

        # Skills
        conversation = ConversationSkill(self.memory)

        self.skill_manager.register(
            MemorySkill(self.memory)
        )

        self.skill_manager.register(
            conversation
        )

        self.skill_manager.register(
            AutomationSkill()
        )

        self.skill_manager.register(
            SystemSkill()
        )

        self.skill_manager.register(
            EmotionSkill(self.memory)
        )

        self.skill_manager.register(
            MemoryInspectorSkill(self.memory)
        )

        # Skill Router
        self.skill_router.register(
            "greeting",
            conversation
        )

        self.skill_router.register(
            "good_morning",
            conversation
        )

        self.skill_router.register(
            "good_afternoon",
            conversation
        )

        self.skill_router.register(
            "good_evening",
            conversation
        )

        self.skill_router.register(
            "good_night",
            conversation
        )

        self.skill_router.register(
            "goodbye",
            conversation
        )

        self.skill_router.register(
            "status",
            conversation
        )

        self.skill_router.register(
            "thanks",
            conversation
        )

        self.skill_router.register(
            "identity",
            conversation
        )

        self.skill_router.register(
            "creator",
            conversation
        )

    def think(self, user_input):
    
        self.memory.short.add("user", user_input)

        memories = self.extractor.extract(user_input)

        if memories:

            self.memory.save(memories)

            m = memories[0]

            key = m["key"]
            value = m["value"]

            replies = {

                "name":
                    f"Nice to meet you, {value}! I'll remember your name.",

                "age":
                    f"Got it! I'll remember that you're {value} years old.",

                "city":
                    f"Okay! I'll remember that you live in {value}.",

                "goal":
                    f"Awesome! I'll remember your goal: {value}.",

                "dream":
                    f"I'll remember your dream: {value}.",

                "profession":
                    f"Got it! I'll remember that you're a {value}.",

                "likes":
                    f"I'll remember that you like {value}.",

            }

            if key in replies:

                self.memory.short.add(
                    "assistant",
                    replies[key]
                )

                return replies[key]

        response = self.thinking.think(user_input)

        return response