"""
Problem 14   5min 15sec
Create a function that takes a single integer argument and returns the sum of all the multiples 
of 7 or 11 that are less than the argument. If a number is a multiple of both 7 and 11, count it just once.

For example, the multiples of 7 and 11 that are below 25 are 7, 11, 14, 21, and 22. The sum of these multiples is 75.

If the argument is negative, return 0.

Problem:
    - Calc sum of all multiples of 7 and 11 that are less than a num
    Input:
        - Int (max num)
    Output:
        - Int (sum of all multiples)
    Rules:
        - -'ve num, return 0
Data:
    - Set: track multiples used. Can sum set at the end
Algo:
    - If num less than 7, return 0
    - Iterate through all multiples of 7 from 7 to max below num provided
        - add all multiples to the set
    - Iterate through multiples of 11
        - add all to set
    - Sum set, return
"""

def seven_eleven(num):
    result = set()
    for seven in range(7, num, 7):
        result.add(seven)
    for eleven in range(11, num, 11):
        result.add(eleven)
    return sum(result)


print(seven_eleven(10) == 7)
print(seven_eleven(11) == 7)
print(seven_eleven(12) == 18)
print(seven_eleven(25) == 75)
print(seven_eleven(100) == 1153)
print(seven_eleven(0) == 0)
print(seven_eleven(-100) == 0)
