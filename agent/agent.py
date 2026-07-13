from agent.planner import Planner
from agent.executor import Executor


class Agent:

    def __init__(self):

        self.planner = Planner()
        self.executor = Executor()

    def run(self, user_input):

        tasks = self.planner.create_plan(user_input)

        return self.executor.execute(tasks)