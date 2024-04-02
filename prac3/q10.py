# Write a python program to check if the substring is present in a given string.

string = input("Enter a string: ")
substring = input("Enter the substring you want to check: ")
if substring in string:
    print("The substring is present in the string.")
else:
    print("The substring is not present in the string.")