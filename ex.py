
def join_or(list1, delim=', ', end='or'):
    list1 = [str(item) for item in list1]
    match len(list1):
        case 0:
            return ''
        case 1:
            return list1[0]
        case 2:
            return f'{list1[0]} {end} {list1[1]}'
    
    string = delim.join(list1[:-1])
    string += f'{delim}{end} {list1[-1]}'
    return string
    

print(join_or([1, 2]))                   # => "1 or 2"
print(join_or([1, 2, 3]))                # => "1, 2, or 3"
print(join_or([1, 2, 3], '; '))          # => "1; 2; or 3"
print(join_or([1, 2, 3], ', ', 'and'))   # => "1, 2, and 3"
