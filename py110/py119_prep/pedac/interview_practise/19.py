"""
Problem 19   2min 15sec
Create a function that takes a list of integers as an argument and returns the integer that appears an odd number of times. 
There will always be exactly one such integer in the input list.

Problem:
    - Find integer in list that appears odd # times
    Input:
        - List of ints
    Output:
        - int occuring odd # times
    Rules:
        - Will always be an answer
Data:
Algo:
    - Iterate through list
        - Check if count of int is odd
            - If yes, return int
"""
def odd_fellow(lst):
    for num in lst:
        if lst.count(num) % 2:
            return num



print(odd_fellow([4]) == 4)
print(odd_fellow([7, 99, 7, 51, 99]) == 51)
print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
print(odd_fellow([0, 0, 0]) == 0)
