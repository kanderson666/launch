# https://launchschool.com/exercises/8a772030?track=python
# turn all columns into rows, and rows into columns
"""
Transpose 3x3 Matrix
A 3x3 matrix can be represented by a list of nested lists: an outer list that contains three sub-lists 
that each contain three elements. For example, the 3x3 matrix shown below:

1  5  8
4  7  2
3  9  6

is represented by the following list of lists:

matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

The transpose of a 3x3 matrix is the matrix that results from exchanging the rows and columns of the original matrix. 
For example, the transposition of the matrix shown above is:

1  4  3
5  7  9
8  2  6

Write a function that takes a list of lists that represents a 3x3 matrix and returns the transpose of the matrix. 
You should implement the function on your own, without using any external libraries.

Take care not to modify the original matrix -- your function must produce a new matrix and leave the input matrix list unchanged.

Problem:
    - Change the input matrix's columns into the rows
    Input:
        - List of lists of integers (3x3 matrix)
    Output:
        - New list of lists of integers (3x3 matrix)
    Rules:
        - Leave input matrix untouched
Algo:
    - Create new matrix (empty list)
    - Iterate through each index of columns (using range of length of 1st nested list)
        - Use helper to get column values (pass in matrix and idx)
            - Create empty column list
            - Iterate through each index of rows
                - Append the value at the column idx of that row to the column list
            - Return the column list
        - Append column list to new matrix list
    - Return new matrix

Data:
    - Matrix input (list of lists, 3x3)
    - integer for column idx (in for loop)
    - integer for row idx (in for loop)
    - List for column
    - Matrix output (list of lists, 3x3)
"""
FIRST_ROW = 0
def transpose(matrix):
    new_matrix = []
    for col_idx in range(len(matrix[FIRST_ROW])):
        new_matrix.append(get_column(matrix, col_idx))
    return new_matrix

def get_column(matrix, col_idx):
    column = []
    for row_idx in range(len(matrix)):
        column.append(matrix[row_idx][col_idx])
    return column

# def transpose(lst):
#     new_lst = []
#     for column in range(len(lst[0])):
#         new_lst.append([])
#         for row in lst:
#             new_lst[column].append(row[column])
#     return new_lst

matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

new_matrix = transpose(matrix)

print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True

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
