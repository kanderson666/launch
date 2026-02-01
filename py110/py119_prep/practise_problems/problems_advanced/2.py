# https://launchschool.com/exercises/b2831239?track=python
# same as 1.py, but accept non-square matrix
# solution also the same- code already worked with any size

# Your code goes here
def transpose(lst):
    new_lst = []
    for column in range(len(lst[0])):
        new_lst.append([])
        for row in lst:
            new_lst[column].append(row[column])
    return new_lst

# All of these examples should print True
print(transpose([[1, 2, 3, 4]]) == [[1], [2], [3], [4]])
print(transpose([[1], [2], [3], [4]]) == [[1, 2, 3, 4]])
print(transpose([[1]]) == [[1]])

matrix_3_by_5 = [
    [1, 2, 3, 4, 5],
    [4, 3, 2, 1, 0],
    [3, 7, 8, 6, 2],
]
expected_result = [
    [1, 4, 3],
    [2, 3, 7],
    [3, 2, 8],
    [4, 1, 6],
    [5, 0, 2],
]

print(transpose(matrix_3_by_5) == expected_result)
