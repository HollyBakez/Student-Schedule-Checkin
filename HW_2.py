#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 17:34:48 2019

@author: hollandho
"""

# Student class
class Student:
    
# default constructor 
    def __init__(self, info):
        self._varname = ' ' 
        self._key_name = ' '
        info_split = info.split(',')
        student_obj = dict()
# parses the necessary keyname and value      
        for element in info_split:
            key_name, value_name = element.split(':')
            key_name = key_name.strip()
            value_name = value_name.strip()
            student_obj[key_name] = value_name
            
            if key_name == 'CWID':
                self.cwid = value_name
            elif key_name == 'FirstName':
                self.fn = value_name
            elif key_name == 'LastName':
                self.ln = value_name
            elif key_name == 'Gender':
                self.gender = value_name
            elif key_name == 'BirthDate':
                self.birthdate = value_name
            elif key_name == 'ClassID':
                self.classid = value_name
            elif key_name == 'ClassDate':
                self.classdate = value_name
            elif key_name == 'Grade':
                self.grade = value_name
# string function to seperate
    def __str__(self):
        return str(self.cwid) + ', ' + str(self.fn) + ', ' + str(self.ln) + ', ' + str(self.gender) + ', ' + str(self.classid) + ', ' + str(self.classdate) + ', ' + str(self.grade)
              
# define setters
                
    def setCWID(self, cwid):
        print("Changing CWID to:", cwid)
        self.cwid = cwid
        
    def setFN(self, fn):
        print("Changing FirstName to:", fn)
        self.fn = fn
        
    def setLN(self, ln):
        print('Changing LastName to:', ln)
        self.ln = ln
    
    def setGender(self, gender):
        print('Changing Gender to:', gender)
        self.gender = gender
    
    def setClassID(self, classid):
        print('Changing ClassID to:', classid)
        self.classid = classid
    
    def setClassDate(self, classdate):
        print('Changing ClassDate to:', classdate)
        self.classdate = classdate
    
    def setGrade(self, grade):
        print('Changing Grade to:', grade)
        self.grade = grade

# define getters
    
    def getCWID(self):
        return self.cwid
    
    def getFN(self):
        return self.fn
   
    def getLN(self):
        return self.ln
    
    def getGender(self):
        return self.gender
    
    def getClassID(self):
        return self.classid
    
    def getClassDate(self):
        return self.classdate
    
    def getGrade(self):
        return self.grade
    
# set properties 
    prop_cwid = property(getCWID, setCWID)
    prop_fn = property(getFN, setFN)
    prop_ln = property(getLN, setLN)
    prop_gender = property(getGender, setGender)
    prop_classid = property(getClassID, setClassID)
    prop_classdate = property(getClassDate, setClassDate)
    prop_grade = property(getGrade, setGrade)

# print output function
    def output(self):
# formats the strings using .format() function, stores in var test_student
#returns using the properties 
      test_student = 'CWID:{0:^12} , FirstName:{1:<15}, LastName:{2:<10}, ClassID:{3:^9}, Grade:{4:>5}'
      return test_student.format(test.prop_cwid, test.prop_fn, test.prop_ln, test.prop_classid, test.prop_grade)
    
    def file_read(self, text):
        count = 0
        student_list = list()
        file_object = open(text, mode = 'r')
        data = file_object.readline()
        while data:
            text_student = Student(data)
            student_list.append(text_student)
        file_object.close()
        
        while count < len(student_list):
            text_print = Student(student_list[count])
            text_print.output()
            count += 1     

#student = 'CWID: 12345, FirstName: Holly, LastName: Ho, Gender: M, BirthDate: 09/17/1998, ClassID: CPSC 223P, ClassDate: 02/24/2019, Grade: A'
#student_amt = input('How many students are there: ')
#student_amt = int(student_amt)
            
print('Please input in this format: \n CWID: 12345, FirstName: John, LastName: Do, Gender: F, BirthDate: 09/17/1998, ClassID: CPSC 223P, ClassDate: 02/24/2019, Grade: A')
student = input('Please input student info: ')
test = Student(student)

#prints out the testing output
print(test.output())






