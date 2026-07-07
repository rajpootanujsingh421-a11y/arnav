import json
from config import Config
import os
class LongMemory:

    def __init__(self):
        
        self.file_path = Config.MEMORY_FILE

        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as file:
                json.dump({}, file)

    def save(self, key, value):

        with open(self.file_path, "r") as file:
            data = json.load(file)

        data[key] = value

        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)

    def load(self, key):

        with open(self.file_path, "r") as file:
            data = json.load(file)

        return data.get(key)
    def delete(self, key):
    
        with open(self.file_path, "r") as file:
            data = json.load(file)

        if key in data:
            del data[key]

        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)

    def all(self):

        with open(self.file_path, "r") as file:
            return json.load(file)