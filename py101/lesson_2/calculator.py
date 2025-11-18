# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.
def validate_number(number):
    try:
        int(number)
    except ValueError:
        return True
    return False

print('Welcome to Calculator!')

first_number = input("==> What is the 1st number? ")
while validate_number(first_number):
    first_number = input("==> What is the 1st number? ")

second_number = input("==> What is the 2nd number? ")
while validate_number(second_number):
    second_number = input("==> What is the 2nd number? ")

operation = input("==> What operator? ")
while operation not in ["+", "-", "*", "/"]:
    operation = input("==> What operator? ")
result = 0

match operation:
    case "+":
        result = int(first_number) + int(second_number)
    case "-":
        result = int(first_number) - int(second_number)
    case "*":
        result = int(first_number) * int(second_number)
    case "/":
        result = int(first_number) / int(second_number)
    case _:
        print("Invalid operator")
print(result)
