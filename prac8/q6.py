class Person:
    name=''
    age=0
    def __init__(self,personName,personAge):
        self.name=personName
        self.age=personAge
    
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)

class SportPerson(Person):
    sport_name=''
    def __init__(self, personName, personAge,sport_name):
        super().__init__(personName, personAge)
        self.sport_name = sport_name

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Sport:",self.sport_name)

sp1=SportPerson("John",22,"Cricket")
p1=Person("arpan",20)

sp1.display()
p1.display()






        




