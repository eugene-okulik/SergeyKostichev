
if __name__ == "__main__":
    my_dict = {
        "tuple": (234, "Berlin", 897, None, False, 0),
        "list": [1999, "New York", 8, 4.444, 8.99, "EUR"],
        "dict": {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5},
        "set": {1, 8, 9, 1, 3, 2, 2, 1, 8, 1989, 78},
    }

    print(my_dict["tuple"][-1])  # Output the last element

    my_dict["list"].append(7888) # add new element in the end of the list
    my_dict["list"].pop(1)       # remove the second element of the list

    my_dict["dict"]['i am a tuple'] = 'I am lying'  # add an element in the dictionary
    del my_dict["dict"]["three"]                    # deleting an element from the dictionary

    my_dict["set"].add(666)   # add an element in the set
    my_dict["set"].remove(1)  # removing an element from the set
