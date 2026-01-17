# 3. Set difference: missing elements
# You have a set of all expected attendees, and a set of actual attendees.
# Use a set operation to find who did NOT attend.

# Your code: missing = ...

# Test cases
expected = {'alice', 'bob', 'charlie', 'diana'}
actual = {'alice', 'charlie'}
missing = expected.difference(actual)
assert missing == {'bob', 'diana'}

expected = {'eve'}
actual = {'eve'}
missing = expected.difference(actual)
assert missing == set()

expected = set()
actual = {'someone'}
missing = expected.difference(actual)
assert missing == set()