from abc import ABC, abstractmethod
class demo:
    val=20
    @staticmethod
    def setVal(val):
        demo.val=val

print(demo.val)
demo.setVal(30)
print(demo.val)


