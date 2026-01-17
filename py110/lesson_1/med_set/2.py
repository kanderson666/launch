# 2. Set operations: intersection
# You are given two sets of student IDs: those who submitted homework,
# and those who took the quiz. Use a set operation to find the IDs
# of students who did BOTH.

# Your code: both = ...


# Test cases
homework = {1, 2, 3, 4}
quiz = {3, 4, 5}
both = homework.intersection(quiz)
assert both == {3, 4}

homework = {10, 20, 30}
quiz = {40, 50}
both = homework.intersection(quiz)
assert both == set()

homework = set()
quiz = {1, 2, 3}
both = homework.intersection(quiz)
assert both == set()