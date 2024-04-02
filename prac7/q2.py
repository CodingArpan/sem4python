file1 = open('demo.txt', 'r')
file2 = open('demo2.txt', 'r')

lst1 = file1.readlines()
lst2 = file2.readlines()


for i in range(min(len(lst1), len(lst2))):
    print(lst1[i].strip() + lst2[i].strip())
