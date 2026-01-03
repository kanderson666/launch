# Problem 5: Find all triplets that sum to a target
# -------------------------------------------------
# Write a function three_sum(nums, target) that:
# - Takes a list of integers nums and an integer target.
# - Returns a NEW list of triplets [a, b, c] such that:
#   - a + b + c == target
#   - a, b, c are elements from nums at different indices.
# - Triplets must be unique: do not include the same combination more than once,
#   regardless of order (e.g., [1,2,3] is the same as [2,3,1]).
# - The order of triplets in the returned list does not matter, but
#   each triplet itself should be sorted in non-decreasing order.
#
# Example:
# nums = [1, 2, -1, 0, -2, 1], target = 0
# One valid output: [[-2, 1, 1], [-1, 0, 1]]

def three_sum(nums1, target):
    if len(nums1) < 3:
        return nums1
    nums = sorted(nums1)
    result = []
    
    for first_idx in range(0, len(nums) - 2):
        num1 = nums[first_idx]
        
        for second_idx in range(first_idx + 1, len(nums) - 1):
            num2 = nums[second_idx]

            tmp = num1 + num2 
            if (tmp + max(nums) < target):
                continue
            
            for third_idx in range(second_idx + 1, len(nums)):
                num3 = nums[third_idx]

                if tmp + num3 != target:
                    continue

                if [num1, num2, num3] not in result:
                    result.append([num1, num2, num3])
    return result


# Test cases
print(three_sum([1, 2, -1, 0, -2, 1], 0))
# Possible expected triplets (order may differ): [[-2, 1, 1], [-1, 0, 1]]

print(three_sum([0, 0, 0, 0], 0))
# Expected: [[0, 0, 0]] (only one unique triplet)

print(three_sum([1, 2, 3, 4, 5], 50))
# Expected: []

print(three_sum([-4, -1, -1, 0, 1, 2], 0))
# Expected (order may differ): [[-1, -1, 2], [-1, 0, 1]]
