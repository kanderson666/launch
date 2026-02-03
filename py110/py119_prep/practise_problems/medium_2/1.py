"""
Lettercase Percentage Ratio
Write a function that takes a string and returns a dictionary containing the following three properties:

the percentage of characters in the string that are lowercase letters
the percentage of characters that are uppercase letters
the percentage of characters that are neither
All three percentages should be returned as strings whose numeric values lie between "0.00" and "100.00", respectively. 
Each value should be rounded to two decimal points.

You may assume that the string will always contain at least one character.

Problem:
    - Output dict with 3 keys representing upper, lowercase, and neither, 
    with their values being the string equiv of how much of the input string matches that category
    Input:
        - String
    Output:
        - dict (case category (string) : % of string that is that category (string))
    Rules:
        - Input will be at least 1 character
        - dict values need to be strings of floats between 0 and 100
        - dict values need to be rounded to 2 decimal places
Data:
    - string, dict
    - int to track total num characters
Algo:
    - Create dict with keys as upper, lower, neither. Values initiated to 0
    - Iterate through each character in string
        - Add 1 to the respective dict category
        - Increase total count by 1
    - Calculate % of each category to total, rounded to 2 decimal places, store as value of category
"""

def letter_percentages(string):
    result = {
        'lowercase': 0,
        'uppercase': 0,
        'neither': 0,
    }
    
    total_chars = 0
    for char in string:
        if char.isupper():
            result['uppercase'] += 1
        elif char.islower():
            result['lowercase'] += 1
        else:
            result['neither'] += 1
        total_chars += 1
    
    for category, value in result.items():
        result[category] = f'{value / total_chars * 100:.2f}'
    return result


expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)
