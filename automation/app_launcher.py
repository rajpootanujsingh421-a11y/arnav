import subprocess

class AppLauncher:
    def open_chrome(self):
        
        try:
            subprocess.Popen("start chrome",shell=True)
            return "Opening Chrome."
        
        except Exception:
            return "Chrome not found."
        
    def open_notepad(self):
        subprocess.Popen("notepad")
        return "Opening Notepad."
    
    def open_calculator(self):
        
        subprocess.Popen("calc")
        return "Opening Calculator."
    
    def open_paint(self):
        
        subprocess.Popen("mspaint")
        return "Opening Paint."