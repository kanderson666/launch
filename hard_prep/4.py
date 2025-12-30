# You want a function remove_in_place(nums, value) that:
# removes all occurrences of value from nums in place
# returns None
# does not create any new list
# Example:
def remove_in_place(nums1, value):
    while value in nums1:
        nums1.remove(value)

nums = [1, 2, 3, 2, 4, 2]
remove_in_place(nums, 2)

print(nums)  # should be [1, 3, 4]

# Questions:
# a) Write this function.
# b) Why is this approach safer than doing for x in nums: nums.remove(value)?
# c) What kinds of bugs can appear when you mutate a list while iterating over it with for x in nums:?