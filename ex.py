def sum_square_difference(count):
    sum = sum(range(1, count + 1))

    sum_of_squares = 0
    for i in range(1, count + 1):
        sum_of_squares += i**2

    return sum**2 - sum_of_squares
print(sum_square_difference(3))
