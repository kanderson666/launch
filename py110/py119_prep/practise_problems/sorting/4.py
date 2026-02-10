"""
Problem 4: Sort by Absolute Difference   1min (lambda)
Difficulty: Advanced


Create a function that takes a list of numbers and a target number. 
It should return a new list with the numbers sorted based on their absolute 
difference from the target number, from the smallest difference to the largest. 
If two numbers have the same absolute difference, their original relative order should be maintained.

"""

def sort_by_difference(num_list, target):
    def sort_it(num):
        return abs(num - target)
    
    # num_list.sort(key=sort_it)
    num_list = sorted(num_list, key=sort_it)

    # num_list.sort(key=lambda num: abs(num - target))
    return num_list

# Test Cases
print(sort_by_difference([9, 5, 1, 8, 3], 6) == [5, 8, 9, 3, 1])
print(sort_by_difference([10, 20, 30, 40], 32) == [30, 40, 20, 10])
print(sort_by_difference([5, 15, 25], 20) == [15, 25, 5])