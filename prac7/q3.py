# Write a Python program to read first n lines of a file

def read_lines(file_name, n):
    with open(file_name) as file:
        for i in range(n):
            print(file.readline())

file_name = input("Enter file name: ")
n = int(input("Enter number of lines to read: "))
read_lines(file_name, n)