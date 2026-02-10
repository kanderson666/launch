"""
Problem 11   11.5min
Create a function that takes a nonempty string as an argument and returns a tuple consisting of a string and an integer. 
If we call the string argument s, the string component of the returned tuple t, and the integer component of the 
tuple k, then s, t, and k must be related to each other such that s == t * k. 
The values of t and k should be the shortest possible substring and the largest possible repeat count that satisfies this equation.

You may assume that the string argument consists entirely of lowercase alphabetic letters.

Problem:
    - Find shortest substring in string that can be used to replicate the entire string
    Input:
        - String
    Output:
        - Tuple (string, int)
            - String is shortest substring possible to create string
            - int is num times substring needs to be repeated to create string
    Rules:
        - Input all lowercase
Data:
    - string to hold substring checking if it creates the string
Algo:
    - Iterate through string
        - build substring
        - check if substring can make string (len string // len substring ) * substring
            - yes, create tuple of substring and len string // len substring

"""
def repeated_substring(string):
    substring = ""
    for char in string:
        substring += char
        duplicates = len(string) // len(substring)
        if substring * duplicates == string:
            return (substring, duplicates)
        

print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
print(repeated_substring('xyxy') == ('xy', 2))
print(repeated_substring('xyz') == ('xyz', 1))
print(repeated_substring('aaaaaaaa') == ('a', 8))
print(repeated_substring('superduper') == ('superduper', 1))
