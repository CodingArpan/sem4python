# Write a program to find the sum of digit of an input number using while loop.

num = input("Enter a number: ")
sum = 0
index=0
while  index < len(num):
    sum += int(num[index])
    index += 1

print(f"The sum of the digits is {sum}.")



