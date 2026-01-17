"""
Given the following data structure return a new list identical 
in structure to the original, but containing only the numbers 
that are multiples of 3.

"""
lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

new_lst = [[num for num in sublist if num % 3 == 0] for sublist in lst]
print(new_lst)

# Expected:
# [[], [3, 12], [9], [15, 18]]
