"""
Problem 18    6min
Create a function that takes a list of integers as an argument. 
Determine and return the index N for which all numbers with an index less than N sum to the same 
value as the numbers with an index greater than N. 
If there is no index that would make this happen, return -1.

If you are given a list with multiple answers, return the index with the smallest value.

The sum of the numbers to the left of index 0 is 0. 
Likewise, the sum of the numbers to the right of the last element is 0.

Problem:
    - Find first index where all numbers to left of index sum to same value as all numbers to riht of index
    Input:
        - List of ints
    Output:
        - Int (index)
    Rules:
        - If none found, return -1
        - Sum to left at index 0 is 0
        - Sum to right of last index is 0
Data:
    - int for index and sums
Algo:
    - Make an index counter starting at 0
    - sum all ints left of index, compare with sum of all to right
    - if equal, return index
    - If not equal, increase index by 1 until reach end of list
"""

def equal_sum_index(lst):
    idx = 0
    while idx + 1 < len(lst):
        if sum(lst[:idx]) == sum(lst[idx + 1:]):
            return idx
        idx += 1
    return -1

print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)
print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1)

# The following test case could return 0 or 3. Since we're
# supposed to return the smallest correct index, the correct
# return value is 0.
print(equal_sum_index([0, 20, 10, -60, 5, 25]) == 0)
