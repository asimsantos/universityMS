import random

class Utils:
    #Generates a random six-digit ID
    @staticmethod
    def generate_random_id():
        new_id = str(random.randint(100000, 999999))
        return new_id
            


            
            