"""
Problem 5: Sort by Vowel Count   3min  (not counting 1-liner lambda solution)
Difficulty: Advanced

Create a function that takes a list of strings and returns a new list with the 
strings sorted by the number of vowels they contain, in descending order (most vowels first). 
The vowel count should be case-insensitive. If two strings have the same number of vowels, 
their original relative order should be preserved. The vowels are 'a', 'e', 'i', 'o', 'u'.

"""
VOWELS = 'aeiou'

def sort_by_vowel_count(str_list):
    # str_list.sort(key=vowel_count, reverse=True)
    # return str_list

    return sorted(str_list, key=lambda string: len([char for char in string.casefold() if char in 'VOWELS']), reverse=True)


def vowel_count(string):
    string = string.casefold()

    vowel_chars = [char for char in string if char in VOWELS]
    return len(vowel_chars)

# Test Cases
print(sort_by_vowel_count(['programming', 'is', 'fun', 'and', 'challenging']) == ['programming', 'challenging', 'is', 'fun', 'and'])
print(sort_by_vowel_count(['apple', 'banana', 'kiwi', 'orange']) == ['banana', 'orange', 'apple', 'kiwi'])
print(sort_by_vowel_count(['Hello', 'World', 'AEIOU']) == ['AEIOU', 'Hello', 'World'])
