# Write a python program to remove i’th character from string

string = input("Enter a string: ")
i = int(input("position of the character to remove: "))
new_string = string[:i] + string[i+1:]
print(f"The new string is: {new_string}")


