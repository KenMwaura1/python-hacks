""" check for duplicates in a list """

from collections import Counter


def unique(lst: list):
    if len(lst) == len(set(lst)):
        print("Total items checked are unique")
    else:
        lst2 = [(a, b) for a, b in
                Counter(lst).most_common()]  # returns a list of tuples with item,no.times found in the list
        for a, b in lst2:
            if b > 1:
                print(f"Duplicated items found : {a} is duplicated {b} times")


unique([0, 2, 4, 6, 8])

unique([1, 3, 3, 5, 9, 8, 5, 8, 1, 1])
