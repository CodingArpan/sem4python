lst = [23, 45, 8, 6, 77, 15, 2, 3, 95, 46, 52]
newlst = [lst[(i+1) % len(lst)] for i in range(len(lst))]
print(newlst)
