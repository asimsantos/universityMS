courses = {
    '702': 'Math',
    '305': 'English',
    '401': 'Science',
    '390': 'Economics',
    '540': 'Political Science'
}

def display_courses():
    print("Available Courses:")
    for code, description in courses.items():
        print(f"{code}: {description}")

def read_students_data():
    students = []
    with open('students.data', 'r') as file:
        lines = file.readlines()
        for line_number, line in enumerate(lines, 1):
            print(f"Debug - Line {line_number}: '{line.strip()}'")  
            parts = line.strip().split(',', 4)  
            if len(parts) < 4:
                print(f"Warning - Malformed line {line_number}: '{line.strip()}'")  
                continue 
            student_id, name, email, password = parts[:4]
            subjects = {}
            if len(parts) == 5 and parts[4]:
                subject_parts = parts[4].split(';')
                for subject in subject_parts:
                    if subject:
                        subj_id, subj_name = subject.split(':')
                        subjects[subj_id] = subj_name
            students.append({
                'id': student_id,
                'name': name,
                'email': email,
                'password': password,
                'subjects': subjects
            })
    return students

def find_student(student_id):
    students = read_students_data()
    for student in students:
        if student['id'] == student_id:
            return student
    return None

def enroll_in_course(student_id, subjects):
    print("Current Subjects: ", subjects)
    if len(subjects) >= 4:
        print("You have already enrolled in the maximum number of courses (4).")
        return
    display_courses()
    choice = input("Enter the course code to enroll in: ").strip()
    if choice == 'done':
        return
    if choice in courses and choice not in subjects:
        subjects[choice] = courses[choice]
        update_students_data(student_id, subjects)
        print("Enrolled in new course successfully.")
    else:
        print("Invalid course code or already enrolled.")

def update_students_data(student_id, subjects):
    students = read_students_data()
    with open('students.data', 'w') as file:
        for student in students:
            if student['id'] == student_id:
                subjects_str = ';'.join(f"{k}:{v}" for k, v in subjects.items())
                line = f"{student['id']},{student['name']},{student['email']},{student['password']},{subjects_str}\n"
            else:
                subjects_str = ';'.join(f"{k}:{v}" for k, v in student['subjects'].items())
                line = f"{student['id']},{student['name']},{student['email']},{student['password']},{subjects_str}\n"
            file.write(line)

def main():
    student_id = input("Please enter your student ID: ").strip()
    student = find_student(student_id)
    if student:
        print(f"Student found: ID={student['id']}, Name={student['name']}")
        while True:
            action = input("Choose an action: Enroll (e), Show Subjects (s), Exit (x): ").lower()
            if action == 'e':
                enroll_in_course(student['id'], student['subjects'])
            elif action == 's':
                print("Enrolled Subjects:")
                for code, name in student['subjects'].items():
                    print(f"{code}: {name}")
            elif action == 'x':
                break
            else:
                print("Invalid action. Please choose again.")
    else:
        print("Student not found. Please ensure the ID is correct and try again.")

if __name__ == "__main__":
    main()