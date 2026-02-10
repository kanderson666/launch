"""
Problem 6   6min 15sec
Create a function that takes a string argument and returns a dict object in which the keys represent 
the lowercase letters in the string, and the values represent how often the corresponding letter occurs in the string.

Problem:
    - Create a dict of occurances of a lowercase letter in a string 
    Input:
        - String
    Output:
        - Dict (lowercase letter : num_occurances)
    Rules:
        - Lowercase only- ignore uppercase and punctuation
Data:
    - Set to track characters seen

Algo:
    - Iterate through each character of string
        - If char isnt lowercase or weve seen it before, continue
        - Add dict member of char : char_count
    Return dict

"""

def count_letters(string):
    seen_chars = set()
    result = {}

    for char in string:
        if not char.islower() or char in seen_chars:
            continue
        result[char] = string.count(char)
    return result



expected = {'w': 1, 'o': 2, 'e': 3, 'b': 1, 'g': 1, 'n': 1}
print(count_letters('woebegone') == expected)

expected = {'l': 1, 'o': 1, 'w': 1, 'e': 4, 'r': 2,
            'c': 2, 'a': 2, 's': 2, 'u': 1, 'p': 2}
print(count_letters('lowercase/uppercase') == expected)

expected = {'u': 1, 'o': 1, 'i': 1, 's': 1}
print(count_letters('W. E. B. Du Bois') == expected)

print(count_letters('x') == {'x': 1})
print(count_letters('') == {})
print(count_letters('!!!') == {})
