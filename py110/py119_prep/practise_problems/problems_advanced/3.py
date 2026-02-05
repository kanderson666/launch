"""
Rotating Matrices
As we saw in the previous exercises, a matrix can be represented by a list of lists. 
For example, the 3x3 matrix shown below:

1  5  8
4  7  2
3  9  6

is represented by the following list of list:

matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

A 90-degree rotation of a matrix produces a new matrix in which each side of the matrix is 
rotated clockwise by 90 degrees. 
For example, the 90-degree rotation of the matrix shown above is:

3  4  1
9  7  5
6  2  8

A 90-degree rotation of a non-square matrix is similar. 
For example, given the following matrix:

3  4  1
9  7  5

its 90-degree rotation is:

9  3
7  4
5  1


1 2 3 4
5 6 7 8
9 a b c
d e f g

d 9 5 1
e a 6 2
f b 7 3
g c 8 4

Write a function that takes an arbitrary MxN matrix, rotates it clockwise by 90-degrees 
as described above, and returns the result as a new matrix. 
The function should not mutate the original matrix.

Problem:
    - Rotate matrix 90 degrees
Algo:
    - Last row become first column
    - 2nd last row become 2nd column
    - 3rd last row become 3rd column
    - etc
    - Length of row becomes num of nested lists

    # - Find num_rows of new matrix by length of matrix
    # - Find num_columns of new matric by length of 1st row of matrix
    - Iterate through rows of matrix, starting from last row
        - Iterate through each member of row, starting from 1st member, tracking idx of that member
            - Use that idx to pick the row of new_matrix to append that member to
"""
FIRST_ROW = 0
def rotate90(matrix):
    new_matrix = [[] for _ in range(len(matrix[FIRST_ROW]))]
    
    for row_idx in range(len(matrix) - 1, -1, -1):
        for new_row_idx, member in enumerate(matrix[row_idx]):
            new_matrix[new_row_idx].append(member)
            
    return new_matrix


matrix1 = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

matrix2 = [
    [3, 7, 4, 2],
    [5, 1, 0, 8],
]

new_matrix1 = rotate90(matrix1)
new_matrix2 = rotate90(matrix2)
new_matrix3 = rotate90(rotate90(rotate90(rotate90(matrix2))))

# These examples should all print True
print(new_matrix1 == [[3, 4, 1], [9, 7, 5], [6, 2, 8]])
print(new_matrix2 == [[5, 3], [1, 7], [0, 4], [8, 2]])
print(new_matrix3 == matrix2)
