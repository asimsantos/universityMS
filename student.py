from utils import Utils
from database import Database
import re
class Student:
    def __init__(self, StudentID, Name, Password,  Email):
        self.Name = Name
        self.Password = Password
        self.StudentID = StudentID
        self.Email = Email
        self.Results = ""

    def enrollSubject(self):
        
        return True

    def removeStudent(self):
        
        return True  

    def viewEnrolment(self):
        print('fsaffd')
        return []  

    def changePassword(self, oldPass, newPass):
        if self.checkPassword(oldPass,self.Email) and self.validatePassword(newPass):
            Database.update_student(self, self.StudentID, self.Name, newPass, self.Email)
        else:
            print('Old or new password is invalid. try again')   
        
    def changingPassword(self): # It should be called from menu
        while 1:
            oldPassword = input("Enter old password: ")
            newPassword = input("Enter new password: ")
            if(self.changePassword(oldPassword,newPassword)):
                break
        self.changePassword(oldPassword,newPassword)
        print('your password has been changed')
        
    def login(self, Email, Password):
        print("Login with your Email and Password\n")
        while 1:
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            if self.validateEmail(email):
                print('Invalid Email. Try Again')
            elif self.checkPassword(password,email):
                print('You are Logged in')
                break
            else: 
                print('Email or Password is incorrect. Try Again')

    def checkPassword(self,password,email):
        students=Database.get_all_students()
        for s in students:
            if(s['email']==email):
                if(s['password']==password):
                    return True
        return False

    def register(self, studentID, name, password, email): 
        self.Name = name
        self.Password = password
        self.StudentID = studentID
        self.Email = email
        Database.add_student(name, password, studentID, email)
        print("You have successfully registered.")

    def studentRegistration(self): # It should be called from menu
        print("Provide the following information for register\n")
        name = input("Enter your name: ")
        while 1:
            email = input("Enter your email: ")
            if self.validateEmail(email):
                break
            else:
                print('Email is invalid')
        while 1:
            password = input("Enter your password: ")
            if self.validatePassword(password):
                break
            else:
                print("Password is invalid")
        self.register(self.generateStudentID(),name,password,email)
    
    def validateEmail(self, email):
        email_pattern = r"^[a-zA-Z0-9._%+-]+@university\.com$"
        if re.match(email_pattern, email):
            return True
        else:
            return False

    def validatePassword(self, password):
        password_pattern = r"^[A-Z][a-zA-Z]{4,}[0-9]{3,}$"
        if re.match(password_pattern, password):
            return True
        else:
            return False

    def generateStudentID(self):
        students=Database.get_all_students()
        students_ids = {s['id'] for s in students}
        while 1:            
            new_id=Utils.generate_random_student_id()
            if(new_id not in students_ids):
                return new_id
        print("Error Generating Student IDs")
        return "xxxxxx"  