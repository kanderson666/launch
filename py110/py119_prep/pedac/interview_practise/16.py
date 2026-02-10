"""
Problem 16   4min 45sec
Create a function that returns the count of distinct case-insensitive alphabetic characters 
and numeric digits that occur more than once in the input string. 
You may assume that the input string contains only alphanumeric characters.

Problem:
    - Count how many different characters appear more than once in string
    Input:
        - String
    Output:
        - Int, count of diff characters
    Rules:
        - input only alphanumeric characters
Data:
    - Set for chars seen
    - Set for chars seen more than once
Algo:
    - Iterate through chars
        - Check if char seen before
            - If no, add to seen set, continue
        - If seen, add to seen multiple set
    - Return length of seen multiple set

"""

def distinct_multiples(string):
    string = string.casefold()

    chars_seen = set()
    seen_multiple = set()

    for char in string:
        if char not in chars_seen:
            chars_seen.add(char)
            continue
        seen_multiple.add(char)
    return len(seen_multiple)

print(distinct_multiples('xyz') == 0)               # (none)
print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
print(distinct_multiples('unununium') == 2)         # u, n
print(distinct_multiples('multiplicity') == 3)      # l, t, i
print(distinct_multiples('7657') == 1)              # 7
print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5
