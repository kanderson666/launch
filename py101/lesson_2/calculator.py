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

# manually setting language selection for welcome message to prove concept
language = "ES"     
print(data[language]["welcome"])

while True:
    first_number = input(data["EN"]["first_msg"])
    while validate_number(first_number):
        first_number = input(data["EN"]["first_msg"])

    second_number = input(data["EN"]["second_msg"])
    while validate_number(second_number):
        second_number = input(data["EN"]["second_msg"])

    operation = input(data["EN"]["operator"])
    while operation not in ["+", "-", "*", "/"]:
        operation = input(data["EN"]["operator"])
    
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

    response = input(data["EN"]["again"])
    while not validate_response(response):
        response = input(data["EN"]["again"])
    
    if response == 'n':
        break

