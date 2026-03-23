"""
Create a function named print_message that requires a keyword-only argument (message) 
and an optional keyword-only argument (level) with a default value of "INFO". 
The function should print out the message prefixed with the level. 
The function shouldn't accept any positional arguments.
"""

def print_message(*, message, level='INFO'):
    return f'{level} {message}'

print(print_message(message='hello'))
print(print_message(level=1, message='hello'))
print(print_message(message='hello', level=1))
