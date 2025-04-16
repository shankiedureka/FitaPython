import json

#To read and load the json file into dictionary
def load_data():
    with open('E:/Git/FitaPython/Project/Student_management_system/sample.json','r') as f:
        student_db = json.load(f)
    
    return student_db

#Saves ths dictionary to json file
def save_data(student_db):
    try:
        with open('E:/Git/FitaPython/Project/Student_management_system/sample.json','w') as f:
            json.dump(student_db,f)
            return 'Success'
    except Exception as e:
        print(str(e))
        return 'Failed'
   
def add_student(student_db):
    try:
        student_id = (input('Enter Student Id: ')) 
        #check whether the ID is already present in the Database
        #a = [1,2,3,4,5]
        #if 1 in a:

        #I can have if without else
        if student_id in student_db:
            print("Student Id already present")
            return None
        
        name = input('Enter the student"s name : ')
        age = int(input('Enter Student Age : '))
        course = input('Enter the course : ')
        marks = float(input('Enter the marks : '))

        #dictionary_variable[key] = value
        student_db[student_id] = {"Name":name,
                                    "Age":age,
                                    "Course":course,
                                    "Marks":marks}
    
        status = save_data(student_db)
        if status == 'Success':
            print('Student details saved successfully')
        else:
            print('Student details throwed error while saving')
    except Exception as e:
        print(str(e))
        print('Issue in adding new student')



      
      
   