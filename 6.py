"""
Write function to remove every other item from list

"""
DELETE_EVEN_IDXs = 1
DELETE_ODD_IDXs = 0
lst = [1, 2, 3, 4, 5, 6, 7]

delete_idx = len(lst) - 1

if delete_idx % 2 == DELETE_ODD_IDXs:
    delete_idx -= 1

while delete_idx >= 0:
    lst.pop(delete_idx)
    delete_idx -= 2
print(lst)
