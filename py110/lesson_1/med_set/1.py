# 1. Unique words with a set
# Write code that, given a list of words (possibly with duplicates),
# produces a set of unique words that are at least 4 characters long.

# Your code: result = ...

# Test cases
words = ['tree', 'sun', 'tree', 'mountain', 'sun', 'cloud']
result = {word for word in words if len(word) >= 4}

assert result == {'tree', 'mountain', 'cloud'}

words = ['a', 'aa', 'aaa', 'aaaa', 'aaaa']
result = {word for word in words if len(word) >= 4}
assert result == {'aaaa'}

words = []
result = {word for word in words if len(word) >= 4}
assert result == set()