from student_management import *

def display_menu():
    print("========Student Management System================")
    print("Operations we support, Just give the opertion number")
    print('Press 6 to exit the application')
    print('1. Add Student')
    print('2. View Students')
    print('3. Search Student by ID')
    print('4. Update Details')
    print('5. Delete Student')
    print('6. Course Statistics')
    print('7. Exit')

def main():
    database = load_data()
    while True:
        display_menu()
        choice = input('Enter the choice : ')
        if choice == '1':
            add_student(database)
        elif choice == '2':
            view_students(database)
        elif choice=='3':
            search_student(database)
        elif choice == '4':
            update_details(database)
        elif choice == '5':
            delete_student(database)
        elif choice == '6':
            course_statistics(database)
        elif choice == '7':
            break

#CRUD operation

if __name__ == "__main__":
    main()







