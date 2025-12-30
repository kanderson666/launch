def non_mutating_delete(lst):
    return lst[:-1]

lst = [1, 2, 3]

print(non_mutating_delete(lst) == [1, 2]) #=> True
print(lst == [1, 2, 3]) #=> True