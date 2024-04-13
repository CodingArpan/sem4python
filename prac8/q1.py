class Employee:

    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def display(self):
        print("Name: ", self.name)
        print("Department: ", self.department)
        print("Salary: ", self.salary)

sujal=Employee("Sujal", "IT", 100000)
sujal.display()
Shaswat=Employee("Shaswat", "IT", 500000)
Shaswat.display()
prabhat=Employee("Prabhat", "IT", 1000000)
prabhat.display()