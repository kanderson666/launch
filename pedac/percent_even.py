# /*
# PERCENTAGE OF EVENS (easy)
# Given a positive integer, return the percentage of even numbers between 1 and that integer, rounded to two decimal places.
"""
@@@ solve in 1-liner for extra challenge
PROBLEM:
    - Determine how many numbers between 1 and a number are even, expressed as % of total numbers
Input:
    - integer (upper limit)
Output: 
    - float (%- even numbers/total numbers)
Rules:
    - input is positive integer
    - round answer to 2 decimal places
    - return % of even numbers compared to total

Data:
    - integer (upper limit)
    - float (% result)
    Intermediary:
        - int count even #s
Algo:
    - use range between 1 and limit (input, inclusive)
        - check if num is even, add to int count
    - divide even count by total count (limit)

"""
def evenPercent(limit):
    # 1-liner:
    return f'{[ 0 for _ in range(1, limit, 2)].count(0) / limit if limit > 1 else "0":.2}'

    # Full write-out:
    # if limit < 2:
    #     return '0'
    #
    # num_evens = 0
    # for num in range(1, limit + 1):
    #     if num % 2 == 0:
    #         num_evens += 1
    # percent = num_evens / limit
    # # print(percent)
    # return f'{percent:.2}'

    # Full 1-liner equivalent:
    # return f'{[num % 2 for num in range(1, limit + 1) if num % 2 == 0].count(0)/limit if limit > 1 else "0":.2}'

# Python test cases:
print(evenPercent(1) == '0')
print(evenPercent(2) == '0.5')
print(evenPercent(3) == '0.33')
print(evenPercent(12) == '0.5')
print(evenPercent(13) == '0.46')