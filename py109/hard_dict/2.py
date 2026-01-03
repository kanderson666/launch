# Problem 2: Group words by sorted letters (anagrams)
# ---------------------------------------------------
# Write a function group_anagrams(words) that:
# - Takes a list of strings `words`.
# - Returns a dictionary where:
#   - Keys are the sorted letters of a word (e.g. "aet" for "eat"/"tea"/"ate").
#   - Values are lists of all words from the input that correspond to that key.
# Requirements:
# - The lists of words should preserve the original order they appeared in
#   the input list.
# - The order of keys in the returned dictionary does not matter.

def group_anagrams(words):
    # your code here
    pass


# Test cases
words1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words1))
# Example expected (order of keys may differ, but lists preserve word order):
# {
#   "aet": ["eat", "tea", "ate"],
#   "ant": ["tan", "nat"],
#   "abt": ["bat"]
# }

words2 = ["listen", "silent", "enlist", "google", "gooegl", "abc"]
print(group_anagrams(words2))
# Expected keys (order may differ):
# "eilnst": ["listen", "silent", "enlist"]
# "eggloo": ["google", "gooegl"]
# "abc": ["abc"]
