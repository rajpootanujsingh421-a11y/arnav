class AppIndex:
    
    def __init__(self):

        self.apps = {}

    def add(self, name, path):

        self.apps[name.lower()] = path

    def get(self, name):

        return self.apps.get(name.lower())

    def all(self):

        return self.apps