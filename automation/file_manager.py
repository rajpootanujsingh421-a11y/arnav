import os
import subprocess
from pathlib import Path


class FileManager:

    def __init__(self):

        self.folders = {

            "desktop": Path.home() / "Desktop",

            "downloads": Path.home() / "Downloads",

            "documents": Path.home() / "Documents",

            "pictures": Path.home() / "Pictures",

            "videos": Path.home() / "Videos",

            "music": Path.home() / "Music"
        }

    def open_folder(self, name):

        name = name.lower().strip()

        if name not in self.folders:

            return None

        path = self.folders[name]

        subprocess.Popen(f'explorer "{path}"')

        return f"Opening {name}."