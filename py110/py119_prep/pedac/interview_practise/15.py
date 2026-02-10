"""
Problem 15   timing error (maybe ~7 or 8 mins)
Create a function that takes a string argument that consists entirely of numeric digits 
and computes the greatest product of four consecutive digits in the string. 
The argument will always have more than 4 digits.

Problem:
    - Find highest possible sum for 4 consecutive digits in string
    Input:
        - String of int digits
    Output:
        - Int sum
    Rules:
        - I/P always have 4+ digits
Data:
    - comprehension to sum 4 consecutive digits
    - int to track highest sum seen
Algo:
    - set highest sum to 0
    - Iterate through string, until 4 digits would pass end of string
        - Sum 4 digits from there
        - Check if is highest sum
"""

CONSECUTIVE_NUMS = 4

def greatest_product(digits):
    highest_sum = 0
    for idx in range(len(digits) - CONSECUTIVE_NUMS + 1):
        nums = [int(num) for num in digits[idx:idx + 4]]
        current_sum = product(nums)
        if current_sum > highest_sum:
            highest_sum = current_sum
    return highest_sum

def product(nums):
    total = 1
    for num in nums:
        total *= num 
    return total

print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6
