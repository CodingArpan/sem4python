def additionList(list1, list2):
    return [list1[i] + list2[i] for i in range(len(list1))]

val=additionList([1, 2, 3], [4, 5, 6])
print(val)