"""
P:
    -Find (s) number of numerical palindromes starting from number (num)
E:
    - if s 0, return empty list
    - Num is at least 2 digits
    - Num reads same forwards and backwards

D:
    - Inputs
        - Integer, integer (number_start, number_of_palindromes)
    - Outputs
        - List of integers (list of palindromes)
A:
    - If s is less than 1, return empty list
    - If num is less than 11, number_start is 11
    - Increment number_start by 1 each loop
        - Check if number_start is palindrome, add to result list
        - Repeat until result list is desired size (s)

"""
def palindrome(num, s):
    result = []
    if num < 11:
        num = 11
        
    while len(result) < s:
        if is_palindrome(num):
            result.append(num)
        num += 1
    return result

def is_palindrome(num):
    num = str(num)
    return num[::-1] == num

print(palindrome(6, 4))
print(palindrome(75, 1))
print(palindrome(101, 2))
print(palindrome(20, 0))
print(palindrome(0, 4))
