def readStudents():
    file = open("students.csv", "r")
    for line in file:
        data = line.split(",")
        dict1 = dict(name=data[0],roll_no=data[1], age=data[2], cgpa=data[3], branch=data[4])
        print(dict1)
    file.close()


def writeStudents():
    file = open("students.csv", "a")
    name = input("Enter name: ")
    roll = input("Enter roll: ")
    age = input("Enter age: ")
    cgpa = input("Enter cgpa: ")
    branch = input("Enter branch: ")
    file.writelines(name + "," + roll + "," + age +
               "," + cgpa + "," + branch + ",\n")
    file.close()


def main():
    print("1. Read students")
    print("2. Write students")
    choice = int(input("Enter choice: "))
    if choice == 1:
        readStudents()
    elif choice == 2:
        writeStudents()
    else:
        print("Invalid choice")
    main()

main()
