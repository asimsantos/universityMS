"""
READ ME
    Data stored in format --> 977834,Asim Santos,asimsantos@gmail.com,mypassword

    To use the functions from this class:
        # Import this the Database class from the database.py file
        from database import Database
        # Create an instance of the class
        db = Database()
        # To add a student
        db.add_student(email, password, name)
        # To change password
        db.update_password('332797', 'mypass2')
        # To find a student by id
        db.get_student_by_id('977834')
        # To view all students
        db.get_all_students()
        # To remove a student by id
        db.delete_student('332797')
        To remove all students
        db.clear_students_data()
"""

from utils import Utils

class Database:
    def __init__(self, filename='students.data'):
        self.filename = filename
        # Try opening the data file to see if it exists
        try:
            open(self.filename, 'r').close()  
        # If the file does not exist, this creates a new file
        except FileNotFoundError:
            open(self.filename, 'w').close() 
    
    # Adds a new student to the database with a unique six-digit ID
    def add_student(self, email, password, full_name):
        existing_ids = {student['id'] for student in self.get_all_students()}
        while True:
            random_id = Utils.generate_random_id()
            if random_id not in existing_ids:
                student_id = random_id
                break
        with open(self.filename, 'a') as file:
            file.write(f"{student_id},{full_name},{email},{password}\n")

    # Gets all students in the database.
    def get_all_students(self):
        students = []
        with open(self.filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                student_id, full_name, email, password = line.strip().split(',')
                students.append({'id': student_id, 'name': full_name, 'email': email, 'password': password})
        return students
    
    # Gets a student by ID.
    def get_student_by_id(self, student_id):
        students = self.get_all_students()
        for student in students:
            if student['id'] == student_id:
                return student
        return None

    # Updates an existing student's password.
    def update_password(self, student_id, new_pw):
        students = self.get_all_students()
        updated = False
        with open(self.filename, 'w') as file:
            for student in students:
                if student_id == student['id']:
                    updated = True
                    file.write(f"{student['id']},{student['name']},{student['email']},{new_pw}\n")
                else:
                    file.write(f"{student['id']},{student['name']},{student['email']},{student['password']}\n")    
        return updated

    # Deletes a student from the database.
    def delete_student(self, student_id):
        students = self.get_all_students()
        deleted = False
        with open(self.filename, 'w') as file:
            for student in students:
                if student['id'] != student_id:
                    file.write(f"{student['id']},{student['name']},{student['email']},{student['password']}\n")
                else:
                    deleted = True
        return deleted

    # Deletes all student from the database.
    def clear_students_data(self):
        open(self.filename, 'w').close()
                    

# Testing
db = Database()

# db.add_student('asimsantos@gmail.com', 'mypass', 'Asim Santos')

# db.update_password('332797', 'mypass2')

# db.delete_student('332797')

# db.clear_students_data()

# print(db.get_student_by_id('977834'))

# print(db.get_all_students())


""" 
Sample data
307328,Test User,testacc@gmail.com,testpass
977834,Asim Santos,asimsantos@gmail.com,mypass
"""