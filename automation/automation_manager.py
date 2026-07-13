import os
from automation.app_launcher import AppLauncher
from automation.browser import Browser
from automation.system import SystemControl
from automation.command_parser import AutomationParser
from automation.windows_app_database import WindowsAppDatabase
from automation.file_manager import FileManager
from automation.file_search import FileSearcher

class AutomationManager:

    def __init__(self):

        self.apps = AppLauncher()
        self.browser = Browser()
        self.files = FileManager()
        self.searcher = FileSearcher()
        self.system = SystemControl()
        self.parser = AutomationParser()
        self.database = WindowsAppDatabase()
        
    def open_app(self, app_name):
    
        app_id = self.database.find(app_name)
        
        if app_id:
            
            if "!" in app_id or "." in app_id:
                return self.apps.launch_store_app(app_id)
            
            return self.apps.launch(app_id)
        return f"I couldn't find '{app_name}'."
    
    def open_folder(self, folder):
        return self.files.open_folder(folder)
    
    def open_file(self, filename):
        path = self.searcher.find_file(filename)
        
        if path is None:
            return f"I couldn't find {filename}."
        os.startfile(path)
        return f"Opening {filename}."