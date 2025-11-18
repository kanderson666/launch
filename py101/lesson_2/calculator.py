# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.
import json

def validate_number(number):
    try:
        int(number)
    except ValueError:
        return True
    return False

def validate_response(response):
    if response in ["y", "n"]:
        return True
    else:
        return False

# Open the JSON file for reading
with open('calc_config.json', 'r') as file:
    data = json.load(file)        

print(data["welcome"])

while True:
    first_number = input(data["first_msg"])
    while validate_number(first_number):
        first_number = input(data["first_msg"])

    second_number = input(data["second_msg"])
    while validate_number(second_number):
        second_number = input(data["second_msg"])

    operation = input(data["operator"])
    while operation not in ["+", "-", "*", "/"]:
        operation = input(data["operator"])
    
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

    response = input(data["again"])
    while not validate_response(response):
        response = input(data["again"])
    
    if response == 'n':
        break

