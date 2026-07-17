class TaskMemory:
    def __init__(self):
        self.tasks = []
        
        self.current = -1
        
    def set_tasks(self, tasks):
        self.tasks = tasks
        self.current = 0
        
    def has_task(self):
        return (
            self.current >= 0
            and self.current < len(self.tasks)
        )
        
    def current_task(self):
        if self.has_task():
            return self.tasks[self.current]
        return None
    
    def next_task(self):
        self.current += 1
        
        if self.has_task():
            return self.tasks[self.current]
        
        return None
    
    def clear(self):
        self.tasks = []
        self.current = -1