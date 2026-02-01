EVEN = 0
ODD = 1

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

for idx in range(len(lst) - 2, -1, -2):
    lst.pop(idx)
print(lst)