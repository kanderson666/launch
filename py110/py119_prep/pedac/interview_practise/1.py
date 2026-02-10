"""  
Problem 1   5min 30sec
Create a function that takes a list of numbers as an argument. 
For each number, determine how many numbers in the list are smaller than it, and place the answer in a list. 
Return the resulting list.

When counting numbers, only count unique values. 
That is, if a number occurs multiple times in the list, it should only be counted once.

Problem:
    - Count how many different #s are smaller than the current number in a list
    Input:
        - List of int (to compare size)
    Output:
        - List of int (of resulting size comparison)
    Rules:
        - Only count each unique number
        - If 1 num in list, return [0]
Data:
    - Set to get unique values
Algo:
    - If list shorter than 2, return [0]
    - Put list into set
    - Interate through each num in list
        - Iterate through each num in set
            - If set num is less than list num, add 1 to count
        - Put count into result list
"""

def smaller_numbers_than_current(lst):
    if len(lst) < 2:
        return [0]

    result = []
    input_set = set(lst)
    for lst_num in lst:
        count = 0
        for set_num in input_set:
            if set_num < lst_num:
                count += 1
        result.append(count)
    return result


# Examples
print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)
