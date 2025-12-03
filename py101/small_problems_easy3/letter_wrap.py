# Your code goes here
from math import ceil
MAX_LEN = 40

def print_in_box(string):
    # get length of string, store each printed line in list
    length = len(string)
    str_lines = []
    
    # calc required number of lines to fit string, minimum of 1 line (empty string)
    num_lines = ceil(length / MAX_LEN)
    if not num_lines:
        num_lines = 1
    chars_in_line = ceil(length / num_lines)
    
    for i in range(num_lines):
        str_lines.append(string[i * chars_in_line : 
                                (i + 1) * chars_in_line])
        
        # add padding to final line if needed
        padding = " " * (chars_in_line - len(str_lines[i]))
        str_lines[i] += padding
    
    horizontal = "+-" + ("-" * chars_in_line) + "-+"
    vertical = "| " + (" " * chars_in_line) + " |"
    
    print(horizontal)
    print(vertical)
    
    for i in range(num_lines):
        print("| " + str_lines[i] + " |")
    
    print(vertical)
    print(horizontal)
        

print_in_box('To boldly go where no one has gone before.')
print_in_box("Modify this function so that it truncates the message if it doesn't fit inside a maximum width provided as a second argument (the width is the width of the box itself). You may assume no maximum if the second argument is omitted.")