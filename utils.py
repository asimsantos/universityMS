import random

class Utils:
    #Generates a random six-digit ID
    @staticmethod
    def generate_random_id():
        new_id = str(random.randint(100000, 999999))
        return new_id
    
    def generate_random_student_id():
        new_id = (random.randint(1, 999999))
        new_id = f"{new_id:06}"
        return new_id
            


            
            