def is_bouncy(string):
    ascending = list(string) == sorted(string)
    descending = list(string) == sorted(string, reverse=True)
    
    return not ascending and not descending
    

def bouncyCount(numbers):
    count = 0
    string_numbers = []
    
    for number in numbers:
        string_numbers.append(str(number))
        
    for string in string_numbers:
        if is_bouncy(string):
            count += 1
    
    return count

# Python test cases:
print(bouncyCount([]) == 0)
print(bouncyCount([11, 0, 345, 21]) == 0)
print(bouncyCount([121, 4114]) == 2)
print(bouncyCount([176, 442, 80701644]) == 2)
print(bouncyCount([1222]) == 0)