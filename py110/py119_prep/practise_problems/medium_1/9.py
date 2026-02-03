"""
Fibonacci Numbers (Memoization)
Our recursive fibonacci function from the previous exercise isn't very efficient. 
It starts slowing down with an nth argument value somewhere around 35-60, depending on your system. 
One way to improve the performance of our recursive fibonacci function (and other recursive functions) is to use memoization.

Memoization is an approach that involves saving a computed answer for future reuse, 
instead of computing it from scratch every time it is needed. 
In the case of our recursive fibonacci function, using memoization saves calls to fibonacci(nth - 2) 
because the necessary values have already been computed by the recursive calls to fibonacci(nth - 1).

For this exercise, your objective is to refactor the recursive fibonacci function to use memoization.

An image representing the computation of the 7th Fibonacci number is shown below. 
It is the same image that was shown in the previous exercise, except this one highlights the values that have previously been computed.
https://launchschool.com/exercises/030ec9a5?track=python

Problem:
    - Write recursive fibonacci function that checks if value has been previously calculated, before doing the recursive call
Input:
    - Integer (nth fibonacci)
Output:
    - Integer (sum of fibonaccis)
Rules:
    - 
Data:
    - Integer (input/output)
    - Dictionary (store nth : sum)
Algo:
    - create global dict for computed values (nth : sum)
    - check if nth == 1 or 2
        - return 1
    - check if func(nth) in dict
        - If yes, return sum value
        - If no, call func
            - store nth and return value in dict
            - return return value
"""

computed = {}

def fibonacci(nth):
    if nth == 1 or nth == 2:
        return 1
    if nth not in computed:
        computed[nth] = fibonacci(nth - 1) + fibonacci(nth - 2)
    return computed[nth]


print(fibonacci(1) == 1)         # True
print(fibonacci(2) == 1)         # True
print(fibonacci(3) == 2)         # True
print(fibonacci(4) == 3)         # True
print(fibonacci(5) == 5)         # True
print(fibonacci(6) == 8)         # True
print(fibonacci(12) == 144)      # True
print(fibonacci(20) == 6765)     # True
