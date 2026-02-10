"""
Problem 3: Sort Tuples by Second Element     unfinished- had to learn how to sort by 2 elements
Difficulty: Intermediate

Create a function that takes a list of tuples, where each tuple contains two elements. 
The function should return a new list of tuples sorted primarily by the second element in ascending order. 
If the second elements are the same, it should then sort by the first element in ascending order.

"""
def sort_by_second_element(tuple_list):
    tuple_list.sort(key=lambda tup: (tup[1], tup[0]))
    # tuple_list.sort(key=second_element)
    return tuple_list

def second_element(tup):
    first, second = tup
    return second, first



# Test Cases
print(sort_by_second_element([(3, 4), (1, 2), (5, 2), (1, 5)]) == [(1, 2), (5, 2), (3, 4), (1, 5)])
print(sort_by_second_element([('c', 2), ('a', 1), ('b', 2)]) == [('a', 1), ('b', 2), ('c', 2)])
print(sort_by_second_element([(9, 9), (8, 8), (7, 7)]) == [(7, 7), (8, 8), (9, 9)])