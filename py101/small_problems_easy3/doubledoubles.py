# Your code goes here
def twice(num):
    str_num = str(num)
    
    return num if is_double(str_num) else num * 2

def is_double(str_num):
    if len(str_num) % 2:
        return False
    
    first_half = str_num[:len(str_num)//2]
    second_half = str_num[len(str_num)//2:]
    
    return True if first_half == second_half else False

print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True