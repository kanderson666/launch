# 4. Eliminating duplicates while preserving length info
# Given a list of integers that may contain duplicates, build a set of
# numbers that appear MORE THAN ONCE in the list.

# Your code: duplicates = ...

# Test cases
nums = [1, 2, 2, 3, 3, 3, 4]
duplicates = {num for num in nums if nums.count(num) > 1}
# 2 appears 2 times, 3 appears 3 times
assert duplicates == {2, 3}

nums = [10, 20, 30]
duplicates = {num for num in nums if nums.count(num) > 1}
assert duplicates == set()

nums = [5, 5, 5, 5]
duplicates = {num for num in nums if nums.count(num) > 1}
assert duplicates == {5}