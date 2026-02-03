"""
Word to Digit
Write a function that takes a string as an argument and returns that string with every occurrence of a "number word" 
-- 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' -- converted to its corresponding digit character.

You may assume that the string does not contain any punctuation.

Problem:
    - Replaces all occurances of the text-written numbers to its numerical counterpart, given a string
Input:
    - String (sentence)
Output:
    - String (word #s converted to numerical #s)
Rules:
    - Input contains no punctuation
    - input is lowercase
    - words separated by space

Data:
    - String input/output
    - Dict to hold conversions
Algo:
    - Create dict with word : number pairs
    - Split string into components, separated by space
    - iterate through components
        - Check if component in dict
            - If yes, replace component with numerical equivalent (as string) in result string
            - If no, add component as-is to result string
    - Return  
"""
import string

CONVERSIONS = { "one" : "1",
                "two" : "2",
                "three" : "3",
                "four" : "4",
                "five" : "5",
                "six" : "6",
                "seven" : "7",
                "eight" : "8",
                "nine" : "9"
}
def word_to_digit(message):
    result = ""
    for component in message.split(" "):
        if component in CONVERSIONS:
            result += CONVERSIONS[component]
        elif component[:-1] in CONVERSIONS and component[-1] in string.punctuation:
            result += CONVERSIONS[component[:-1]] + component[-1]
        else:
            result += component
        result += " "
    return result.strip()

message = 'Please call me at five, five, five, one two, three, four.'
print(word_to_digit(message) == "Please call me at 5, 5, 5, 1 2, 3, 4.")
# Should print True
