class Overload:
    def __init__(self, a):
        self.a = a

    def __pow__(self, nextObj):
        return self.a ** nextObj.a


obj1 = Overload(2)
obj2 = Overload(3)
print(obj1 ** obj2)
print(obj1 ** obj2)
