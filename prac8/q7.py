class A:
    def check(self):
        print("Check-A")

class B(A):
    pass

class D(A):
    def check(self):
        print("Check-D")

class C(B):
    def check(self):
        print("Check-C")

class E(B, D):
    pass

a1 = E()
a1.check()

# ==========================

class A:
    def check(self):
        print("Check-A")
class F:
    def check(self):
        print("Check-F")

class B(A):
    pass

class C(F):
    def check(self):
        print("Check-C")

class D(F):
    def check(self):
        print("Check-D")

class E(B,C,D):
    pass

a1 = E()
a1.check()
