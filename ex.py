
x = [[1, 2], 3, 4, 5]

def foo(lst):
    lst[0] += lst[0] + [3]

def bar(lst):
    lst[0] += lst[0] + [3]

foo(x)
print(x)    # [[1, 2, 3], 3, 4]

bar(x)      # [[1, 2, 3], 3, 4, 6]
print(x)
