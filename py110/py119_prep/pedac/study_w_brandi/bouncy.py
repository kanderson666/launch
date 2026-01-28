# /*
# BOUNCY COUNT
# Some numbers have only ascending digits, like 123, 3445, 2489, etc.
# Some numbers have only descending digits, like 321, 5443, 9842, etc.
# A number is "bouncy" if it has both ascending and descending digits, like 313, 92543, etc.
# Write a method that takes a list of numbers and counts how many of them are bouncy.
"""
P:
    - Count how many sets of numbers in list have ascending and descending digits within it
Input:
    - List of integers
Output:
    - Integer (count of bouncy integers from input list)
Rules:
    - Empty list returns 0
    - Digits need to ascend and descend
    - Positive numbers only in list

Data:
    - list input
    - Integer numbers from list
    - Integer count output
    Intermediary:
        - Bool ascending
        - Bool descending 
        - string to check through each char of integer from list
        - string to hold last digit

Algo:
    - iterate through each num in list
        - Check if num is bouncy
            - convert num to str
            - iterate through each digit of str
                - store first digit in last_digit variable
                - compare next digit to last
                - if digit larger:
                    - set ascend bool to true
                - if digit smaller:
                    - set descend bool to true
                - update last_digit to current digit
            - if both flags were set, return True
        - If bouncy, increase bouncy_count by 1
"""

def bouncyCount(lst):
    bouncy_count = 0
    
    for num in lst:
        if bouncy(num):
            bouncy_count += 1
    
    return bouncy_count

def bouncy(num):
    ascend = False
    descend = False
    num = str(num)
    last_digit = num[0]

    for digit in num:
        if digit > last_digit:
            ascend = True
        elif digit < last_digit:
            descend = True
        last_digit = digit
    
    if ascend and descend:
        return True
    return False
        
# Python test cases:
print(bouncyCount([]) == 0)
print(bouncyCount([11, 0, 345, 21]) == 0)
print(bouncyCount([121, 4114]) == 2)
print(bouncyCount([176, 442, 80701644]) == 2)
