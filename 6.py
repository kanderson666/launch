"""
Is It Prime?
A prime number is a positive number that is evenly divisible only by itself and 1. 
Thus, 23 is prime since its only divisors are 1 and 23. 
However, 24 is not prime since it has divisors of 1, 2, 3, 4, 6, 8, 12, and 24. Note that the number 1 is not prime.

Write a function that takes a positive integer as an argument and returns True if the number is prime, False if it is not prime.

You may not use any of Python's add-on packages to solve this problem. 
Your task is to programmatically determine whether a number is prime without relying on functions that already do that for you.

Problem:
    - Determine if number is a prime number
Input:
    - Integer
Output:
    - Boolean (True = Prime)

Data:
    - Integer input
    - Boolean output
    Intermediary:
        - ?

Algo:
    - If input is 2, is prime
    - If input is 1 or even, not prime
    - check if any numbers between 2 and half of number in question divide evenly into it
"""
def is_prime(num_check):
    if num_check == 2:
        return True
    if num_check == 1 or num_check % 2 == 0:
        return False

    for num in range(3, num_check // 2 + 1, 2):
        if num_check % num == 0:
            return False
    return True

print(is_prime(1) == False)              # True
print(is_prime(2) == True)               # True
print(is_prime(3) == True)               # True
print(is_prime(4) == False)              # True
print(is_prime(5) == True)               # True
print(is_prime(6) == False)              # True
print(is_prime(7) == True)               # True
print(is_prime(8) == False)              # True
print(is_prime(9) == False)              # True
print(is_prime(10) == False)             # True
print(is_prime(23) == True)              # True
print(is_prime(24) == False)             # True
print(is_prime(997) == True)             # True
print(is_prime(998) == False)            # True
print(is_prime(3_297_061) == True)       # True
print(is_prime(23_297_061) == False)     # True