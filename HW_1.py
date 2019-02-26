'''

Created by Holland Ho 2/24/2019
Homework 1, Student-Registration Program

'''
# Asks for amount of students
student_amt = input("How many students are there?")
student_amt = int(student_amt)
count = 0 
student_roster = list() #making a list of student objects

#inputs student info 
while count < student_amt:
    print('Student', count+1, 'info')
    cwid = input("Please enter in a CWID: ")
    cwid = int(cwid)
    firstname = input("Please enter in the First Name: ")
    lastname = input("Please enter in the Last Name: ")
    gender = input("Please enter in a Gender: ")
    birth = input("Please enter in the BirthDate: ")

#adds to a list of classes for the individual student
#each student has their own class schedule
'''
    class_id = list() # no need to make it complicated, just enter in again 
    class_amt = input("How many classes is this student taking: ")
    class_amt = int(class_amt)
    count2 = 0
    while count2 < class_amt:
        print('Class#: ', count2+1)
#adds amount of classes based on user input
        class_id.append(input("Please enter in the ClassID: "))
        count2 += 1
'''
#class_id = input("Please enter in the ClassID: ")
    class_date = input("Please enter in the ClassDate: ")
    grade = input("Please enter in the Grade: ")
    student_obj = {'CWID': cwid, 'FirstName': firstname, 'LastName': lastname, 'Gender': gender, 'BirthDate': birth, 'ClassID': class_id, 'ClassDate': class_date, 'Grade': grade}
# adds student info into the list for each individual student
    student_roster.append(student_obj)
    count += 1

print(student_roster)


#searching up desired class roster, displays students currently enrolled
'''
class_roster = input("Which class roster do you want to pull up: ")

count3 = 0

while count3 < len(student_roster):
    if class_roster == student_roster[count3][student_obj.get('ClassID')]:
        print(student_roster[count3])
    count3 += 1
'''
