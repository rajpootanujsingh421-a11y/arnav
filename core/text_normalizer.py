import re

class TextNormalizer:
    def normalize(self, text: str):
        text = text.lower().strip()
        
        text = re.sub(r"\s+", " ", text)
        
        text = re.sub(r"[!?.,]", "", text)
        
        filler_words = [

            "please",
            "pls",
            "plz",
            "bro",
            "buddy",

        ]

        for word in filler_words:

            text = re.sub(rf"\b{re.escape(word)}\b", "", text)
            
            
        wake_words = [

            "arnav",

        ]

        for word in wake_words:

            text = re.sub(rf"\b{re.escape(word)}\b", "", text)
            
        text = re.sub(r"\s+", " ", text).strip()
        
        return text