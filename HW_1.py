'''
Created by Holland Ho 2/24/2019
Homework 1, Student-Registration Program

'''

student_amt = input("How many students are there? ") # Recieves how many students there are
student_amt = int(student_amt) # turns input to int
if student_amt < 1: # amount of students must be greater than 0
    student_amt = input("Please enter an amount greater than 0: ")
    student_amt = int(student_amt)
count = 0 #counter
student_roster = list() #Creates a student roster list of student objects
class_roster = dict() # dictionary using class as the key and student objects as the value

while count < student_amt: # Takes in student info 'x' amount of times
    info = input("Please enter in student info: ")  # takes in student info
    info_split = info.split(',') #splits at the ','
    student_obj = dict() # creates a student dictionary 
    new_list = list() #refreshes a new list 
    for student in info_split:
        key_name, value_name = student.split(':') #splits at the ':' to create the key and value 
        key_name = key_name.strip() #removes the whitespaces from key,value inputs
        value_name = value_name.strip()
        #key_name = key_name.lower() #testing
        student_obj[key_name] = value_name # Updates the key and value in the student dictionary

    student_roster.append(student_obj)  # adds student object into student list
    class_name = student_obj.get('ClassID') # saves the classID value as a key 
    if class_roster.get(class_name) == None:  #if the classID is empty    
        class_roster[class_name] = new_list# create a new list
        class_roster[class_name].append(student_obj) #append to that list
    else: # if the class list already exists, add to it
        class_roster[class_name].append(student_obj) # addes to the list

    count +=1 #increments counter

class_desired = input("What class do you want to pull up?   ") # asks user for the class to pull up
#while class_roster.get(class_desired) == None: #if class does not exist
    #class_desired = input("Class roster was not found, please enter another class: ")
while class_desired != '-1':
    while class_roster.get(class_desired) == None: #if class not found then prompt again
         class_desired = input("Class roster was not found, please enter another class: ")
    print(class_desired, class_roster.get(class_desired)) # displays the student objects of that class
    class_desired = input('Enter another class to pull up or if finished please enter -1 to exit: ')
print('All Students: ',student_roster)

