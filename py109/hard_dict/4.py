# Problem 4: Invert a dictionary with non-unique values
# -----------------------------------------------------
# You are given a dictionary where:
# - Keys are student names (strings).
# - Values are grades (integers).
# Write a function invert_grades(grades) that:
# - Returns a NEW dictionary where:
#   - Keys are grades.
#   - Values are lists of student names who have that grade.
# Requirements:
# - The list of students for each grade should be sorted alphabetically.
# - If the input is empty, return an empty dictionary.

def invert_grades(grades):
    # your code here
    pass


# Test cases
grades1 = {
    "Alice": 90,
    "Bob": 85,
    "Charlie": 90,
    "Diana": 70,
    "Eve": 85,
}

print(invert_grades(grades1))
# Expected (order of keys may differ):
# {
#   90: ["Alice", "Charlie"],
#   85: ["Bob", "Eve"],
#   70: ["Diana"]
# }

grades2 = {}
print(invert_grades(grades2))
# Expected: {}
