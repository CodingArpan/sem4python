
file = open('demo.txt', 'r')
maximum = ''
for line in file:
    lst = line.split(" ")
    for word in lst:
        if len(word) > len(maximum):
            maximum = word

print("The longest word is: ", maximum)