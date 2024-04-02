lst = [88, 45, 8, 6, 77, 15, 2, 3, 95, 46, 52]

elem = input("Enter the element to be searched: ")
elem = int(elem)

if elem in lst:
    print("Element found at index: ", lst.index(elem))
    print("maximum element in the list is: ", max(lst))
    print("minimum element in the list is: ", min(lst))
else:
    print("Element not found")

for i in range(len(lst)):
    if lst[i] == elem:
        print("Element found at index: ", i)
        break
    else:
        print("Element not found")
max = lst[0]
min = lst[0]
for i in range(len(lst)):
    if lst[i] > max:
        max = lst[i]
    if lst[i] < min:
        min = lst[i]
print("maximum element in the list is: ", max)

