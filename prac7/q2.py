file1 = open('demo.txt', 'r')
file2 = open('demo2.txt', 'r')

lst1 = file1.readlines()
lst2 = file2.readlines()

concat = zip(lst1, lst2)
for i in concat:
    print(i[0].strip() + i[1].strip())

# for i in range(min(len(lst1), len(lst2))):
#     print(lst1[i].strip() + lst2[i].strip())
