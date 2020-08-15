""" The traditional dict[key] method """
dictionary = {"A":5, "B":8, "C":12}
print(dictionary["B"]) # Returns 8
# print(dictionary["D"]) Throws a KeyError when a key is not found
""" The dict.get method """
print(dictionary.get("A"))  # Returns 5
print(dictionary.get("D")) # Returns None when key is not found preventing a keyError 