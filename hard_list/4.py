# Problem 4: Spiral traversal of a 2D matrix
# ------------------------------------------
# You are given a 2D list (matrix) of integers.
# Write a function spiral_order(matrix) that:
# - Returns a NEW list with the elements of the matrix in spiral order,
#   starting from the top-left corner, going right, then down, then left,
#   then up, and so on.
#
# Example:
# [
#   [1,  2,  3],
#   [4,  5,  6],
#   [7,  8,  9]
# ]
# -> [1, 2, 3, 6, 9, 8, 7, 4, 5]

def spiral_order(matrix):    
    def right(lst, matrix):
        for _ in range(len(matrix[0])):
            lst.append(matrix[0].pop(0))
        del matrix[0]

    def down(lst, matrix):
        for line in range(len(matrix)):
            lst.append(matrix[line].pop())

    def left(lst, matrix):
        for _ in range(len(matrix[-1])):
            lst.append(matrix[-1].pop(-1))
        del matrix[-1]

    def up(lst, matrix):
        for line in range(len(matrix)):
            lst.append(matrix[-line - 1].pop(0))

    if not matrix:
        return []
    work = [row[:] for row in matrix]
    
    result = []
    while work:
        right(result, work)
        if not work:
            break
        down(result, work)
        if not work:
            break
        left(result, work)
        if not work:
            break
        up(result, work)
    return result

# Test cases
matrix1 = [
    [1,  2,  3],
    [4,  5,  6],
    [7,  8,  9]
]
print(spiral_order(matrix1))
# Expected: [1, 2, 3, 6, 9, 8, 7, 4, 5]

matrix2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12]
]
print(spiral_order(matrix2))
# Expected: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

matrix3 = [[1]]
print(spiral_order(matrix3))
# Expected: [1]

matrix4 = []
print(spiral_order(matrix4))
# Expected: []
