# /*
# Given two words, how many letters do you have to remove from them to make them anagrams?

# Problem
# Given two strings, return the number of characters that need to be removed from both to make them anagrams.

# Rules/Requirements
# - only lowercase alphabetic characters
# - anagram is same letters with same frequencies, order doesn't matter
# - one empty string => length of the other string
# - if there are no common characters between two strings, return sum of length of both

# Data Structures
# Input: two strings
# Output: Number (count of letters to be removed)
# Intermediate:
#   Boolean: testing length of strings for being empty
#   Number: compare frequencies of letters
#   String: create sorted string (anagrams will match exactly)
#   Array: convert strings to arrays - create a set, iterate over a string
#   Dictionary: tally of frequencies of letters {'a': 1, 'b': 2, ...}
#   Set: unique set of characters that are in both strings

# High-level strategies
# Kurtis: Create a set of unique characters from both strings. Iterate through the set, count how many chars in each string, keep count of differences.

#   ('codewars', 'hackerrank') == 10
#   {a, c, d, e, h, k, n, o r, s, w}
#   a = 1a - 2a = 1
#   c = 1c - 1c = 0
#   d = 1d - 0d = 1
#   e = 1e - 1e = 0
#   h = 0h - 1h = 1
#   k = 0k - 2k = 1

#   Jacob: Create an array of characters from each string X

#   Jacob: Create a dictionary to tally letters for each word. Compare values for each key and add up the differences. Make sure I don't miss any keys, and don't double count any either.

# High-level strategies
# Kurtis: Create a set of unique characters from both strings. Iterate through the set, count how many chars in each string, keep count of differences.

def anagram_difference(string1, string2):
    # unique_set = set()
    # for char in (string1 + string2):
    #     unique_set.add(char)
    # for char in string2:
    #     unique_set.add(char)
    my_set = set(string1 + string2)
    total = 0
    for char in my_set:
        count1 = string1.count(char)
        count2 = string2.count(char)
        total += abs(count1-count2)
    return total
        

print(anagram_difference('', '') == 0)
print(anagram_difference('a', '') == 1)
print(anagram_difference('', 'a') == 1)
print(anagram_difference('ab', 'a') == 1)
print(anagram_difference('ab', 'ba') == 0 )
print(anagram_difference('ab', 'cd') == 4)
print(anagram_difference('aab', 'a') == 2 )
print(anagram_difference('a', 'aab') == 2 )
print(anagram_difference('codewars', 'hackerrank') == 10 )
print(anagram_difference("oudvfdjvpnzuoratzfawyjvgtuymwzccpppeluaekdlvfkhclwau", "trvhyfkdbdqbxmwpbvffiodwkhwjdjlynauunhxxafscwttqkkqw") == 42)
print(anagram_difference("fcvgqognzlzxhmtjoahpajlplfqtatuhckxpskhxiruzjirvpimrrqluhhfkkjnjeuvxzmxo", "qcfhjjhkghnmanwcthnhqsuigwzashweevbegwsbetjuyfoarckmofrfcepkcafznykmrynt") == 50)
