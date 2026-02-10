"""
Problem 2   22min?   7min 2nd time
Create a function that takes a list of integers as an argument. 
The function should return the minimum sum of 5 consecutive numbers in the list. 
If the list contains fewer than 5 elements, the function should return None.

Problem:
    - Find the lowest sum of 5 consective #s in a list of #s
    Input:
        - List of integers to check
    Output:
        - Integer (lowest sum)
    Intermediary:
        - int to track lowest sum so far
        - int for length of list
Data:
    - List & ints described above
Algo:
    - Get length of list
    - Incrementally check groups of 5 in list, starting at beginning, until 5th element would be outside of list
    - Check if sum is less than previous lowest sum

    - Find last element that would begin the check of 5 (if size 6, last index is 5, last start index is 1)
    [0, 1, 2, 3, 4, 5, 6]
     1  2  3  4  5  6  7
"""
CHECK_SIZE = 5

def minimum_sum(lst_input):
    length = len(lst_input)
    if length < CHECK_SIZE:
        return None
    lowest_sum = abs(sum(lst_input))
    start_index = 0

    while start_index + CHECK_SIZE <= length:
        current_sum = sum(lst_input[start_index: start_index + CHECK_SIZE])
        if current_sum < lowest_sum:
            lowest_sum = current_sum
        start_index += 1
    return lowest_sum



print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)
