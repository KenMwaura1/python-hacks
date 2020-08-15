number = 1024
# using map() to separate each element and store it in a list
digit_list = list(map(int, str(number)))
print(digit_list)
# Using list comprehension
digit_list2 = [int(a) for a in str(number)]
print(digit_list2)
# Simplest approach
digit_list3 = list(str(number))
print(digit_list3)