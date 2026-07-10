class AutomationParser:
    
    def parse(self, text):

        text = text.lower().strip()

        if "chrome" in text:
            return ("app", "chrome")

        if "notepad" in text:
            return ("app", "notepad")

        if "calculator" in text or "calc" in text:
            return ("app", "calculator")
        
        if "paint" in text:
            return ("app", "paint")

        if "google" in text and "search" not in text:
            return ("browser", "google")

        if "youtube" in text and "search" not in text:
            return ("browser", "youtube")

        return None