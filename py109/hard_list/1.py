# Problem 1: Rotate a list in-place
# ---------------------------------
# Write a function rotate(lst, k) that:
# - Rotates the list lst to the right by k positions.
# - Modifies the list in-place and also returns it.
# - Handles:
#   - k larger than the length of the list (use modulo).
#   - k = 0 or negative k (negative means rotate left).
#
# Examples:
# [1, 2, 3, 4, 5], k = 2  -> [4, 5, 1, 2, 3]
# [1, 2, 3, 4, 5], k = -1 -> [2, 3, 4, 5, 1]

def rotate(lst, k):
    # your code here
    pass


# Test cases
nums1 = [1, 2, 3, 4, 5]
print(rotate(nums1, 2))     # Expected: [4, 5, 1, 2, 3]

nums2 = [1, 2, 3, 4, 5]
print(rotate(nums2, -1))    # Expected: [2, 3, 4, 5, 1]

nums3 = [1, 2, 3]
print(rotate(nums3, 5))     # Expected: [2, 3, 1]

nums4 = []
print(rotate(nums4, 3))     # Expected: []
