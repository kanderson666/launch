# Your code goes here
"""
Problem:
    - Find next featured number after supplied number
    Input:
        - Int
    Output:
        - Int
    Rules:
        - Must be multiple of 7, but not of 2
        - Each digit of number must only appear once
        - Error if theres no higher feature number
Data:
    - ints
    - String to test each digit
Algo:
    - Find num to start range at (helper)
        - int divide # supplied by 7, and add 1
        - If that num even, add 1
        - Multiply that num by 7, that is our start
    - Iterate through nums, starting at start num, ending at largest possible feature (9876543201) + 1, stepping by 14 (to skip the even nums)
        - Convert num to string, also to set
        - Check if string and set lengths are equal
            - If yes, is feature, return
            - If no, continue
    - If not find before finish iterating, return Error
"""
LARGEST = 9876543201 + 1
error = ("There is no possible number that "
         "fulfills those requirements.")

def next_featured(start):
    start = range_start(start)
    for num in range(start, LARGEST, 14):
        str_num = str(num)
        set_num = set(str_num)
        if len(str_num) == len(set_num):
            return num
    return error

def range_start(num):
    multiplier = num // 7 + 1
    if multiplier % 2 == 0:
        multiplier += 1
    return multiplier * 7
    


print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

print(next_featured(9876543201) == error)       # True
