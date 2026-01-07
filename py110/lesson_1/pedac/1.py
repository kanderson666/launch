"""
PROBLEM:

Given a string, write a function `palindrome_substrings` which returns
all the palindromic substrings of the string that are 2 or more characters
long. Palindrome detection should be case-sensitive.
"""

# Test cases:
# Comments show expected return values
palindrome_substrings("abcddcbA")   # ["bcddcb", "cddc", "dd"]
palindrome_substrings("palindrome") # []
palindrome_substrings("")           # []
palindrome_substrings("repaper")    # ['repaper', 'epape', 'pap']
palindrome_substrings("supercalifragilisticexpialidocious") # ["ili"]

"""
P:
Understand the Problem:
    Input: string
    Output: list of strings
    Rules:
        Explicit req:
            -return all palindromes within string of 2+ characters
            -palindromes case-sensitive
        Implicit req:
            -If string empty, return empty list
            -if no palindromes, return empty list

D: 
Data Structure:
    -List

A:
Algorithm:
  - Declare a result variable and initialize it to an empty list.
  - Create a list named substr_list that contains all the substrings
    of the input string that are at least 2 characters long.
  - Loop through the words in the substr_list list.
  - If the word is a palindrome, append it to the result list.
  - Return the result list.
"""
