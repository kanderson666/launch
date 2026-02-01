"""
Rotation (Part 2)
Write a function that rotates the last count digits of a number. 
To perform the rotation, move the first of the digits that you want to rotate to the end 
and shift the remaining digits to the left.

Problem:
    - Grab digit from desired position from end of number, place that digit on the end, and shift all other digits up 1

    Input:
        - Integer (number)
        - Integer (index from end of digit to move to end)
    Output:
        - Integer (adjusted number)
    Rules:
        - 
Data:
    - Integer (number input)
    - Integer (index from end)
    Intermediary:
        - String equivalent of number input for digit manipulation
A:
    - Convert number input to string
    - Via slicing, return digits up to index, concatenated with digits after index, followed by digit from index
"""
def rotate_rightmost_digits(num, idx):
    num = str(num)
    return int(num[:-idx] + num[-idx + 1:] + num[-idx]) if idx > 1 else int(num)


print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True