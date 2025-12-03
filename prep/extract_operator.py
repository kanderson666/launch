# Your code goes here
def calculate(num1, num2, operator):
    match operator:
        case '+': return num1 + num2
        case '-': return num1 - num2
        case '%': return num1 % num2
        case '**': return num1 ** num2
num1 = float(input("1st: "))
num2 = float(input("2nd: "))

for operator in ['+', '-', '%', '**']:
    operation = f"{num1} {operator} {num2}" 
    result = calculate(num1, num2, operator)
    print(f"{operation} = {result}")
