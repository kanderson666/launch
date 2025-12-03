# Your code goes here
from math import ceil
MAX_LEN = 20

def print_in_box(string):
    if len(string) > MAX_LEN:
        lines = word_wrap(string)
        chars_in_line = MAX_LEN

    else:
        lines = []
        lines.append(string)
        chars_in_line = len(string)
    
    print_box(lines, chars_in_line)
        
def word_wrap(string):
    words = string.split()
    lines = [""]
    char_count = 0

    for word in words:
        # cant fit word- wrap
        if len(word) + char_count > MAX_LEN:
            lines[-1] += " " * (MAX_LEN - len(lines[-1]))   # add padding to complete line
            lines.append(word + " ") 
            char_count = len(word + " ") 

        # cant fit space after word, wrap after word
        elif len(word + " ") + char_count > MAX_LEN:
            lines[-1] += word
            lines.append("")
            char_count = 0 

        # can fit word and space
        else:
            lines[-1] += word + " "
            char_count += len(word + " ")
    
    # add padding to last line
    lines[-1] += " " * (MAX_LEN - len(lines[-1])) 
    return lines

def print_box(lines, chars_in_line):
    horizontal = "+-" + ("-" * chars_in_line) + "-+"
    vertical = "| " + (" " * chars_in_line) + " |"
    
    print(horizontal)
    print(vertical)
    
    for i in range(len(lines)):
        print("| " + lines[i] + " |")
    
    print(vertical)
    print(horizontal)

print_in_box('To boldly go where no one has gone before.')
print_in_box("Modify this function so that it truncates the message if it doesn't fit inside a maximum width provided as a second argument (the width is the width of the box itself). You may assume no maximum if the second argument is omitted.")