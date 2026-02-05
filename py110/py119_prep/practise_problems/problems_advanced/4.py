"""
Merge Sorted Lists
Write a function that takes two sorted lists as arguments and returns a new list that 
contains all the elements from both input lists in ascending sorted order. 
You may assume that the lists contain either all integer values or all string values.

You may not provide any solution that requires you to sort the result list. 
You must build the result list one element at a time in the proper order.

Your solution should not mutate the input lists.

Algo:
    - Get length of both lists
    - Start idx counter for both lists
    - put 1st value of 1st list in result list
    - loop while len result < len of both lists
        - While list2[idx2] < result[-1] and idx2 < len(list2)
            - put in 2nd last spot of result
            - increase idx2 by 1
        - While list1[idx1] < result[-1] and idx1 < len(list1)
    - return result

"""
# Option 1, following Algo
# def merge(list1, list2):
#     if not list1:
#         return list2 if list2 else []
#     if not list2:
#         return list1 if list1 else []

#     idx1, idx2 = 0, 0
#     result = [list1[idx1]]
#     idx1 += 1

#     while len(result) < (len(list1) + len(list2)):
#         while idx2 < len(list2) and list2[idx2] < result[-1]:
#             result.insert(-1, list2[idx2])
#             idx2 += 1

#         if idx1 < len(list1):
#             result.append(list1[idx1])
#             idx1 += 1
#         elif idx2 < len(list2):
#             result.append(list2[idx2])
#             idx2 += 1

#     return result

# Option 2, simplified after finished Option 1
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


# All of these examples should print True
print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
print(merge([], [1, 4, 5]) == [1, 4, 5])
print(merge([1, 4, 5], []) == [1, 4, 5])

names1 = ['Alice', 'Kim', 'Pete', 'Sue']
names2 = ['Bonnie', 'Rachel', 'Tyler']
names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
                  'Rachel', 'Sue', 'Tyler']
print(merge(names1, names2) == names_expected)