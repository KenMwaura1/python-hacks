""" Reverse a list using the slicing approach """


def list_reverse(lst):
    list1 = lst[::-1]
    return list1


list2 = [5, 6, 8, 7, 4, 9, 3, ]
print(list_reverse(list2))
