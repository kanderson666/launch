# 2. Remove duplicates while preserving order
#
# Write a function `unique_in_order(lst)` that returns a NEW list containing
# the elements of lst, but with duplicates removed, keeping only the first
# occurrence of each element in their original order.
#
# Example: [3, 1, 3, 2, 1] -> [3, 1, 2]
#
# Rules:
# - Do NOT use set(lst) (that would lose the order).
# - Do it “manually” using basic operations.

def unique_in_order(lst):
    if not lst:
        return []
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result


# Test cases
print(unique_in_order([3, 1, 3, 2, 1]))              # [3, 1, 2]
print(unique_in_order([1, 1, 1, 1]))                 # [1]
print(unique_in_order([1, 2, 3, 4]))                 # [1, 2, 3, 4]
print(unique_in_order([]))                           # []
print(unique_in_order(['a', 'b', 'a', 'c', 'b']))    # ['a', 'b', 'c']