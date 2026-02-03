"""
Fibonacci Number Location By Length
As we've seen in the last few exercises, the Fibonacci series is a computationally simple series. 
However, the results grow at an incredibly rapid rate. 
For example, the 100th Fibonacci number is 354,224,848,179,261,915,075 -- that's enormous, 
especially considering that it takes six iterations just to find the first 2-digit Fibonacci number.

Write a function that calculates and returns the index of the first Fibonacci number that has the number 
of digits specified by the argument. The first Fibonacci number has an index of 1. 
You may assume that the argument is always an integer greater than or equal to 2.

Problem:
    - Determine how far into fibonacci series before result is n digits long
Input:
    - Integer (how many digits we want the sum to be)
Output:
    - Integer (what nth number to create sum of (input) length digits)
Rules:
    - Length always >= 2

Data:
    - Integer (input/output)

Algo:
    - Iterate through all nums between 2 and infinity
        - Check if lenth of return value of fibonacci at that num == length desired
            - If no, continue
            - If yes, return that num
"""
import sys

sys.set_int_max_str_digits(50_000)
computed = {}

def find_fibonacci_index_by_length(length):
    num = 2
    while len(str(fibonacci(num))) < length:
        num += 1
    return num

def fibonacci(nth):
    if nth == 1 or nth == 2:
        return 1
    if nth not in computed:
        computed[nth] = fibonacci(nth - 1) + fibonacci(nth - 2)
    return computed[nth]


# All of these examples should print True
# The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
print(find_fibonacci_index_by_length(1000) == 4782)

# Next example might take a little while on older systems
print("Long")
print(find_fibonacci_index_by_length(10000) == 47847)
