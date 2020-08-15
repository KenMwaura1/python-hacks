dict1 = {'players': 251, 'audience': 1500}
dict2 = {'audience': 1700, 'matches': 30}
merged_dict = {**dict1, **dict2}  # if any common keys are found the latter keys are used in the merged dict (dict2)
print(merged_dict)
