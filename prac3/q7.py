# Write a program to count number of digits, upper-case characters and lower-case
# characters from the string.

string = input("Enter a string: ")
num = 0
upper = 0
lower = 0
for i in string:
    
    if i in "0123456789":
        num += 1
    elif ord(i) in range(65, 91):
        upper += 1
    elif ord(i) in range(97, 123):
        lower += 1
print(f"Number of digits: {num}")
print(f"Number of upper-case characters: {upper}")
print(f"Number of lower-case characters: {lower}")
