class Student:
    cnt = 0

    def __init__(self):
        Student.cnt += 1

    def get_value(self):
        self.enr_no = input("Enrollment Number: ")
        self.name = input("Name: ")
        self.branch = input("Branch: ")

    def print_value(self):
        print("Enrollment Number: ", self.enr_no)
        print("Name: ", self.name)
        print("Branch: ", self.branch)
    @staticmethod
    def show():
        print("Total number of students: ", Student.cnt)

for i in range(3):
    s = Student()
    s.get_value()
    s.print_value()

Student.show()