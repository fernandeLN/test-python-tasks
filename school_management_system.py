"""
School management system task
"""

# list_of_commands = ["create", "manage", "end"]
# user_type = ["student", "teacher", "homeroom teacher", "end"]
student_data = []
teacher_data = []
homeroom_teacher_data = []

def create_menu():
    print("=======CREATE MENU=======")
    while True:
        printed_user = (input("Enter the name of the category you want to create (student - teacher - homeroom teacher) or END to go back\n: ")).lower()
        # if printed_user not in user_type:
        #     print("Invalid category. Try again from the available categories.")
        # else:
        if printed_user == "end":
            break
        elif printed_user == "student":
            first_name_student = (input("Enter student's first name: ")).upper()
            last_name_student = (input("Enter student's last name: ")).upper()
            classroom_student = (input("Enter student's class room: ")).upper()
            student_data.append({"first_name": first_name_student, "last_name": last_name_student, "classroom": classroom_student})
            print(f"created student {first_name_student} {last_name_student} in classroom {classroom_student}")
            print(f"list of student data: {student_data}")

        elif printed_user == "teacher":
            first_name_teacher = (input("Enter teacher's first name: ")).upper()
            last_name_teacher = (input("Enter teacher's last name: ")).upper()
            subject_teacher = (input("Enter teacher's subject: ")).lower()
            classes = []
            classes_teacher = (input("Enter class names (press Enter on empty line to finish):")).upper()
            while classes_teacher != "":
                classes.append(classes_teacher)
                classes_teacher = (input("Enter class names (press Enter on empty line to finish):")).upper()
            teacher_data.append({"first_name": first_name_teacher, "last_name": last_name_teacher,"subject": subject_teacher, "classes_in_charge": classes})
            print(f"created teacher {first_name_teacher} {last_name_teacher} teaching {subject_teacher} and in charge of classes {classes}")
            print(f"list of teacher data: {teacher_data}")

        elif printed_user == "homeroom teacher":
            first_name_h_teacher = (input("Enter homeroom teacher's first name: ")).upper()
            last_name_h_teacher = (input("Enter homeroom teacher's last name: ")).upper()
            class_h_teacher = (input("Enter homeroom teacher's main class room: ")).upper()
            homeroom_teacher_data.append({"first_name":first_name_h_teacher, "last_name":last_name_h_teacher, "classroom": class_h_teacher})
            print(f"{first_name_h_teacher} {last_name_h_teacher} is in charge of class {class_h_teacher}")
            print(f"list of homeroom teacher data: {homeroom_teacher_data}")
        else:
            print("Invalid category. Try again from the available categories.")

def class_info_display(class_name):
    print(f"List of students in class {class_name.upper()}:")
    for student in student_data:
        if student["classroom"] == class_name.upper():
            print(f"{student['first_name']} {student['last_name']}")
    for teacher in homeroom_teacher_data:
        if teacher["classroom"] == class_name.upper():
            print(f"The homeroom teacher of class {class_name} is:\n{teacher['first_name']} {teacher['last_name']}")

def find_student(first_name, last_name):
    print(f"Info display for student: {first_name} {last_name}")
    for student in student_data:
        if student["first_name"] == first_name and student["last_name"] == last_name:
            return student
    return None

def find_teacher(first_name, last_name):
    print(f"Info display for teacher: {first_name} {last_name}")
    for teacher in teacher_data:
        if teacher["first_name"] == first_name and teacher["last_name"] == last_name:
            return teacher
    return None

def find_homeroom_teacher(first_name, last_name):
    print(f"Info display for homeroom teacher: {first_name} {last_name}")
    for h_teacher in homeroom_teacher_data:
        if h_teacher["first_name"] == first_name and h_teacher["last_name"] == last_name:
            return h_teacher
    return None


def manage_menu():
    print("=======MANAGE MENU=======")
    while True:
        choice = (input("Enter the category you want to manage: class - student - teacher - homeroom teacher, or END to go back\n")).lower()
        if choice == "end":
            break
        elif choice == "class":
            class_name = (input("Enter the name of the class you want to manage: ")).upper()
            class_info_display(class_name)
        elif choice == "student":
            student_first_name_to_find = (input("Enter student's first name : ")).upper()
            student_last_name_to_find = (input("Enter student's last name : ")).upper()
            s = find_student(student_first_name_to_find, student_last_name_to_find)

            if not s:
                print("Student not found")
            else:
                print(f"{student_first_name_to_find} {student_last_name_to_find} is in class {s['classroom']}")
                print("Teachers and subjects of this class are: ")
                found_teacher = False
                for teacher in teacher_data:
                    if s['classroom'] in teacher['classes_in_charge']:
                        print(f"{teacher['first_name']} {teacher['last_name']} - {teacher['subject']}")
                        found_teacher = True
                if not found_teacher:
                    print("No teacher found for this class")

        elif choice == "teacher":
            teacher_first_name_to_find = (input("Enter teacher's first name : ")).upper()
            teacher_last_name_to_find = (input("Enter teacher's last name : ")).upper()
            t = find_teacher(teacher_first_name_to_find, teacher_last_name_to_find)
            if not t:
                print("Teacher not found")
            else:
                print(f"{teacher_first_name_to_find} {teacher_last_name_to_find} is teaching the following classes {t['classes_in_charge']}")

        elif choice == "homeroom teacher":
            h_teacher_first_name_to_find = (input("Enter homeroom teacher's first name : ")).upper()
            h_teacher_last_name_to_find = (input("Enter homeroom teacher's last name : ")).upper()
            h = find_homeroom_teacher(h_teacher_first_name_to_find, h_teacher_last_name_to_find)
            if not h:
                print("Homeroom teacher not found")
            else:
                class_name = h['classroom']
                print(f"Leads class {class_name} with the following students :")
                class_students = [s for s in student_data if s['classroom'] == class_name.upper()]
                if class_students:
                    for s in class_students:
                        print(f"- {s['first_name']} {s['last_name']}")
                else:
                    print("No student found for this class")


while True:
    command = (input("Enter command from available commands: create, manage, end.\n")).lower()
    if command == "create":
        create_menu()
    elif command == "manage":
        manage_menu()
    elif command == "end":
        print("Program ended. Bye!")
        break
    else:
        print("Invalid command. Try again.")