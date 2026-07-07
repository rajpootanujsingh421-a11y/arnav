from config import Config

class SystemSkill:
    def handle(self, user_input):
        text = user_input.strip().lower()
        if text == "help":
            return (
                "Available Commands:\n"
                "- hello\n"
                "- time\n"
                "- date\n"
                "- version\n"
                "- status\n"
                "- about\n"
                "- exit\n"
            )
        elif text == "version":
            return f"{Config.APP_NAME} Version : {Config.VERSION}"
        elif text == "status": 
            return f"Status : {Config.STATUS}"
        elif text == "about": 
            return (
                f"I am {Config.APP_NAME} AI.\n"
                "Created to become a human-like intelligent assistant."
            )
        return None