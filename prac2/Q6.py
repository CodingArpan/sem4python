# Write a python program to for library charges a fine for books returned late. Following
# are the fines:
# First five days: 40 paisa per day.
# Six to ten day: 65 paisa per day.
# Above ten days: 80 paisa per day

# Solution:
days = int(input("Enter the number of days: "))
if days <= 5:
    fine = days * 0.40
elif days <= 10:
    fine = days * 0.65
else:
    fine = days * 0.80
print("The fine for the given days is", fine)

