"""
READ ME
    Data stored in format --> 977834,Asim Santos,asimsantos@gmail.com,mypassword

    To use the functions from this class::
        # Import this the Database class from the database.py file
        from database import Database
        # Create an instance of the class
        db = Database()

        ### CRUD functions
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

        ### Subject operations
        # To add a subject
        set_subjects(student_id, subject_id, subject_name)
        # To display all Subject list by student ID
        get_subjects(student_id)
        # To remove a subject from the student's data
        remove_subject(student_id, subject_id)

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
    # changed by ashraf    
    def add_student(self, studentID, name, password, email):
        with open(self.filename, 'a') as file:
            file.write(f"{studentID},P{name},{password},{email},\n")
        print("Student data added to Database")

    # def add_student(self, email, password, full_name):
        # students = self.get_all_students() 
        # existing_ids = {student['id'] for student in students}
        # while True:
        #     random_id = Utils.generate_random_id()
        #     if random_id not in existing_ids:
        #         student_id = random_id
        #         break
        # with open(self.filename, 'a') as file:
        #     file.write(f"{student_id},{full_name},{email},{password},\n")
    # changed by ashraf  


    # Gets all students in the database.
    # def get_all_students(self):
    #     students = []
    #     with open(self.filename, 'r') as file:
    #         lines = file.readlines()
    #         for line in lines:
    #             student_id, full_name, email, password = line.strip().split(',')
    #             students.append({'id': parts[0], 'name': parts[1], 'email': parts[2], 'password': password})
    #     return students

    def get_all_students(self):
        students = []
        with open(self.filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(',')
                if len(parts) < 4:
                    continue
                student = {
                    'id': parts[0],
                    'name': parts[1],
                    'password': parts[2],
                    'email': parts[3],
                    'subjects': dict(item.split(':') for item in parts[4].split(';') if item)
                }
                students.append(student)
        return students
    
    # Gets a student by ID.
    def get_student_by_id(self, student_id):
        students = self.get_all_students()
        for student in students:
            if student['id'] == student_id:
                return student
        return None

    # changed by ashraf  
    def update_student(self, studentID, new_name, new_password, new_email):
        with open(self.filename, 'r') as file:
            lines = file.readlines()
        for i, line in enumerate(lines):
            if line.startswith(f'P{studentID},'):
                student_data = line.strip().split(',')
                student_data[1] = new_name
                student_data[2] = new_email
                student_data[3] = new_password
                updated_line = f"P{studentID},{','.join(student_data[1:])},\n"
                lines[i] = updated_line
                break
        else:
            print(f"Student with ID {studentID} not found.")
        with open(self.filename, 'w') as file:
            file.writelines(lines)
        print("Student data updated in the database")

    # Updates an existing student's password.
    # def add_student(self, email, password, full_name): # need to check
    #     students = self.get_all_students()
    #     existing_ids = {student['id'] for student in students}
    #     while True:
    #         random_id = Utils.generate_random_id()
    #         if random_id not in existing_ids:
    #             student_id = random_id
    #             break
    #     with open(self.filename, 'a') as file:
    #         file.write(f"{student_id},{full_name},{email},{password},\n")
    # changed by ashraf  

    # Deletes a student from the database.
    def delete_student(self, student_id):
        students = self.get_all_students()
        with open(self.filename, 'w') as file:
            for student in students:
                if student['id'] != student_id:
                    self.write_student(file, student)
        return len(students) > len(self.get_all_students())

    # Deletes all student from the database.
    def clear_students_data(self):
        open(self.filename, 'w').close()


    # Updates an existing student's password.
    def update_password(self, student_id, new_pw):
        students = self.get_all_students()
        updated = False
        with open(self.filename, 'w') as file:
            for student in students:
                if student['id'] == student_id:
                    student['password'] = new_pw
                    updated = True
                self.write_student(file, student)
        return updated
                    
    # Adds subjects to the student's records
    def set_subjects(self, student_id, subject_id, subject_name):
        students = self.get_all_students()
        updated = False
        with open(self.filename, 'w') as file:
            for student in students:
                if student['id'] == student_id:
                    student['subjects'][subject_id] = subject_name
                    updated = True
                self.write_student(file, student)
        return updated
    
    # Gets all the subjects a student is enrolled to
    def get_subjects(self, student_id):
        student = self.get_student_by_id(student_id)
        return student['subjects'] if student else None

    # Removes a subject(by ID) from the student's records
    def remove_subject(self, student_id, subject_id):
        students = self.get_all_students()
        updated = False
        with open(self.filename, 'w') as file:
            for student in students:
                if student['id'] == student_id and subject_id in student['subjects']:
                    del student['subjects'][subject_id]
                    updated = True
                self.write_student(file, student)
        return updated

    # changed by ashraf
    # Helper function to write into the student.data in a uniform layout
    # def write_student(self, file, student):
    #     subjects_str = ';'.join(f"{key}:{value}" for key, value in student['subjects'].items())
    #     file.write(f"{student['id']},{student['name']},{student['password']},{student['email']},{subjects_str}\n")
    # changed by ashraf

# Testing
db = Database()

# db.add_student('asimsantos@gmail.com', 'mypass', 'Asim Santos')
# db.add_student('teststu@gmail.com', 'testpass', 'Test Student')

# db.update_password('853160', 'testpass2')

# db.delete_student('861984')

# db.clear_students_data()

# print(db.get_student_by_id('110571'))

# print(db.get_all_students())

# db.set_subjects('110571','501','Maths')
# db.set_subjects('110571','732','Science')


# print(db.get_subjects('110571')) 
# db.remove_subject('110571','501')
# print(db.get_subjects('110571')) 


""" 
Sample data
110571,Asim Santos,asimsantos@gmail.com,mypass,732:Science
"""