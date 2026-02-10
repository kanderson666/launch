"""
Problem 5   8min
Create a function that takes a string argument and returns the character that occurs most often in the string. 
If there are multiple characters with the same greatest frequency, return the one that appears first in the string. 
When counting characters, consider uppercase and lowercase versions to be the same.

Problem:
    - Find the most frequent character in the string
    Input:
        - String
    Output:
        - String (character most occuring)
    Rules: 
        - If multiple characters have same occurance, return first one to occur
        - Ignore case
Data:
    - Set to have only unique characters
    - Dict to store char and count

    - String to store casefold string
    - int to store highest count
    - String to store char with highest count
    - Set to store letters tested
Algo:
    - convert string to casefold string
    - Iterate through each char of string
        - Check if char in set of seen chars
            - If yes, continue
        - Check count of char
        - If count higher than current highest count
            - Replace highest char and count
    Return highest char

"""
def most_common_char(string_input):
    lowercase_string = string_input.casefold()

    seen_chars = set()
    highest_count = 0
    highest_char = ""

    for char in lowercase_string:
        if char in seen_chars:
            continue
        count = lowercase_string.count(char)
        if count > highest_count:
            
            highest_char = char
            highest_count = count
    return highest_char

print(most_common_char('Hello World') == 'l')
print(most_common_char('Mississippi') == 'i')
print(most_common_char('Happy birthday!') == 'h')
print(most_common_char('aaaaaAAAA') == 'a')

my_str = 'Peter Piper picked a peck of pickled peppers.'
print(most_common_char(my_str) == 'p')

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e')
