num1 = 1
num2 = [2]
num3 = [3]

lst1 = [num1, num2, num3[0]]    # int, list, int

num1 += 42  # 43
num2[0] += 42   # 44
num3[0] += 42   # 45

print(lst1) # what prints here? 1, [44], 3
