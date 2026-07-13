from agent.tasks import Task

class LocalPlanner:
    
    def create_plan(self, user_input):
        text = user_input.lower()
        
        if "youtube" in text and "play" in text:
            
            query = (
                text.replace("paly", "")
                    .replace("on youtube", "")
                    .replace("youtube", "")
                    .strip()
                    
            )
            return [ 
                    Task(
                        "youtube_search",
                        query=query
                    ),
                    Task(
                        "play_first"
                    )
                    ]
        if "search" in text and "google" in text:
            query = (
                text.replace("search", "")
                    .replace("on google", "")
                    .replace("google", "")
                    .strip()
            )
            return [
                Task(
                    "google_search",
                    query=query
                )
            ]
        return None