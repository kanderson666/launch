"""
Problem 10   # 13min (2min to understand what problem is asking)
Create a function that takes a string of digits as an argument and returns the number of even-numbered substrings that can be formed. 
For example, in the case of '1432', the even-numbered substrings are '14', '1432', '4', '432', '32', and '2', for a total of 6 substrings.

If a substring occurs more than once, you should count each occurrence as a separate substring.

Problem:
    - Find number of substrings can form an even number (last digit is even #)
    Input:
        - String of digits
    Output:
        - Int num of possible even num substrings
    Rules:
        - If same substring occur, count both
Data:
    - Int to check if digit is even #
Algo:
    - Start at end of string, iterate through each digit backwards
        - If digit is odd, continue
        - Num possibilities with ending digit even is equal to num digits remaining

"""

def even_substrings(string_of_digits):
    digits_reversed = string_of_digits[::-1]
    total = 0

    for idx, digit in enumerate(digits_reversed):
        if int(digit) % 2:
            continue
        total += len(digits_reversed) - idx
    return total


print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)
