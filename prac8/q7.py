class A:
    def check():
        print("Check-A")

class B(A):
    pass

class D(A):
    def check():
        print("Check-D")

class C(B):
    def check():
        print("Check-C")

class E(B,D):
    pass

# ==========================

# class A:
#     def check():
#         print("Check-A")
# class F:
#     def check():
#         print("Check-F")

# class B(A):
#     pass

# class C(F):
#     def check():
#         print("Check-C")

# class D(F):
#     def check():
#         print("Check-D")

# class E(B,C,D):
#     pass

a1=E()
a1.check()



