import re
mobile = input("Enter mobile number: ")
if re.match('[6-9]\d{9}$', mobile):
    print("Valid mobile number")
else:
    print("Invalid mobile number")
