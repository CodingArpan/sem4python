def printNPrimeNumbers(n):
    count = 0
    num = 2
    while count < n:
        isPrime = True
        for i in range(2, num):
            if num % i == 0:
                isPrime = False
                break
        if isPrime:
            print(num)
            count += 1
        num += 1


printNPrimeNumbers(10)