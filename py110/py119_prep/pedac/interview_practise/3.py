"""
Problem 3  22min    9min 45sec 2nd try  (at bottom)
Create a function that takes a string argument and returns a copy of the string with every second character 
in every third word converted to uppercase. Other characters should remain the same.

Problem:
    - For every 3rd word in a string, convert every other letter in that word to uppercase
    Input:
        - String
    Output:
        - String w letters altered
    Rules:
        - Every other letter uppercased, starting w 2nd letter of word
        - Leave all other characters
Data:
    - Strings
    - List of words
Algo:
    - Split string into words
    - Ensure there at least 3 words
        - If not, return input string
    - Iterate through list of words using idx (every other 3rd word)
        - Ensure word is at least 2 characters
            - If not, continue on to next word
        - Set current_word = ""
        - Iterate through each character of word
            - if index is odd and character is a letter
                - Convert char to uppercase
            - Add char to current_word string
        - Replace word in word_list with current_word
    - Join words in word list and return
"""

def to_weird_case(input_string):
    word_lst = input_string.split(' ')
    if len(word_lst) < 3:
        return input_string

    for word_idx, word in enumerate(word_lst):
        if (word_idx + 1) % 3:
            continue
        if len(word) < 2:
            continue

        current_word = ""
        
        for idx, char in enumerate(word_lst[word_idx]):
            if not char.isalpha() or (idx + 1) % 2:
                current_word += char
                continue

            current_word += char.upper()

        word_lst[word_idx] = current_word
    
    return " ".join(word_lst)

    


original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)


"""
Problem:  2nd attempt
    - Convert every other letter in every 3rd word to uppercase
    Input:
        - String
    Output:
        - String w letters converted
    Rules:
        - Dont change other characters
Data:
    - List to store words

Algo:
    - Split sentence into words
    - Iterate through words
        - On 3rd word, Iterate through each character
            - transfer character to result string (word) unless 2nd char and alphabet
        - add word to result list
    - join words
"""


# def to_weird_case(string):
#     words = string.split()
#     for idx, word in enumerate(words):
#         if (idx + 1) % 3 == 0:
#             words[idx] = edit_word(word)

#     return " ".join(words)

# def edit_word(word):
#     result = ""
#     for idx, char in enumerate(word):
#         if char.isalpha() and (idx + 1) % 2 == 0:
#             result += char.upper()
#         else:
#             result += char
#     return result