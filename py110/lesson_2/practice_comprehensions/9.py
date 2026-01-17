"""
This problem may prove challenging. Try it, but don't stress about it. 
If you don't solve it in 20 minutes, you can look at the answer.

Given the following data structure, write some code to return a list 
that contains only the dictionaries where all the numbers are even.

"""
lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]
def check_even(dictt):
    for lsts in dictt.values():
        if any([num % 2 for num in lsts]):
            return False
        # for num in lsts:
        #     if num % 2 == 1:
        #         return False
    return True
result = [dictt for dictt in lst if check_even(dictt)]
print(result)

# Expected:
# [{'e': [8], 'f': [6, 10]}]
