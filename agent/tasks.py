class Task:
    
    def __init__(self, task_type, **kwargs):

        self.type = task_type

        self.data = kwargs