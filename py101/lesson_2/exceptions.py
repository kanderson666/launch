def lower_first(word):
    try:
        return word[0].lower() + word[1:]
    except (TypeError, IndexError):
        print("Hi")
        return word  # Handle exceptions by returning `word` as-is

print(lower_first("FOO"))  # Output: "fOO"
print(lower_first(""))     # Output: "32"