import random
from database import Database

class Subjects:

    def __init__(self):
        self.db = Database()
        self.subjects = [
                {'id': '702', 'name': 'Math'},
                {'id': '305', 'name': 'AI/ML'},
                {'id': '401', 'name': 'Science'},
                {'id': '390', 'name': 'Computer'},
                {'id': '540', 'name': 'History'},
                {'id': '745', 'name': 'Programming'}
            ]

    def display_subjects(self):
        print("Available Courses:")
        for subject in self.subjects:
            print(f"ID: {subject['id']}, Name: {subject['name']}")


    def enroll_subject(self, student_id):
        enrolled_subjects = self.db.get_subjects(student_id)
        if enrolled_subjects and len(enrolled_subjects) >= 4:
            print("Cannot enroll more than 4 subjects.")
            return False

        available_courses = [subject for subject in self.subjects if subject['id'] not in enrolled_subjects]

        subject_to_enroll = random.choice(available_courses)
        self.db.set_subjects(student_id, subject_to_enroll['id'], subject_to_enroll['name'], random.randint(0, 100))
        print(f"Enrolled in {subject_to_enroll['name']}.")
        return True

    def drop_subject(self, student_id, subject_id):
        enrolled_subjects = self.db.get_subjects(student_id)
        if subject_id in enrolled_subjects:
            self.db.remove_subject(student_id, subject_id)
            print(f"Dropped subject with ID {subject_id}.")
            return True
        else:
            print("Subject not found or already dropped.")
            return False
        

# Testing
sub = Subjects()

# sub.display_subjects()

# sub.enroll_subject('110571')

# sub.drop_subject('110571', '540')