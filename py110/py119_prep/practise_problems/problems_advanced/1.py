# https://launchschool.com/exercises/8a772030?track=python
# turn all columns into rows, and rows into columns

# Your code goes here

def transpose(lst):
    new_lst = []
    for column in range(len(lst[0])):
        new_lst.append([])
        for row in lst:
            new_lst[column].append(row[column])
    return new_lst
    
matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

new_matrix = transpose(matrix)

print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True
