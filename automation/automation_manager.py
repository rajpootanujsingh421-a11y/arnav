from automation.app_launcher import AppLauncher
from automation.browser import Browser
from automation.system import SystemControl
from automation.command_parser import AutomationParser


class AutomationManager:

    def __init__(self):

        self.apps = AppLauncher()
        self.browser = Browser()
        self.system = SystemControl()
        self.parser = AutomationParser()