'''
------Test Cases and Outputs-------------
How many students are there? 10
Please enter in student info: CWID: 882277123, FirstName: Holland, LastName: Ho, Gender: M, BirthDate: 09/17/1996, ClassID: CPSC 223P, ClassDate: 02/26/2019, Grade: A
Please enter in student info: CWID: 123456789, FirstName: Jason, LastName: Jon, Gender: M, BirthDate: 01/02/1999, ClassID: BIO 101, ClassDate: 02/25/2019, Grade: B
Please enter in student info: CWID: 987654321, FirstName: Kelsie, LastName: Nguyen, Gender: F, BirthDate: 02/28/1999, ClassID: MATH 250A, ClassDate: 02/01/2019, Grade: A
Please enter in student info: CWID: 889234112, FirstName: Jasmine, LastName: Nguyen, Gender: F, BirthDate: 03/02/1999, ClassID: CPSC 223P, ClassDate: 02/26/2019, Grade: A
Please enter in student info: CWID: 445231234, FirstName: Brian, LastName: Chung, Gender: M, BirthDate: 02/29/1998, ClassID: CPSC 254, ClassDate: 01/18/2019, Grade: B
Please enter in student info: CWID: 882277123, FirstName: Holland, LastName: Ho, Gender: M, BirthDate: 09/17/1996, ClassID: CPSC 254, ClassDate: 02/26/2019, Grade: C
Please enter in student info: CWID: 776234123, FirstName: Jenny, LastName: Long, Gender: F, BirthDate: 03/19/1998, ClassID: MATH 250A, ClassDate: 02/26/2019, Grade: F
Please enter in student info: CWID: 992232133, FirstName: Ryan, LastName: Do, Gender: M, BirthDate: 09/11/1999, ClassID: GEOL 101, ClassDate: 02/01/2019, Grade: A
Please enter in student info: CWID: 123456789, FirstName: Jason, LastName: Jon, Gender: M, BirthDate: 01/12/1999, ClassID: GEOL 101, ClassDate: 02/01/2019, Grade: B
Please enter in student info: CWID: 880912332, FirstName: Kenneth, LastName: Garcias, Gender: M, BirthDate: 07/24/1997, ClassID: MATH 150B, ClassDate: 03/24/2019, Grade: D
What class do you want to pull up?   1
Class roster was not found, please enter another class: 2
Class roster was not found, please enter another class: CPSC 254
CPSC 254 [{'CWID': '445231234', 'FirstName': 'Brian', 'LastName': 'Chung', 'Gender': 'M', 'BirthDate': '02/29/1998', 'ClassID': 'CPSC 254', 'ClassDate': '01/18/2019', 'Grade': 'B'}, {'CWID': '882277123', 'FirstName': 'Holland', 'LastName': 'Ho', 'Gender': 'M', 'BirthDate': '09/17/1996', 'ClassID': 'CPSC 254', 'ClassDate': '02/26/2019', 'Grade': 'C'}]
Enter another class to pull up or if finished please enter -1 to exit: MATH 250A
MATH 250A [{'CWID': '987654321', 'FirstName': 'Kelsie', 'LastName': 'Nguyen', 'Gender': 'F', 'BirthDate': '02/28/1999', 'ClassID': 'MATH 250A', 'ClassDate': '02/01/2019', 'Grade': 'A'}, {'CWID': '776234123', 'FirstName': 'Jenny', 'LastName': 'Long', 'Gender': 'F', 'BirthDate': '03/19/1998', 'ClassID': 'MATH 250A', 'ClassDate': '02/26/2019', 'Grade': 'F'}]
Enter another class to pull up or if finished please enter -1 to exit: BIO 101
BIO 101 [{'CWID': '123456789', 'FirstName': 'Jason', 'LastName': 'Jon', 'Gender': 'M', 'BirthDate': '01/02/1999', 'ClassID': 'BIO 101', 'ClassDate': '02/25/2019', 'Grade': 'B'}]
Enter another class to pull up or if finished please enter -1 to exit: GEOL 101
GEOL 101 [{'CWID': '992232133', 'FirstName': 'Ryan', 'LastName': 'Do', 'Gender': 'M', 'BirthDate': '09/11/1999', 'ClassID': 'GEOL 101', 'ClassDate': '02/01/2019', 'Grade': 'A'}, {'CWID': '123456789', 'FirstName': 'Jason', 'LastName': 'Jon', 'Gender': 'M', 'BirthDate': '01/12/1999', 'ClassID': 'GEOL 101', 'ClassDate': '02/01/2019', 'Grade': 'B'}]
Enter another class to pull up or if finished please enter -1 to exit: CPSC 223P
CPSC 223P [{'CWID': '882277123', 'FirstName': 'Holland', 'LastName': 'Ho', 'Gender': 'M', 'BirthDate': '09/17/1996', 'ClassID': 'CPSC 223P', 'ClassDate': '02/26/2019', 'Grade': 'A'}, {'CWID':'889234112', 'FirstName': 'Jasmine', 'LastName': 'Nguyen', 'Gender': 'F', 'BirthDate': '03/02/1999', 'ClassID': 'CPSC 223P', 'ClassDate': '02/26/2019', 'Grade': 'A'}]
Enter another class to pull up or if finished please enter -1 to exit: -1
All Students:  [{'CWID': '882277123', 'FirstName': 'Holland', 'LastName': 'Ho', 'Gender': 'M', 'BirthDate': '09/17/1996', 'ClassID': 'CPSC 223P', 'ClassDate': '02/26/2019', 'Grade': 'A'}, {'CWID': '123456789', 'FirstName': 'Jason', 'LastName': 'Jon', 'Gender': 'M', 'BirthDate': '01/02/1999', 'ClassID': 'BIO 101', 'ClassDate': '02/25/2019', 'Grade': 'B'}, {'CWID': '987654321', 'FirstName': 'Kelsie', 'LastName': 'Nguyen', 'Gender': 'F', 'BirthDate': '02/28/1999', 'ClassID': 'MATH 250A', 'ClassDate': '02/01/2019', 'Grade': 'A'}, {'CWID': '889234112', 'FirstName': 'Jasmine', 'LastName': 'Nguyen', 'Gender': 'F', 'BirthDate': '03/02/1999', 'ClassID': 'CPSC 223P', 'ClassDate': '02/26/2019', 'Grade': 'A'}, {'CWID': '445231234', 'FirstName': 'Brian', 'LastName': 'Chung', 'Gender': 'M', 'BirthDate': '02/29/1998', 'ClassID': 'CPSC 254', 'ClassDate': '01/18/2019', 'Grade': 'B'}, {'CWID': '882277123', 'FirstName': 'Holland', 'LastName': 'Ho', 'Gender': 'M', 'BirthDate': '09/17/1996', 'ClassID': 'CPSC 254', 'ClassDate': '02/26/2019', 'Grade': 'C'}, {'CWID': '776234123', 'FirstName': 'Jenny', 'LastName': 'Long', 'Gender': 'F', 'BirthDate': '03/19/1998', 'ClassID': 'MATH 250A', 'ClassDate': '02/26/2019', 'Grade': 'F'}, {'CWID': '992232133', 'FirstName': 'Ryan', 'LastName': 'Do', 'Gender': 'M', 'BirthDate': '09/11/1999', 'ClassID': 'GEOL 101', 'ClassDate': '02/01/2019', 'Grade': 'A'}, {'CWID': '123456789', 'FirstName': 'Jason', 'LastName': 'Jon', 'Gender': 'M', 'BirthDate': '01/12/1999', 'ClassID': 'GEOL 101', 'ClassDate': '02/01/2019', 'Grade': 'B'}, {'CWID': '880912332', 'FirstName': 'Kenneth', 'LastName': 'Garcias', 'Gender': 'M', 'BirthDate': '07/24/1997', 'ClassID': 'MATH 150B', 'ClassDate': '03/24/2019', 'Grade': 'D'}]
Hollands-MBP:~ hollandho$

'''