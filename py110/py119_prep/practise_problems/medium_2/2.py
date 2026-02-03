"""
Triangle Sides
A triangle is classified as follows:

Equilateral: All three sides have the same length.
Isosceles: Two sides have the same length, while the third is different.
Scalene: All three sides have different lengths.
To be a valid triangle, the sum of the lengths of the two shortest sides must be greater than the length of the longest side, 
and every side must have a length greater than 0. If either of these conditions is not satisfied, the triangle is invalid.

Write a function that takes the lengths of the three sides of a triangle as arguments and returns one of the following four 
strings representing the triangle's classification: 'equilateral', 'isosceles', 'scalene', or 'invalid'.

Problem:
    - Determine type of triangle- eguil, isos, scal, or invalid
    Input:
        - 3x int (lengths of side of triangle)
    Output:
        - string (type of triangle)
    Rules:
        - invalid if sum of 2 shortest sides less than length of longest side
        - every side need length longer than 0
Data:
    - 3x ints (input)
    - string output
    Intermediary:
        - List to store inputs
        - set to determine type of triangle
Algo:
    - Put inputs in list
    - sort list
    - check if valid triangle
        - ensure smallest item in list > 0
        - ensure smallest 2 items > biggest item
        - if either no, invalid
    - put list into set
    - length of set determine type of triangle
"""

def triangle(side1, side2, side3):
    my_lst = [side1, side2, side3]
    my_lst.sort()
    if invalid_triangle(my_lst):
        return "invalid"
    my_set = set(my_lst)
    length = len(my_set)

    match length:
        case 1:
            return 'equilateral'
        case 2:
            return 'isosceles'
        case 3:
            return 'scalene'

def invalid_triangle(lst):
    if lst[0] == 0:
        return True
    if lst[0] + lst[1] <= lst[2]:
        return True
    return False


print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True
