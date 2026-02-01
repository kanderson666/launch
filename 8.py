"""
Fibonacci Numbers (Recursion)
In the previous exercise, we developed a procedural solution for computing the nth Fibonacci number.

This sequence can also be computed using a recursive function. A recursive function is one in which the function calls itself. 
For example, the following function is a recursive function that computes the sum of all integers between 1 and n:
def sum_recursive(n):
    if n == 1:
        return 1

    return n + sum_recursive(n - 1)
"""
def fibonacci(nth):
    if nth == 1 or nth == 2:
        return 1
    return fibonacci(nth - 1) + fibonacci(nth - 2)


print(fibonacci(1) == 1)         # True
print(fibonacci(2) == 1)         # True
print(fibonacci(3) == 2)         # True
print(fibonacci(4) == 3)         # True
print(fibonacci(5) == 5)         # True
print(fibonacci(6) == 8)         # True
print(fibonacci(12) == 144)      # True
print(fibonacci(75) == 6765)     # True
