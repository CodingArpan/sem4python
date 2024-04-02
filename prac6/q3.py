def sortlist(lst):
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst


lst = [3, 2, 1, 4, 5]

print(sortlist(lst))

