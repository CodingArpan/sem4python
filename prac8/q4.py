class Hospital:
    def __init__(self,pname,pno,pdisease):
        self.pname=pname
        self.pno=pno
        self.pdisease=pdisease
        
p1 = Hospital("John",101,"Fever")
setattr(p1,"pno",102)
print(getattr(p1,"pno"))
setattr(p1,"pmob",1234567890)
print(getattr(p1,"pmob"))
print(hasattr(p1,"pmob"))
print(delattr(p1, "pdisease"))
print(hasattr(p1,"pdisease"))

print(Hospital.__dict__)
print(Hospital.__doc__)
print(Hospital.__name__)
print(Hospital.__module__)
print(Hospital.__bases__)

del p1
