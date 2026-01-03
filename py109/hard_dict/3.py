# Problem 3: Find the most common substrings of length k
# ------------------------------------------------------
# Write a function most_common_substrings(s, k) that:
# - Takes a string s and an integer k.
# - Considers all substrings of length k in s (overlapping allowed).
# - Counts how many times each substring appears.
# - Returns a dictionary:
#   - Keys: substrings of length k.
#   - Values: counts of how many times each substring appears.
# Additionally:
# - After building the dictionary, determine which substring(s) appear the
#   most times and what that maximum count is.
# - You can print the most common substring(s) and their count from inside
#   the function (or outside, after receiving the dict).

def most_common_substrings(s, k):
    # your code here
    pass


# Test cases
s1 = "ababa"
k1 = 2
print(most_common_substrings(s1, k1))
# All substrings of length 2: "ab", "ba", "ab", "ba"
# Expected dict: {"ab": 2, "ba": 2}
# Most common substrings: "ab" and "ba" with count 2

s2 = "aaaaa"
k2 = 2
print(most_common_substrings(s2, k2))
# Substrings: "aa", "aa", "aa", "aa"
# Expected dict: {"aa": 4}
# Most common substring: "aa" with count 4
