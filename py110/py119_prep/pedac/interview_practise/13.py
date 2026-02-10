"""
Problem 13   7min
Create a function that takes two strings as arguments and returns True if some portion of the characters 
in the first string can be rearranged to match the characters in the second. Otherwise, the function should return False.

You may assume that both string arguments only contain lowercase alphabetic characters. 
Neither string will be empty.

Problem:
    - Check if string1 a superset of string2
    Input:
        - 2 strings
    Output:
        - bool
    Rules:
        - lowercase only
Data:
    - Set- check if string1 superset of string2
Algo:
    - Turn both strings into sets
    - Check if string1 a superset of string2
        - If yes, need verify chars with multiple occurances in string2 occur at least that many times in string1
            - If yes, return True
"""

def unscramble(string1, string2):
    for char in string2:
        if string2.count(char) > string1.count(char):
            return False
    return True



print(unscramble('ansucchlohlo', 'launchschool') == True)
print(unscramble('phyarunstole', 'pythonrules') == True)
print(unscramble('phyarunstola', 'pythonrules') == False)
print(unscramble('boldface', 'coal') == True)
print(unscramble('olc', 'cool') == False)
