def century(year):
    century = (year - 1) // 100 + 1

    if century > 10 and 10 < int(str(century)[-2:]) < 20:
        return str(century) + "th"
    
    match str(century)[-1]:
        case "1": end = "st"
        case "2": end = "nd"
        case "3": end = "rd"
        case _: end = "th"
        
    return str(century) + end


print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True