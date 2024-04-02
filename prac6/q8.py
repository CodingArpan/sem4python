students = [
    {"name": "John", "age": 21},
    {"name": "Jane", "age": 22},
    {"name": "Peter", "age": 23},
    {"name": "Tom", "age": 24},
    {"name": "Alice", "age": 25}
]
sorted_student = sorted(students, key=lambda x: x['age'])
print(sorted_student)
