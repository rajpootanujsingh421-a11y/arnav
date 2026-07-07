from core.prompt_builder import PromptBuilder
from memory.memory_manager import MemoryManager
from personality.personality import Personality
from core.context import ContextEngine

memory = MemoryManager()
personality = Personality()
context = ContextEngine(memory)

builder = PromptBuilder(memory, personality, context)

print(builder.build("What is Artificial Intelligence?"))