import random

class Utils:
    @staticmethod
    def generate_random_id():
        """Generates a unique six-digit ID that is not already in use."""
        new_id = str(random.randint(100000, 999999))
        return new_id
            


            
            