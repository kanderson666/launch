"""
Dict methods:
    Get, setdefault, update, pop/popitem 
Set methods:
    update, remove, union, intersection, isdisjoint
"""

my_dict = {1: 2, 3: 4, 5: 6}
my_dict2 = {5: 7, 8: 9, 10: 11}

# print(my_dict.get(3))
# print(my_dict.get(4, "hi"))

# print(my_dict.setdefault(3, 'hi'))
# print(my_dict.setdefault(6, "hello"))
# print(my_dict)

# print(my_dict.update(my_dict2))
# print(my_dict)

# print(my_dict.pop(3))
# print(my_dict)

print(my_dict.popitem())

my_set = {1, 2, 3, 4, 5}
my_set2 = {4, 5, 6, 7}

# print(my_set.update(my_set2))
# print(my_set)

# print(my_set.remove(4))
# print(my_set)
# print(my_set.remove(8))

# print(my_set.union(my_set2))
# print(my_set)

# print(my_set.intersection(my_set2))

# print(my_set.isdisjoint(my_set2))
