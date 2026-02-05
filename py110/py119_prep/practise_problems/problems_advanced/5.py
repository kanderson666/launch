"""
Merge Sort
A merge sort is a recursive sorting algorithm that works by breaking down a list's elements into nested sub-lists, 
then combining those nested sub-lists back together in sorted order. It is best explained with an example. 
Given the list [9, 5, 7, 1, 8, 2, 0, 6], let's walk through the process of sorting it with merge sort. 
We'll start off by breaking the list down into nested sub-lists:

[[[[9], [2]], [[7], [6]]], [[[8], [5]], [[0], [1]]]] -->
[[[2, 9], [6, 7]], [[5, 8], [0, 1]]] -->
[[2, 6, 7, 9], [0, 1, 5, 8]] -->
[0, 1, 2, 5, 6, 7, 8, 9]

For example, on the 2nd line, we merge [2, 9] with [6, 7], which becomes `[2, 6, 7, 9].

Write a function that takes a list argument and returns a new list that contains the values from the input list in sorted order. 
The function should sort the list using the merge sort algorithm as described above. 
You may assume that every element of the list will have the same data type: either all numbers or all strings.

Problem:
    - Take a list and sort it using merge sort
    - Turn elements into nested lists, merge lists together
    Input:
        - List
    Output:
        - List sorted
    Rules:
        - Input list be all same data type
Data:
    - List input/output
    Intermediary:
        - Nested lists to hold groups of members, until only 1 member in the list
        - Possibly integer to track size of list
Algo:
    - Nest lists (helper)
        - Split list into 2 equal lists (odd size give extra to right list)
        - Continue to divide lists until only 1 member remain in bottom list
    - Merge lists (helper)
        - Work from bottom of list (single member) and merge outward until all merged
    
Nest Lists PEDAC:
Problem:
    - Take a list and turn it into 2 lists, split in the middle
    Input:
        - List
    Output:
        - 2 lists nested in list
    Rules:
        - If input list has just 1 member, return list
Example:
    Single:
    - [1, 2, 3, 4] == [[1, 2], [3, 4]]
    - [1, 2, 3, 4, 5] == [[1, 2], [3, 4, 5]]
    Recursive:
    - [1, 2, 3, 4, 5, 6] == [[[1], [[2], [3]]], [[4], [[5], [6]]]]
    - [1, 2, 3, 4, 5, 6, 7] == [[[1], [[2], [3]]], [[[4], [5]], [[6], [7]]]
    - [1, 2, 3, 4, 5, 6, 7, 8] == [[[[1], [2]], [[3], [4]]], [[[5], [6]], [[7], [8]]]]
Data:
    - Lists
    - Integer to determine midpoint
Algo:
    - Find midpoint of list
    - Create list up to midpoint, separate list after midpoint
    - Return 2 lists nested together
"""
def merge_sort(lst):
    midpoint = len(lst) // 2
    lst1 = lst[:midpoint]
    lst2 = lst[midpoint:]

    if len(lst1) > 1:
        lst1 = merge_sort(lst1)
    if len(lst2) > 1:
        lst2 = merge_sort(lst2)
    
    combined = merge(lst1, lst2)

    return combined

def merge(list1, list2):
    if not list1:
        return list2 if list2 else []
    if not list2:
        return list1 if list1 else []

    idx2 = 0
    result = []

    for num in list1:
        result.append(num)

        while idx2 < len(list2) and list2[idx2] < result[-1]:
            result.insert(-1, list2[idx2])
            idx2 += 1

    if idx2 < len(list2):
        result.extend(list2[idx2:])

    return result


# def nest_lists(lst):
#     midpoint = len(lst) // 2
#     lst1 = lst[:midpoint]
#     lst2 = lst[midpoint:]

#     if len(lst1) > 1:
#         lst1 = nest_lists(lst1)
#     if len(lst2) > 1:
#         lst2 = nest_lists(lst2)
    
#     combined = [lst1] + [lst2]
#     return combined

# print(nest_lists([1, 2, 3, 4, 5, 6]) == [[[1], [[2], [3]]], [[4], [[5], [6]]]])
# print(nest_lists([1, 2, 3, 4, 5, 6, 7]) == [[[1], [[2], [3]]], [[[4], [5]], [[6], [7]]]])
# print(nest_lists([1, 2, 3, 4, 5, 6, 7, 8]) == [[[[1], [2]], [[3], [4]]], [[[5], [6]], [[7], [8]]]])



# All of these examples should print True
print(merge_sort([9, 5, 7, 1]) == [1, 5, 7, 9])
print(merge_sort([5, 3]) == [3, 5])
print(merge_sort([6, 2, 7, 1, 4]) == [1, 2, 4, 6, 7])
print(merge_sort([9, 2, 7, 6, 8, 5, 0, 1]) == [0, 1, 2, 5, 6, 7, 8, 9])

original = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
            'Kim', 'Bonnie']
expected = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel',
            'Sue', 'Tyler']
print(merge_sort(original) == expected)

original = [7, 3, 9, 15, 23, 1, 6, 51, 22, 37, 54,
            43, 5, 25, 35, 18, 46]
expected = [1, 3, 5, 6, 7, 9, 15, 18, 22, 23, 25,
            35, 37, 43, 46, 51, 54]
print(merge_sort(original) == expected)
