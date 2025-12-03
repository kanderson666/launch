# Your code goes here
def penultimate(string):
    words = tokenize(string)
    if words[0] == "":
        return None
    return words[len(words) // 2]
def tokenize(string):
    return string.split(" ")

# These examples should print True
print(penultimate(""))
print(penultimate("Launch school is not cool"))