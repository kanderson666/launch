"""
How to make dict comprehension
"""

my_list_of_tuples = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]

my_dict = {key: value for key, value in my_list_of_tuples}

for key, value in my_list_of_tuples:
    print(key,value)
print(my_dict)
