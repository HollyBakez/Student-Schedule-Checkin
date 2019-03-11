'''
Homework 2 
Created by Holland Ho 
Date 3/10/2019
'''
print("Please enter the student info in this format ")
print("CWID: 12345678, FirstName: Holland, ...")


class Student:
    student_default = " " #init to whitespace
    # default constructor 
    # set to dictionary? key/value as setters/getters?
    def __init__(self):
        self.student_default = "CWID: 12345678, FirstName: Brian, LastName: Chungsta, Gender: M, BirthDate: 03/14/1999, ClassID: CPSC 223P, ClassDate: 01/26/2018, Grade: A  "
 
    def setCWID(self, cwid):
        self._cwid = cwid

    def getCWID(self):
        return self._cwid
'''
    def setFN(self, first_name):
        self._fn = first_name

    def setLN(self, last_name):
        self._ln = last_name

    def setGender(self, gender):
        self._gender = gender 

    def setBirthDate(self, birth_date):
        self._birth_date = birth_date

    def setClassID(self, classid):
        self._classid = classid

    def setClassDate(self, classdate):
        self._classdate = classdate 

    def setGrade(self, grade):
        self._grade = grade 
''' 
    def print_student(self):
        print(self.student_default)

student_info = Student()

student_info.print_student()