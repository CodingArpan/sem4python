# Write a program to create and initialize the tuple. Also remove 3rd element from tuple

# Create and initialize the tuple
tup = (1, 2, 3, 4, 5)
tup1= tuple([1, 2, 3, 4, 5])
print(tup)
print(tup1)
# Remove 3rd element from tuple
tup = tup[:2] + tup[3:]
print(tup)



