from datetime import datetime

class CommandHandler:
    
    def process(self, command: str):
        command = command.lower().strip()   
        
        if command == "hello":
            return "Hello Anuj! 👋" 
        
        elif command == "who are you":
            return "I am Arnav AI."
        
        elif command == "time":
            return datetime.now().strftime("%I:%M:%S %p")
        
        elif command == "date":
            return datetime.now().strftime("%d-%m-%Y")

        elif command == "exit":
            return "exit"
        
        else:
            return "Sorry, I don't understand that command."