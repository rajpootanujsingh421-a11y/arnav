from memory.extractor import MemoryExtractor
from memory.memory_manager import MemoryManager

extractor = MemoryExtractor()
manager = MemoryManager()

text = "Mera naam Anuj hai"

memories = extractor.extract(text)

manager.save(memories)

print(manager.get("name"))