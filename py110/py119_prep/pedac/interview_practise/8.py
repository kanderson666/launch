"""
Problem 8   4min
Create a function that takes a non-empty string as an argument. 
The string consists entirely of lowercase alphabetic characters. 
The function should return the length of the longest vowel substring. 
The vowels of interest are "a", "e", "i", "o", and "u".

Problem:
    - Find longest streak of vowels in string
    Input:
        - String
    Output:
        - Int (streak length)
Algo:
    - Make constant with all vowels
    - Iterate through each char in string
        - If char in constant
            - add 1 to count
            - Update longest streak if needed
    Return longest streak

"""
VOWELS = 'aeiou'
def longest_vowel_substring(string):
    longest_streak = 0
    current_streak = 0
    for char in string:
        if char not in VOWELS:
            current_streak = 0
            continue
        current_streak += 1
        if current_streak > longest_streak:
            longest_streak = current_streak
    return longest_streak

print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)
