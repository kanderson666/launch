"""
Rotation (Part 1)
Write a function that rotates a list by moving the first element to the end of the list. 
Do not modify the original list; return a new list instead.

If the input is an empty list, return an empty list.
If the input is not a list, return None.
Review the test cases below, then implement the solution accordingly.

Problem:
    - Move first element of list to end, and move all other elements forward 1
Input:
    - List
Output:
    - New list with moved members
Rules:
    - Return new list
    - If input is empty list, return empty list
    - If input not a list, return None

Data:
    - List (input and output)

Algo:
    - Check if list, return None if not
    - Check if list not empty, return empty list if not
    - Return concatenated list of 1st index to end, plus 0th index

"""

def rotate_list(lst):
    if not isinstance(lst, list):
        return None
    if not lst:
        return lst
    return lst[1:] + lst[:1]


# All of these examples should print True

print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
print(rotate_list(['a']) == ['a'])
print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
print(rotate_list([]) == [])

# return `None` if the argument is not a list
print(rotate_list(None) == None)
print(rotate_list(1) == None)

# the input list is not mutated
lst = [1, 2, 3, 4]
print(rotate_list(lst) == [2, 3, 4, 1])
print(lst == [1, 2, 3, 4])