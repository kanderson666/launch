# Problem 3: Longest increasing contiguous subarray
# -------------------------------------------------
# Write a function longest_increasing_run(nums) that:
# - Takes a list of integers nums.
# - Returns a NEW list that is the longest contiguous subarray where
#   each element is strictly greater than the previous element.
# - If there are multiple with the same maximum length, return the first one.
# - For an empty list, return [].
#
# Example:
# [1, 2, 2, 3, 4] -> [2, 3, 4] (from indices 2 to 4)

def longest_increasing_run(nums):
    if not nums:
        return nums
    temp_lst = []
    longest_lst = []

    for num in nums:
        if not temp_lst:
            temp_lst.append(num)
            continue
        if num > temp_lst[-1]:
            temp_lst.append(num)
        else:
            if len(temp_lst) > len(longest_lst):
                longest_lst = temp_lst.copy()
            temp_lst.clear()
            temp_lst.append(num)
    if len(temp_lst) > len(longest_lst):
        longest_lst = temp_lst.copy()
    return longest_lst

# Test cases
print(longest_increasing_run([1, 2, 2, 3, 4]))
# Expected: [2, 3, 4]

print(longest_increasing_run([5, 4, 3, 2, 1]))
# Expected: [5]

print(longest_increasing_run([1, 3, 5, 4, 6, 7, 2, 3, 4, 5]))
# Expected: [4, 6, 7] or [2, 3, 4, 5] depending on which is longer
# Here, [2, 3, 4, 5] length 4 > [4, 6, 7] length 3
# So Expected: [2, 3, 4, 5]

print(longest_increasing_run([]))
# Expected: []
