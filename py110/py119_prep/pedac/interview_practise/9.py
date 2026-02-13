"""
Problem 9  3min (built-in method)  17min without
Create a function that takes two string arguments and returns the number of times that the second string occurs in the first string. 
Note that overlapping strings don't count: 'babab' contains 1 instance of 'bab', not 2.

You may assume that the second argument is never an empty string.

Problem:
    - Find how many times 2nd string is found in 1st string, w/o overlaps
    Input:
        - 2 strings
    Output:
        - int (num of occurances)
    Rules:
        - Occurances cant overlap
        - 2nd string never empty
Data:
    - int for start of search in string1
Algo:
    - While string2 in string1[start:]
        - Find index of 1st occurance of string2 in string1
        - Increase count by 1
        - Change start to index + len of string2
    - Return count

"""

def count_substrings(string1, string2):
    count = 0
    start_idx = 0

    while start_idx < len(string1) and string2 in string1[start_idx: ]:
        start_idx += string1[start_idx:].index(string2) + len(string2)
        count += 1
    return count
    # return string1.count(string2) Works with built-in method

"""
Algo:
    - Set start_idx to 0
    - Repeat while string2 can fit in string1 from start_idx
        - Check if slice from start_idx of string1 to len of string 2 matches string2
            - If yes, add 1 to count, set start_idx to last char of match
        - Increase start_idx by 1

def count_substrings(string1, string2):
    start_idx = 0
    count = 0

    while start_idx + len(string2) <= len(string1):
        if string1[start_idx: start_idx + len(string2)] == string2:
            count += 1
            start_idx += len(string2) - 1
        start_idx += 1
    return count
"""

print(count_substrings('babab', 'bab') == 1)
print(count_substrings('babab', 'ba') == 2)
print(count_substrings('babab', 'b') == 3)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('', 'x') == 0)
print(count_substrings('bbbaabbbbaab', 'baab') == 2)
print(count_substrings('bbbaabbbbaab', 'bbaab') == 2)
print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1)


