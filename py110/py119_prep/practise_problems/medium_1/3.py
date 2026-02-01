"""
Rotation (Part 3)
Take the number 735291 and rotate it by one digit to the left, getting 352917. 
Next, keep the first digit fixed in place and rotate the remaining digits to get 329175. 
Keep the first two digits fixed in place and rotate again to get 321759. 
Keep the first three digits fixed in place and rotate again to get 321597. 
Finally, keep the first four digits fixed in place and rotate the final two digits to get 321579. 
The resulting number is called the maximum rotation of the original number.

Write a function that takes an integer as an argument and returns the maximum rotation of that integer. 
You can (and probably should) use the rotate_rightmost_digits function from the previous exercise.

Problem:
    - Move each digit from each increasing index until reach end of number
    - After move 1st digit, move NEW 2nd digit (used to be the 3rd digit)
    Input:
        - Integer to be rotated
    Output:
        - Integer after rotation
    Rules:
        - Increment index that you rotate by 1 after each rotation
Data:
    - Integer for input and result
    Intermediary:
        - String to manipulate integer during rotations
Algo:
    - Convert input to string for manipulation
    - Step through each index from beginning of string to end
        - Keep string up to index, plus string after index, plus digit at index
"""
def max_rotation(num):
    num = str(num)
    for idx in range(len(num)):
        num = rotate_rightmost_digits(num, idx)
    return int(num)

def rotate_rightmost_digits(num, idx):
    return num[:idx] + num[idx + 1:] + num[idx]


print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True