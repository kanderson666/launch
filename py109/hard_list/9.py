# 4. Flatten a list of lists one level
#
# Write a function `flatten_one_level(lst)` that takes a list which may contain
# other lists as elements, and returns a NEW list with only one level of nesting removed.
#
# Example: [1, [2, 3], 4, [5, 6]] -> [1, 2, 3, 4, 5, 6]
#
# Rules:
# - Only flatten ONE level: if an inner element is itself a list, extend the result with its elements.
# - If an element is NOT a list, just append it.

def flatten_one_level(lst):
    if not lst:
        return []
    result = []
    for item in lst:
        if isinstance(item, list):
            for nested in item:
                result.append(nested)
        else:
            result.append(item)
    return result

# Test cases
print(flatten_one_level([1, [2, 3], 4, [5, 6]])) # [1, 2, 3, 4, 5, 6]
print(flatten_one_level([[1, 2], [3], [4, 5]])) # [1, 2, 3, 4, 5]
print(flatten_one_level([1, 2, 3])) # [1, 2, 3]
print(flatten_one_level([])) # []
print(flatten_one_level([[1, [2, 3]], 4])) # [1, [2, 3], 4]  (only flattened one level, inner [2, 3] stays)