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

    def groupStudentsByGrade(self):
        try:
            students = self.db.get_all_students()
            if students:
                grades = {}
                for student in students:
                    grade = student['grade']
                    if grade not in grades:
                        grades[grade] = []
                    grades[grade].append(student)
                
                print("Students Grouped by Grade:")
                print("---------------------------")
                for grade, students in grades.items():
                    print(f"Grade: {grade}")
                    print("--------------------")
                    for student in students:
                        print(f"Student ID: {student['id']}, Name: {student['name']}, Email: {student['email']}")
                    print()
            else:
                print("No students found.")
        except Exception as e:
            print(f"Error: {e}")

    def partitionStudentsByPassFail(self):
        try:
            students = self.db.get_all_students()
            if students:
                pass_students = []
                fail_students = []
                for student in students:
                    if student['average_mark'] >= 50:
                        pass_students.append(student)
                    else:
                        fail_students.append(student)
                
                print("Students Partitioned by Pass/Fail:")
                print("-----------------------------------")
                print("Pass:")
                for student in pass_students:
                    print(f"Student ID: {student['id']}, Name: {student['name']}, Email: {student['email']}")
                print("\nFail:")
                for student in fail_students:
                    print(f"Student ID: {student['id']}, Name: {student['name']}, Email: {student['email']}")
            else:
                print("No students found.")
        except Exception as e:
            print(f"Error: {e}")

    def removeStudent(self, student_id):
        try:
            if self.db.delete_student(student_id):
                print(f"Student with ID {student_id} has been removed successfully.")
            else:
                print(f"Student with ID {student_id} not found.")
        except Exception as e:
            print(f"Error: {e}")

    def clearAllData(self):
        try:
            confirmation = input("Are you sure you want to clear all data? This action cannot be undone. (yes/no): ")
            if confirmation.lower() == 'yes':
                self.db.clear_students_data()
                print("All data cleared successfully.")
            else:
                print("Clear operation aborted.")
        except Exception as e:
            print(f"Error: {e}")

            

db = Database()
admin = Admin(db)
admin.viewAllStudents()
admin.groupStudentsByGrade()
admin.partitionStudentsByPassFail()
# admin.removeStudent("853160")
# admin.clearAllData()