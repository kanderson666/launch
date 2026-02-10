"""
Problem 1: Sort by String Length  2min 30sec (test cases were incorrectly provided. This time is with solution and debugging test cases)
Difficulty: Basic

Create a function that takes a list of strings and returns a new list with 
the strings sorted by length, from shortest to longest.


"""

def sort_by_length(str_list):
    
    str_list.sort(key=len)
    return str_list
    # return sorted(str_list, key=len)

# Test Cases
print(sort_by_length(['python', 'is', 'a', 'powerful', 'language']) == ['a', 'is', 'python', 'powerful', 'language'])
print(sort_by_length(['go', 'java', 'c++', 'rust']) == ['go', 'c++', 'java', 'rust'])
print(sort_by_length(['a', 'b', 'c']) == ['a', 'b', 'c'])
print(sort_by_length([]) == [])