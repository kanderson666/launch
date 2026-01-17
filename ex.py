statement = "The Flintstones Rock"

result = {}

for char in statement:
    if char.isspace():
        continue
    result[char] = result.get(char, 0) + 1
print(result)