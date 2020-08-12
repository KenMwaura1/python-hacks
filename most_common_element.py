""" Return the most common element in a list"""
number_list = [1, 8, 7, 5, 4, 5, 9, 6, 7, 5, 8, 3]
print(max(set(number_list), key=number_list.count))  # Returns 5

# OR use the collections module
from collections import Counter

print(Counter(number_list).most_common())
"""returns a list of most common items [(5, 3), (8, 2), (7, 2), (1, 1), (4, 1), (9, 1), (6, 1), (3, 1)]"""
