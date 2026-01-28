"""
Problem:
    - Return number if all digits of input number were squared   
        -ex 84 come out as 6416 since 8^2 = 64 and 4^2 = 16
Input:
    - integer
Output:
    - Integer (concatenation of squared digits from input)
Rules:
    - All input are positive

Data:
    - Integer input
    - Integer output
    Intermediary:
        - String equivalent of input
        - String to create output

Algo:
    - Convert input to string
    - Iterate through each digit of string number
        - Concatenate square of digit onto result
"""

def square_digits(num):
    num_str = str(num)
    result = ""
    for digit in num_str:
        result += str(int(digit)**2)
    return int(result)


print(square_digits(0) ==    0)
print(square_digits(64) ==   3616)
print(square_digits(1111) == 1111)
print(square_digits(2222) == 4444)
print(square_digits(3333) == 9999)
print(square_digits(3212) == 9414)
print(square_digits(1234) == 14916)
print(square_digits(77455754) == 4949162525492516)
print(square_digits(99999999) == 8181818181818181)