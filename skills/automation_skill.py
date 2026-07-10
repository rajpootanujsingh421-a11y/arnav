from automation.automation_manager import AutomationManager


class AutomationSkill:

    def __init__(self):

        self.auto = AutomationManager()

    def handle(self, user_input):

        command = self.auto.parser.parse(user_input)

        if command is None:
            return None

        category, action = command
#apps
        if category == "app":

            if action == "chrome":
                return self.auto.apps.open_chrome()

            elif action == "notepad":
                return self.auto.apps.open_notepad()

            elif action == "calculator":
                return self.auto.apps.open_calculator()

            elif action == "paint":
                return self.auto.apps.open_paint()

#Browser
        elif category == "browser":

            if action == "google":
                return self.auto.browser.open_google()

            elif action == "youtube":
                return self.auto.browser.open_youtube()

        return None