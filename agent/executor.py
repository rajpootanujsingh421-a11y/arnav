from automation.automation_manager import AutomationManager
from automation.web.browser_agent import BrowserAgent
from automation.web.google_agent import GoogleAgent
from agent.task_memory import TaskMemory


class Executor:

    def __init__(self):

        self.auto = AutomationManager()
        self.browser = BrowserAgent()
        
        self.google = GoogleAgent(self.browser)
        self.task_memory = TaskMemory()

    def execute(self, tasks):
    
        if not tasks:
            return None

        # Save complete plan
        self.task_memory.set_tasks(tasks)

        while self.task_memory.has_task():

            task = self.task_memory.current_task()

            print("-------------")
            print("Task :", task.type)
            print("Data :", task.data)
            print("-------------")

        # Browser Tasks
            if task.type == "youtube_search":

                self.browser.youtube_search(
                    task.data["query"]
                )

            elif task.type == "play_first":

                print("▶ Executing play_first")

                self.browser.play_first_video()

            elif task.type == "google_search":

                self.google.search(
                    task.data["query"]
                )

        # App Tasks
            elif task.type == "open_app":

                self.auto.open_app(
                    task.data["target"]
                )

        # Move to next task
            self.task_memory.next_task()

        self.task_memory.clear()

        return "Done."