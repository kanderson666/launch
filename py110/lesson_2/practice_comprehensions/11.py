"""
The following dictionary has list values that contains strings. 
Write some code to create a list of every vowel (a, e, i, o, u) 
that appears in the contained strings, then print it.

"""
VOWELS = 'aeiou'
dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

result = ""
for lst in dict1.values():
    for string in lst:
        for char in string:
            if char in VOWELS:
                result += char
list_of_vowels = list(result)
print(list_of_vowels)

# same as 1 comprehension
list_of_vowels = [char for lst in dict1.values() 
                        for string in lst 
                            for char in string 
                                if char in VOWELS]
print(list_of_vowels)

# same as 1-line
list_of_vowels = [char for lst in dict1.values() for string in lst for char in string if char in VOWELS]
print(list_of_vowels)
# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']


# Expected:
# Start by trying to write this using nested loops.

"""
Extra Challenge: Once your nested loop code works, try to refactor the 
code so it uses a single list comprehension. 
(You can print the resulting list outside of the comprehension.)
"""