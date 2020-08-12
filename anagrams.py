""" Check if two strings are anagrams of each other """
from collections import Counter


def anagram_checker(string_1, string_2):
    return Counter(string_1) == Counter(string_2)


anagram_checker('pqrs', 'rqqs')  # evaluates to true

anagram_checker('pqrs', 'rqqs')  # evaluates to false
