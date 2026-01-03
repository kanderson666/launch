# 5. Longest increasing contiguous subsequence
#
# Write a function `longest_increasing_run(lst)` that returns the LONGEST
# contiguous increasing subsequence in the list.
#
# Increasing means: each next element is strictly greater than the previous one.
#
# Example: [1, 2, 2, 3, 4] -> [2, 3, 4]  (the longest strictly increasing run)
#
# If there are multiple runs with the same maximum length, return the FIRST one.

def longest_increasing_run(lst):
    if not lst:
        return []
    longest_run = []
    current_run = []

    for num in lst:
        if not current_run or num > current_run[-1]:
            current_run.append(num)
            continue
        elif len(current_run) > len(longest_run):
            longest_run = current_run
        current_run = [num]
    if len(current_run) > len(longest_run):
            longest_run = current_run
    return longest_run

# Test cases
print(longest_increasing_run([1, 2, 2, 3, 4])) # [2, 3, 4]
print(longest_increasing_run([5, 4, 3, 2, 1])) # [5]  (no increasing steps, so each element alone is a run)
print(longest_increasing_run([1, 2, 3, 1, 2, 3, 4])) # [1, 2, 3, 4]
print(longest_increasing_run([])) # []  (empty list -> empty run)
print(longest_increasing_run([10])) # [10]