class MemoryExtractor:
    def extract(self, text: str):
        
        text = text.lower()
        
        if "my favorite language is" in text:
            value = text.replace("my favorite language is", "").strip()
            return ("favorite_language", value)
        if "i live in" in text:
            value = text.replace("i live in", "").strip()
            return ("city", value)
        if "my goal is" in text:
            value = text.replace("my goal", value)
            
        return None