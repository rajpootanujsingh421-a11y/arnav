import os


class SystemControl:

    def shutdown(self):
        os.system("shutdown /s /t 1")

    def restart(self):
        os.system("shutdown /r /t 1")

    def lock(self):
        os.system("rundll32.exe user32.dll,LockWorkStation")