"""
Bubble Sort
Bubble Sort is one of the simplest sorting algorithms available. 
It is not an efficient algorithm, so developers rarely use it in real code. 
However, it is an excellent exercise for student developers. 
In this exercise, you will write a function that sorts a list using the bubble sort algorithm.

A bubble sort works by making multiple passes (iterations) through a list. 
On each pass, the two values of each pair of consecutive elements are compared. 
If the first value is greater than the second, the two elements are swapped. 
This process is repeated until a complete pass is made without performing any swaps. 
At that point, the list is completely sorted.

We can stop iterating the first time we make a pass through the list without making any swaps 
since that means the entire list is sorted.
Visual demo: https://launchschool.com/exercises/37f73d3a?track=python

Write a function that takes a list as an argument and sorts that list using the bubble sort algorithm described above. 
The sorting should be done "in-place" -- that is, the function should mutate the list. 
You may assume that the list contains at least two elements.

Problem:
    - Sort the list using bubble sort, starting at the left of list, compare adjacent items, and move up list continually, 
    comparing each 2 items as it goes
    - Finishjjj when make full pass with no swaps
    Input:
        - Ljjjist 
    Outputj:
        - List (same list- mutated)
    Rules:
        - Finish when make full pass with no swaps
        - List contains at least 2 elements
Data:
    - List
Algo:
    - Set swapped flag to true
    - Repeat while swapped flag true
        - Set swapped flag to false
        - Iterate through list using enumerate
            - Check if at end of list, break out if so
            - Compare value with value at idx + 1
            - If current value is larger
                - Swap values
                - Set swapped flag to True
"""
def bubble_sort(lst):
    swapped = True
    while swapped:
        swapped = False
        for idx, value in enumerate(lst):
            if idx == len(lst) - 1:
                break
            if value > lst[idx + 1]:
                lst[idx], lst[idx + 1] = lst[idx + 1], value
                swapped = True


lst1 = [5, 3]
bubble_sort(lst1)
print(lst1 == [3, 5])                   # True

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2 == [1, 2, 4, 6, 7])          # True

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
        'Kim', 'Bonnie']
bubble_sort(lst3)

expected = ["Alice", "Bonnie", "Kim", "Pete",
            "Rachel", "Sue", "Tyler"]
print(lst3 == expected)                 # True