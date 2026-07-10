import re


class LanguageDetector:

    def detect(self, text: str) -> str:

        if not text:
            return "unknown"

        # Hindi Unicode
        if re.search(r'[\u0900-\u097F]', text):
            return "hindi"

        english_words = sum(word.isascii() for word in text.split())

        if english_words == len(text.split()):
            return "english"

        return "hinglish"