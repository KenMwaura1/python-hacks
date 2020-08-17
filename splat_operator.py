""" The splat operator provides an efficient way to unpack lists of args """

test_dict = {'x': 6, 'y': 7, 'z': 8}
test_list = [9, 10, 11]
*a, = test_dict.keys()
*b, = test_dict.values()
*c, = test_list
print(a)
print(b)
print(c)
