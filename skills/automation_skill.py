from automation.automation_manager import AutomationManager


class AutomationSkill:

    def __init__(self):

        self.auto = AutomationManager()

        # Last opened application/browser
        self.last_target = None

    def handle(self, user_input):

        text = user_input.lower().strip()

        # Context Based Commands
        if self.last_target == "youtube":

            if text.startswith("search "):

                query = text.replace("search ", "").strip()

                return self.auto.browser.search_youtube(query)

            if text.startswith("play "):
    
    # Play commands Planner ko handle karne do

                return None

        if self.last_target == "google":

            if text.startswith("search "):

                query = text.replace("search ", "").strip()

                return self.auto.browser.search_google(query)

        # Normal Parser
        command = self.auto.parser.parse(text)

        if command is None:
            return None

        category, action = command

        # Planner ko handle karne do
        if (
            "play" in text
            or "search" in text
        ):
            return None

        # Apps
        if category == "app":

            self.last_target = action

            return self.auto.open_app(action)

        # Browser
        elif category == "browser":

            self.last_target = action

            if action == "google":
                return self.auto.browser.open_google()

            elif action == "youtube":
                return self.auto.browser.open_youtube()

        # Dynamic Apps
        elif category == "dynamic_app":

            self.last_target = action

            return self.auto.open_app(action)

        # Folder
        elif category == "folder":

            return self.auto.open_folder(action)

        # File
        elif category == "file":

            return self.auto.open_file(action)

        return None