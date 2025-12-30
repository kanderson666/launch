# def find_pairs(nums, target):
#     pairs = []
#     seen = set()
#     for num in nums:
#         complement = target - num
#         if complement in seen and [complement, num] not in pairs and [num, complement] not in pairs:
#             pairs.append([complement, num])
#         seen.add(num)
#     return pairs

# print(find_pairs([1, 2, 3, 4, 3, 2, 1], 5))

def find_pairs(nums1, target):
    pairs = set()
    seen = set()

    nums = nums1.copy()
    nums.sort()
    
    for num in nums:
        complement = target - num
        
        if complement in seen:
            pairs.add(tuple(sorted((complement, num))))
        seen.add(num)
    return pairs

print(find_pairs([1, 2, 3, 4, 3, 2, 1], 6)) # [2, 3], [1, 4]

# Questions:
# a) What will this print?
# b) Is there any bug or potential performance issue related to how duplicates are handled? Explain.
# c) How could you change the way pairs are stored or checked to avoid the in pairs scans?
