"""
Egyptian Fractions
A Rational Number is any number that can be represented as the result of the division between two integers, e.g., 1/3, 3/2, 22/7, etc. 
The number to the left is called the numerator, and the number to the right is called the denominator.

A Unit Fraction is a rational number where the numerator is 1.

An Egyptian Fraction is the sum of a series of distinct unit fractions (no two are the same), such as:

1   1    1    1
- + - + -- + --
2   3   13   15

Every positive rational number can be written as an Egyptian fraction. For example:

    1   1   1   1
2 = - + - + - + -
    1   2   3   6

Write two functions: 

1. one that takes a Rational number as an argument, and returns a list of the denominators that are part of an Egyptian Fraction 
representation of the number, 

2. takes a list of numbers in the same format, and calculates the resulting Rational number. 

You will need to use the Fraction class provided by the fractions module.

1. Egyptian: 
Problem:
    - Convert Rational number into Egyptian Fraction
    Input:
        - Rational # (3/4)
    Output:
        - List of denomenators of egyptian fraction
    Rules:
        - 
Data:
    - Integer sum of list
Algo:
    - Initiate lst_sum to Fraction(0, 0)
    - Initiate denomenator to 1
    - While lst_sum < goal (input)
        - If lst_sum + 1/denomenator == goal
            - add denomenator to lst
            - return lst
        - If lst_sum + 1/denomenator < goal
            - add denomenator to lst
        - denomenator += 1
"""
from fractions import Fraction

def egyptian(goal):
    result = []
    lst_sum = 0
    denomenator = 1
    while lst_sum < goal:
        new_fraction = Fraction(1,denomenator)

        if lst_sum + new_fraction <= goal:
            result += [denomenator]
            lst_sum += new_fraction

        denomenator += 1
    return result

"""
2. Unegyptian:

"""
def unegyptian(lst):
    lst_sum = 0
    for denomenator in lst:
        lst_sum += Fraction(1, denomenator)
    return lst_sum


# Using the egyptian function
# Your results may differ for these first 3 examples
print(egyptian(Fraction(2, 1)))      # [1, 2, 3, 6]
print(egyptian(Fraction(137, 60)))   # [1, 2, 3, 4, 5]
print(egyptian(Fraction(3, 1)))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 230, 57960]

# Using the unegyptian function
# All of these examples should print True
print(unegyptian(egyptian(Fraction(1, 2))) == Fraction(1, 2))
print(unegyptian(egyptian(Fraction(3, 4))) == Fraction(3, 4))
print(unegyptian(egyptian(Fraction(39, 20))) == Fraction(39, 20))
print(unegyptian(egyptian(Fraction(127, 130))) == Fraction(127, 130))
print(unegyptian(egyptian(Fraction(5, 7))) == Fraction(5, 7))
print(unegyptian(egyptian(Fraction(1, 1))) == Fraction(1, 1))
print(unegyptian(egyptian(Fraction(2, 1))) == Fraction(2, 1))
print(unegyptian(egyptian(Fraction(3, 1))) == Fraction(3, 1))
