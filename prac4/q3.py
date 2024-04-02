num = input("Enter a number :")
num = int(num)

lstSet = set()
for i in range(1, num//2):
    if num % i == 0:
        # print(i)
        print(f"{i} * {num/i} = {num/i*i}")
        lstSet.add(i)

print(lstSet)
