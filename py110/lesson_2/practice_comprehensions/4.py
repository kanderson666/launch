"""
Given the following data structure, write some code that uses 
comprehensions to define a dictionary where the key is the first 
item in each sublist, and the value is the second.
"""
from pprint import pp
lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]

# for key, value in lst:
#     # for key, value in sublist:
#     print(key, value)

dct = {key : value for key, value in lst}

pp(dct)


# Expected:
# Pretty printed for clarity
# {
#     'a': 1,
#     'b': 'two',
#     'sea': {'c': 3},
#     'D': ['a', 'b', 'c']
# }