"""
Given the following data structure, return a new list identical in 
structure to the original but, with each number incremented by 1. 
Do not modify the original data structure. Use a comprehension.

"""
lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

# just for loops
# new_lst = []
# for dct in lst:
#     new_lst.append({})
#     for key, value in dct.items():
#         new_lst[-1][key] = value + 1
# print(new_lst)

# 1 comprehension {dict}
# new_lst = []
# for dct in lst:
#     new_lst.append({key : value + 1 for key, value in dct.items()})

# 2 comprehensions ([{dict} list])
new_lst = [{key : value + 1 for key, value in dct.items()} for dct in lst]

print(new_lst)

# Expected:
# [{'a': 2}, {'b': 3, 'c': 4}, {'d': 5, 'e': 6, 'f': 7}]