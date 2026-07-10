from memory.extractor import MemoryExtractor
from memory.memory_manager import MemoryManager

extractor = MemoryExtractor()
manager = MemoryManager()

text = "Mera naam Anuj hai"

memory = extractor.extract(text)

manager.save(memory)

print("Saved Successfully")