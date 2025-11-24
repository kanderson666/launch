numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]

print(numbers[len(numbers) - 1 :  : -1])    #len(numbers)-1 not needed

print(list(reversed(numbers)))
print(numbers)