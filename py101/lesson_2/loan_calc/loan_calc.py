import json

# Open the JSON file for reading
with open('loan_calc.json', 'r') as file:
    MESSAGE = json.load(file)

def check_input(message):
    while True:
        num = input(MESSAGE[message])
        try:
            num = float(num)
            if num <= 0:
                raise ValueError
        except (ValueError, TypeError):
            print(MESSAGE["float_issue"])
        else:
            return float(num)

'''
m = p * (j / (1 - (1 + j) ** (-n)))
m = monthly payment
p = loan amount
j = monthly interest rate
n = loan duration in months
'''
def calc_payment():
    return loan_amount * (monthly_interest / 
        (1 - (1 + monthly_interest) ** (-duration)))

loan_amount = check_input("loan")
interest_rate = check_input("interest") / 100
duration = check_input("duration") * 12
monthly_interest = interest_rate / 12

payment = calc_payment()

#payment = round(payment, 2)     #round to 2 decimal places
print(f"Your monthly payment is: ${payment:,.2f}")  #commas & 2 decimal places
