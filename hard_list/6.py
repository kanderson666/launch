# 1. Rotate a list to the right by k steps
#
# Write a function `rotate_right(lst, k)` that returns a NEW list where the elements
# are rotated to the right by k positions.
#
# Rules:
# - Do NOT use slicing like lst[-k:] + lst[:-k] (try to do it “manually”).
# - Handle k > len(lst) by wrapping around (k can be any non-negative integer).
# - The original list should not be modified.

def rotate_right(lst, k):
    pass  # your code here


# Test cases
print(rotate_right([1, 2, 3, 4, 5], 1))   # [5, 1, 2, 3, 4]
print(rotate_right([1, 2, 3, 4, 5], 2))   # [4, 5, 1, 2, 3]
print(rotate_right([1, 2, 3, 4, 5], 5))   # [1, 2, 3, 4, 5]
print(rotate_right([1, 2, 3, 4, 5], 7))   # [4, 5, 1, 2, 3]
print(rotate_right([], 3))                # []
print(rotate_right([10], 100))            # [10]