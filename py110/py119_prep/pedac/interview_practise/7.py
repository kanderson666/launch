"""
Problem 7   6min 15sec
Create a function that takes a list of integers as an argument and returns the number of identical pairs of integers in that list. 
For instance, the number of identical pairs in [1, 2, 3, 2, 1] is 2: occurrences each of both 2 and 1.

If the list is empty or contains exactly one value, return 0.

If a certain number occurs more than twice, count each complete pair once. 
For instance, for [1, 1, 1, 1] and [2, 2, 2, 2, 2], the function should return 2. 
The first list contains two complete pairs while the second has an extra 2 that isn't part of the other two pairs.

Problem:
    - Count number of pairs of identical numbers in list
    Input:
        - List of ints
    Output:
        - Int (number of pairs)
    Rules:
        - If 3 of same #, only 1 complete pair. 4 of same # is 2 pairs
        - If size of list is less than 2, return 0
Data:
    - Set to track nums seen
Algo:
    - If size of list is smaller than 2, return 0
    - Iterate through each num in list
        - If num already seen, continue
        - Add count of num // 2 to total count of pairs
    - Return total
"""
def pairs(lst):
    if len(lst) < 2:
        return 0
    nums_seen = set()

    num_pairs = 0
    for num in lst:
        if num in nums_seen:
            continue
        num_pairs += lst.count(num) // 2
        nums_seen.add(num)
    return num_pairs


print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
print(pairs([]) == 0)
print(pairs([23]) == 0)
print(pairs([997, 997]) == 1)
print(pairs([32, 32, 32]) == 1)
print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)
