""" 
Problem 4   15min
Create a function that takes a list of integers as an argument and returns a tuple of two numbers that are closest together in value. 
If there are multiple pairs that are equally close, return the pair that occurs first in the list.

Problem:
    -  Find 2 numbers from a list that are closest together
    Input:
        - List of ints
    Output:
        - Tuple of 2 closest nums
    Rules:
        - If 2 pairs equally close, return first pair
Data:
    - List, tuple
    - Int of difference between closest pair
Algo:
    - Set difference to high number
    - Iterate through list for each num
        - Iterate through list again from current num + 1 to end
            - Find difference between 2 nums abs(num1 - num2)
            - If difference is smaller than difference between current pair, these nums are the new pair

"""
def closest_numbers(lst):
    pair_difference = float('inf')

    for idx, first_num in enumerate(lst):
        if idx + 1 == len(lst):
            break
        for second_num in lst[idx + 1:]:
            difference = abs(first_num - second_num)
            if difference < pair_difference:
                closest_pair = (first_num, second_num)
                pair_difference = difference

    return closest_pair



print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))
