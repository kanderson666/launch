"""
Problem 17  # forgot to time. ~15mins?
Create a function that takes a list of integers as an argument. 
The function should determine the minimum integer value that can be appended to the list 
so the sum of all the elements equals the closest prime number that is greater than the current sum of the numbers. 

For example, the numbers in [1, 2, 3] sum to 6. The nearest prime number greater than 6 is 7. 
Thus, we can add 1 to the list to sum to 7.

Notes:

The list will always contain at least 2 integers.
All values in the list must be positive (> 0).
There may be multiple occurrences of the various numbers in the list.

Problem:
    - Sum list of int
    - Find first prime number greater than the sum
    - Find difference between sum of list and prime number
    
Problem:
    - Find closest prime number higher than provided num
    Input:
        - Int (min)
    Output:
        - Int prime number
Data:
    - Ints
Algo:
    - While true
        - Iterate through nums from 2 to num, to see if is prime
            - If not prime, increase num by 1
            - If prime, return num
"""
def nearest_prime_sum(lst):
    lst_sum = sum(lst)
    prime = find_next_prime(lst_sum + 1)
    return prime - lst_sum

def find_next_prime(check):
    while True:
        for num in range(2, check):
            if check % num == 0:
                break
            if num == check - 1:
                return check
        check += 1


print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

# Nearest prime to 163 is 167
print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)
