'''
Created by Holland Ho 2/24/2019
Homework 1, Student-Registration Program
'''

student_amt = input("How many students are there? ") # Recieves how many students there are
student_amt = int(student_amt) # turns input to int
count = 0 
student_roster = list() #Creates a student roster list of student objects

while count < student_amt: # Takes in student info 'x' amount of times
    info = input("Please enter in student info: ") 
    info_split = info.split(',') #splits at the ','
    student_obj = dict() # creates a student dictionary 

    for student in info_split:
       
        key_name, value_name = student.split(':') #splits at the ':' to create the key and value 
        key_name = key_name.strip()
        value_name = value_name.strip()
        student_obj[key_name] = value_name # Updates the key and value in the student dictionary
        #student_roster.append(student_obj)
    student_roster.append(student_obj)  # adds student object into student list
    count +=1 #increments counter

   
print(student_roster)