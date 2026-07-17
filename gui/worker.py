from PySide6.QtCore import QObject, Signal, Slot

class AssistantWorker(QObject):
    finished = Signal(str)
    
    def __init__(self, assistant, text):
        
        super().__init__()
        
        self.assistant = assistant
        self.text = text
        
    @Slot()
    def run(self):
        response = self.assistant.process_command(self.text)
        
        self.finished.emit(response)
        