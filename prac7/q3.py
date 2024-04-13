# Write a Python program to read first n lines of a file
file_name = input("Enter file name: ")
n = int(input("Enter number of lines to read: "))
with open(file_name) as file:
    for i in range(n):
        print(file.readline())

