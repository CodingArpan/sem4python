lst =[11,55,52,71,89,45,25,36,85,96,52]
lstcopy=lst.copy()
lst.sort()
print(lst)

for i in range(len(lstcopy)):
    for j in range(len(lstcopy)-1):
        if lstcopy[j] > lstcopy[j+1]:
            lstcopy[j], lstcopy[j+1] = lstcopy[j+1], lstcopy[j]
            


print(lstcopy)
