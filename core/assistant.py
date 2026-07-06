from config import APP_NAME, VERSION
from utils.logger import logger
from core.brain import Brain    
from core.response import Response

class ArnavAssistant:   
    def __init__(self):
        self.name = APP_NAME
        self.version = VERSION
        self.status = "ONLINE"
        
        self.brain = Brain()

        logger.info("Assistant Started")
        
    def introduce(self):    
        
        print(f"\nHello! I am {self.name}.")
        print(f"Version : {self.version}")
        print(f"Status  : {self .status}") 
        
    def start(self):
        self.introduce()
        
        while True:
            command = input("\nYou : ")
            logger.info(f"User : {command}")
            response = self.brain.think(command)
            
            if response == "exit":
                print("Arnav : Goodbye Anuj 👋")
                logger.info ("Assistant Closed")
                break
            print(f"Arnav : {response}")
            logger.info(f"Arnav : {response}")