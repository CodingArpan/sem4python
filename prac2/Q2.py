name = input("Enter your name: ")
enrollment_no = input("Enter your enrollment number: ")
branch = input("Enter your branch: ")
age = input("Enter your age: ")
email = input("Enter your email: ")
mobile_no = input("Enter your mobile number: ")

struct = """
===========================
Your Name : {}
Your Enrollment No : {}
Branch: {}
Age: {} years
Email: {}
Mobile No: {}
===========================
 """
print(struct.format(name, enrollment_no, branch, age, email, mobile_no))
