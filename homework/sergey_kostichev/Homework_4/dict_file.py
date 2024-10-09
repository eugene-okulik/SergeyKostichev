my_dict = {
    "tuple": (234, "Berlin", 897, None, False, 10),
    "list": [1999, "New York", 8, 4.444, 8.99, "EUR"],
    "dict": {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5},
    "set": {1, 8, 9, 1, 3, 2, 2, 1, 8, 1989, 78},
}

print(my_dict["tuple"][-1])

my_dict["list"].append(7888)
my_dict["list"].pop(1)

my_dict["dict"]['i am a tuple'] = 'I am lying'
del my_dict["dict"]["three"]

my_dict["set"].add(666)
my_dict["set"].remove(1)
