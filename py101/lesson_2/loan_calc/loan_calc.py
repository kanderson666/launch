import json

def check_float(message):
    while True:
        num = input(MESSAGE[message])
        try:
            float(num)
        except (ValueError, TypeError):
            print(MESSAGE["float_issue"])
        else:
            return float(num)

# Open the JSON file for reading
with open('loan_calc.json', 'r') as file:
    MESSAGE = json.load(file)

loan_amount = check_float("loan")
interest_rate = check_float("interest") / 100
duration = check_float("duration") * 12
monthly_interest = interest_rate / 12

'''
m = p * (j / (1 - (1 + j) ** (-n)))
m = monthly payment
p = loan amount
j = monthly interest rate
n = loan duration in months
'''
payment = loan_amount * (monthly_interest / \
        (1 - (1 + monthly_interest) ** (-duration)))

#payment = round(payment, 2)     #round to 2 decimal places

print(f"Your monthly payment is: ${payment:,.2f}")
