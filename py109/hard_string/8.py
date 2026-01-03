# 3. Find the most frequent word (with normalization)

"""
Write a function `most_frequent_word(text)` that:

- Treats uppercase and lowercase letters as the same (case-insensitive).
- Considers words as sequences of letters and digits only.
- Ignores all other characters (punctuation, etc.).
- Returns the most frequent word in lowercase.
- If there is a tie, return the word that appears first in the original text
  (based on first occurrence, not alphabetical order).

Examples:
most_frequent_word("Apple banana apple.")        -> "apple"
most_frequent_word("One, two; two: THREE three") -> "two"
most_frequent_word("A a a B b b c")              -> "a"
"""
def word_count(text1):
    result = {}
    for word in text1:
        if word in result:
            result[word] += 1
            continue
        fixed_word = ""
        for char in word:
            if char.isalnum():
                fixed_word += char
            else:
                fixed_word += " "
        if fixed_word in result:
            result[fixed_word] += 1
        else:
            result[fixed_word] = 1
    return result

def most_frequent_word(text):
    if not text:
        return ""
    
    word_dict = word_count(text.casefold().split())

    highest_count = 0
    highest_word = ""
    for word in word_dict:
        if word_dict[word] > highest_count:
            highest_word = word
            highest_count = word_dict[word]
    return highest_word

print(most_frequent_word("Apple banana apple."))#        -> "apple"
print(most_frequent_word("One, two; two: THREE three"))# -> "two"
print(most_frequent_word("A a a B b b c"))#              -> "a"
