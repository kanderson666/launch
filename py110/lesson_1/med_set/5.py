# 5. Set comprehension with a condition
# Given a string, build a set (using a set comprehension) that contains
# all lowercase vowels that appear in the string at least once.

# Your code: vowels_in_string = ...
VOWELS = 'aeiou'
# Test cases
text = 'Launch School'
vowels_in_string = {char for char in text if char.islower() and char in VOWELS}
# 'Launch School' contains: a, u, o
assert vowels_in_string == {'a', 'u', 'o'}

text = 'PYTHON'
vowels_in_string = {char for char in text if char.islower() and char in VOWELS}
assert vowels_in_string == set()

text = 'beautiful'
vowels_in_string = {char for char in text if char.islower() and char in VOWELS}
# contains: a, e, i, u
assert vowels_in_string == {'a', 'e', 'i', 'u'}