from database import Database
from utils import Utils
from student import Student
class Admin:
    def __init__(self):
        self.db = Database()

    #checked
    def viewAllStudents(self):
        try:
            students = self.db.get_all_students()
            if students:
                for student in students:
                    print('    '+student['name']+' :: '+student['id']+' --> EMAIL: '+student['email'])
        except Exception as e:
            print("Error: {e}")

    def groupStudentsByGrade(self):
        try:
            students = self.db.get_all_students()
            students_by_grade = {}
            for student in students:
                # Calculate the average marks
                total_marks = sum(subject['marks'] for subject in student['subjects'].values())
                num_subjects = len(student['subjects'])
                average_marks = total_marks / num_subjects
                
                # Get the grade based on the average marks
                grade = get_grade(average_marks)
                
                # Add the student to the corresponding grade category
                if grade not in students_by_grade:
                    students_by_grade[grade] = []
                students_by_grade[grade].append(student)

            # Print students grouped by their grade
            for grade, students_in_grade in students_by_grade.items():
                print(f"Grade: {grade}")
                for student in students_in_grade:
                    print(f"  ID: {student['id']}, Name: {student['name']}, Email: {student['email']}, Average Marks: {sum(subject['marks'] for subject in student['subjects'].values()) / len(student['subjects'])}")
                print()  # Add an empty line for better readability
            for subject_id, subject_info in subjects.items():
                marks = subject_info['marks']
                print('        [ Subject::'+subject_id+' -- marks = '+str(marks)+' -- grade =  '+self.getGrade(marks)+' ]')
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
admin = Admin()
# admin.viewAllStudents()
admin.groupStudentsByGrade()
# admin.partitionStudentsByPassFail()
# admin.removeStudent("853160")
# admin.clearAllData()
