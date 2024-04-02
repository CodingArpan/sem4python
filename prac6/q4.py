def min_max(lst):
    min = lst[0]
    max = lst[0]
    for i in range(1, len(lst)):
        if lst[i] < min:
            min = lst[i]
        if lst[i] > max:
            max = lst[i]
    tup = (min, max)
    return tup


val=min_max([5, 3, 2, 1, 4, 6, 7, 8, 9, 10])
print(val)
