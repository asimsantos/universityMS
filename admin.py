from database import Database

class Admin:
    def __init__(self, db):
        self.db = db

    def viewAllStudents(self):
        try:
            students = self.db.get_all_students()
            if students:
                print("List of All Students:")
                print("---------------------")
                for student in students:
                    print(f"Student ID: {student['id']}, Name: {student['name']}, Email: {student['email']}")
            else:
                print("No students found.")
        except Exception as e:
            print(f"Error: {e}")

# Example usage
db = Database()
admin = Admin(db)
admin.viewAllStudents()
