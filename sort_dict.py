def dict1():
    keyval = {}
    # Initiliaze the values
    keyval[3] = 48
    keyval[1] = 10
    keyval[2] = 8
    keyval[5] = 12
    keyval[4] = 254
    keyval[6] = 20
    print("Task 3:-\nKeys and Values sorted",
          "in alphabetical order by the value")
    # Remember this would arrange in aphabetical sequence
    # Convert it to float to mathematical purposes
    print(sorted(keyval.values()))


dict1()

""" ALTERNATIVELY use the collections module """

from collections import Counter

dict2 = {"x": 55, "y": 22, "z": 88}


def dict_sorter(dict):
    print(sorted(Counter(dict).values()))


dict_sorter(dict2)
