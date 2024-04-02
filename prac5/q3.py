d = {"a": 1, "b": 2, "c": 3, "d": 4, "d": 5}

dict = dict(filter(lambda x: x[1] <= 2, d.items()))

print(dict)