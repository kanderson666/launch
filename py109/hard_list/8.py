# 3. Group consecutive equal elements
#
# Write a function `group_consecutive(lst)` that returns a NEW list of lists,
# where each inner list contains a “run” of equal elements that were next
# to each other in the original list.
#
# Example: [1, 1, 2, 3, 3, 3, 2] -> [[1, 1], [2], [3, 3, 3], [2]]

def group_consecutive(lst):
    result = []
    last = None
    for num in lst:
        if num != last:
            result.append([])
        result[-1].append(num)
        last = num
    return result

# Test cases
print(group_consecutive([1, 1, 2, 3, 3, 3, 2])) # [[1, 1], [2], [3, 3, 3], [2]]
print(group_consecutive([7, 7, 7])) # [[7, 7, 7]]
print(group_consecutive([1, 2, 3])) # [[1], [2], [3]]
print(group_consecutive([])) # []
print(group_consecutive(['a', 'a', 'b', 'a', 'a'])) # [['a', 'a'], ['b'], ['a', 'a']]