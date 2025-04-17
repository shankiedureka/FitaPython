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

def view_students(student_db):
    #whether there are students in database
    #checking whether the students_db is having atleast 1 value
    #if student_db is empty
    if not student_db: #if not False
        print('No students found')
        return None
    for key,val in student_db.items():
        #to get the value in dictionary
        #dictionary_variable[key]
        # student_db[key]['Name']
        print("Id: : {},Name: {} ,Age : {}, Course:{},Marks:{} ".format(key,val['Name'],val['Age'],val['Course'],val['Marks']))

def search_student(student_db):
    id = input('Enter Students Id : ')
    if id in student_db:
        print(student_db[id])
    else:
        print('Student Id not found')

def update_details(student_db):
    try:
        id = input('Enter Students Id : ')
        if id not in student_db:
            print('Student Id is not found')
        else:
            name = input('Enter the student"s name : ')
            age = int(input('Enter Student Age : '))
            course = input('Enter the course : ')
            marks = float(input('Enter the marks : '))

            #dictionary_variable[key] = value
            student_db[id] = {"Name":name,
                                        "Age":age,
                                        "Course":course,
                                        "Marks":marks}
        
            status = save_data(student_db)
            if status == 'Success':
                print('Student details updated successfully')
            else:
                print('Student details throwed error while updating')
    except Exception as e:
        print(str(e))
        print('Student details throwed error while updating')

def delete_student(student_db):
    id = input('Enter student Id : ')
    if id not in student_db:
        print('StudentId not found')
    else:
        del student_db[id]
        status = save_data(student_db)
        if status == 'Success':
            print('Student detail deleted successfully')
        else:
            print('Student details throwed error while deleting')
        
def course_statistics(student_db):
    if not student_db:
        print('No details in database')
        return None
    stats = {}
    for key,val in student_db.items():
        course_name = val['Course']
        if course_name in stats:
            #assigning = getting the value
            stats[course_name] = stats[course_name] + 1
        else:
            stats[course_name] = 1
    print(stats)



   