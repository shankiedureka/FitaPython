from student_management import add_student, load_data

def display_menu():
    print("========Student Management System================")
    print("Operations we support, Just give the opertion number")
    print('1. Add Student')

def main():
    database = load_data()
    while True:
        display_menu()
        choice = input('Enter the choice : ')
        if choice == '1':
            add_student(database)
        if choice != '1':
            break


if __name__ == "__main__":
    main()







