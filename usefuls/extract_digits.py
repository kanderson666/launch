num = 4936
num_temp = num
size = 1

while True:
    if num_temp // 10 >= 1:
        size += 1
        num_temp //= 10
    else:
        break

for n in range(size):
    # prints digits forwards (4-6) 
    num_temp = num
    num_temp //= (10**(size - n - 1))

    print(num_temp % 10)


    # prints digits backwards (6-4)
    #print(num % 10)
    #num //= 10
