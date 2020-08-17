""" one line factorial finder using a lambda function """
from functools import reduce

factorial = (lambda i: reduce(int.__mul__, range(1, i + 1), 1))(4)
print(factorial)