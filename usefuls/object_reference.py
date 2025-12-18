num1 = 1
num2 = [2]
num3 = [3]

lst1 = [num1, num2, num3[0]]

num1 += 42
num2[0] += 42
num3[0] += 42

print(lst1) # what prints here?
