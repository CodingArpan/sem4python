# Create a tuple with name courses and initialize it with JAVA, PHP, C#, Android. Insert
# two items HTML and Python at the 3rd position in tuple.

tup = ('JAVA', 'PHP', 'C#', 'Android')
print(tup)

tup = tup[:2] + ('HTML', 'Python') + tup[2:]
print(tup)



