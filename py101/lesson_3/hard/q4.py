def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    if len(dot_separated_words) != 4:
        return False
    
    while dot_separated_words:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False

    return True

def is_an_ip_number(number):
    if not number.isdigit():
        return False
    
    return True if (int(number) >= 0) and (int(number) <= 255) else False
        

ip = "199.1.1.1"

print(is_dot_separated_ip_address(ip))