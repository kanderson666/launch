"""
Given a list of strings, sort the list based on the highest number of adjacent consonants 
a string contains and return the sorted list. If two strings contain the same highest number 
of adjacent consonants, they should retain their original order in relation to each other. 
Consonants are considered adjacent if they are next to each other in the same word or if 
there is a space between two consonants in adjacent words.

1. Problem:
Input:
    - List of strings
Output:
    - List of strings (sorted)
Rules:
    Explicit:
        - Sort list based on strings with highest number adjacent consonants
        - If 2 equal, keep order provided
        - Space not affect adjacency
    Implicit:
        - Single consonant not affect order
        - Return new list
        - Only lowercase provided
        - Will not contain punctuation
        - Will always have multiple elements in input
Questions:
    - Mutate the original list, or return new list? [Unknown- assuming new list]
    - Case insensitive? [Assuming lowercase only]
    - Punctuation affect adjacency? [Unknown- assuming no punctuation]
    - How handle empty or single element list? [Unknown- assume multiple elements]

2. Examples:
my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']

3. Data
Type: List of strings

4. Algorithm:
    - Store all consonants in list
    - Iterate through each string
        - Start current and highest consonant counts at 0, last letter consonant boolean to False
        - If letter is space, go to next
        - Check if current letter is consonant
            - Check if last letter was consonant
                - Increase current count by 1
            - Set last letter consonant to True
        - If no
            - Check if current count > highest count
                - If yes, update highest count
            - Set last letter consonant boolean to False
            - Set current count 0
        - At end of string, put count and string in list of tuples
    - Sort matches
        - See other PEDAC
    - Return list
"""
"""
    1. Problem
    Input:
    - List of tuples (count, string)
    Output:
    - List of strings (in order of count)
    Rules:
        Explicit:
            - Highest count first
            - Tied counts same order as received
        Implicit:
            - More than 1 member provided
    3. Data
    - list of tuples as input
    - list to store sorted strings
    - int to track highest scores

    4. Algorithm
    - Loop through first member of tuples to find highest score
    - Once found, add strings with highest score, in order to list
    - Repeat loop, looking for highest score thats below previous highest until all members in both lists
"""
    
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

def count_consonants(string_lst):
    results_lst = []
    for string in string_lst:
        current_count = 0
        highest_count = 0
        last_consonant = False
        for char in string:
            if char.isspace():
                continue
            if char in CONSONANTS: 
                if last_consonant:
                    current_count += 1
                last_consonant = True
            else:
                highest_count = current_count if current_count > highest_count else highest_count
                last_consonant = False
                current_count = 0
        highest_count = current_count if current_count > highest_count else highest_count
        results_lst.append((highest_count, string))
    return results_lst

def sort_strings(tple_lst):
    sorted_lst = []
    last_count = float('inf')
    while len(sorted_lst) < len(tple_lst):
        highest_count = -1
        for tple in tple_lst:
            if tple[0] > highest_count and tple[0] < last_count:
                highest_count = tple[0]
        for tple in tple_lst:
            if tple[0] == highest_count:
                sorted_lst.append(tple[1])
        last_count = highest_count
    return sorted_lst

def sort_by_consonant_count(string_lst):
    counted_lst = count_consonants(string_lst)
    result_lst = sort_strings(counted_lst)
    return result_lst


my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list)== ['dddaa', 'ccaa', 'aa', 'baa'])

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list) == ['salt pan', 'can can', 'batman', 'toucan'])

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list) == ['bar', 'car', 'far', 'jar'])

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list) == ['month', 'day', 'week', 'year'])

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list) == ['xxxx', 'xxxb', 'xxxa'])