"""
Sum Square - Square Sum
Write a function that computes the difference between the square of the sum of the first count 
positive integers and the sum of the squares of the first count positive integers.

Problem:
    - Calculate 2 sums, then subtract one from the other
        - 1. sum from 1 up to a number, then square that sum
        - 2. Square each num from 1 up to a number, then sum those squares
        - 3. Do 1 - 2
    Input:
        - Integer (limit for each calc)
    Output:
        - Integer (result of the maths)
Data:
    - Integer x2
    Intermediary:
        - List for comprehension?
        - Or integers for step-by-step math
Algo:
    - sum a list comprehension of range, then square it and subtract another summed comprehension
    of range that squares as it builds
"""

def sum_square_difference(limit):
    return sum(range(1, limit + 1))**2 - sum(num**2 for num in range(1, limit + 1))


print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True
