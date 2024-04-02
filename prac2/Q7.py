# Write a python program to count odd numbers from given three numbers and display
# maximum odd number.

# Solution:
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
max_odd = 0
if a % 2 != 0 and a > max_odd:
    max_odd = a
if b % 2 != 0 and b > max_odd:
    max_odd = b
if c % 2 != 0 and c > max_odd:
    max_odd = c

print("The maximum odd number is", max_odd)
