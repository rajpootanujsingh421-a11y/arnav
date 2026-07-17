import random
from brain.responses import RESPONSES

class ResponseSelector:
    def get(self, category, **kwargs):
        responses = RESPONSES.get(category)
        if not responses:
            return None
        
        response = random.choice(responses)
        return response.format(**kwargs)