# Your code goes here
"""
Problem:
    - Find how many Friday 13ths in a specified year
    Input:
        - int (year)
    Output:
        - int (# Friday 13ths in that year)
Algo:
    - 
"""
import datetime

def friday_the_13ths(year):
    # create list of dates of each 13th of each month
    dates = [datetime.date(year, month, 13) for month in range(1, 13)]
    
    # count days of those dates where the 13th is on Friday
    count = 0
    for day in dates:
        if day.isoweekday() == 5:
            count += 1
    return count


print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True
