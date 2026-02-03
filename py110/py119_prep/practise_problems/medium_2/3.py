# Your code goes here
"""
Problem:
    - Determine if triangle is valid, right, acute or obtese, given 3 angles as input
    Input:
        - 3x integer angles
    Output:
        - String (type of triangle)
    Rules:
        - Sum of 3 angles must equal 180
        - Every angle greater than 0
        - Inputs will be integer, representing degress
Data:
    - 3x int input
    - string output
    - list to store int inputs
Algo:
    - put 3x inputs into list
    - Sort list
    - Test if invalid triangle (helper)
        - lowest # is greater than 0
        - Test if all 3 angles equal 180
        - If either no, return True
    - Check if 90 in list
        - If yes, return right
    - Check if biggest angle greater than 90
        - If yes, return obtuse
    - Otherwise, return Acute
"""
def triangle(side1, side2, side3):
    tri_list = sorted([side1, side2, side3])
    if is_invalid_tri(tri_list):
        return "invalid"
    if 90 in tri_list:
        return 'right'
    if tri_list[-1] > 90:
        return 'obtuse'
    return 'acute'

def is_invalid_tri(tri_list):
    if tri_list[0] <= 0:
        return True
    if sum(tri_list) != 180:
        return True
    return False


print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True
