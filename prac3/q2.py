# Write a program to check special number. If the sum of the factorial of digits of a number (N) is equal to the number itself, the number (N) is called a special number.


num = input("Enter a number: ")
sum = 0
for c in num:
    n = int(c)
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    sum += factorial
# 145
if (sum == int(num)):
    print(f"{num} is a special number.")
else:
    print(f"{num} is not a special number.")
