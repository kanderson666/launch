# 2. Compress repeated characters

"""
Write a function `compress(text)` that does a simple run-length encoding
on a string:

- Consecutive repeated characters are replaced by:
    "<char><count>" if count > 1
  Single characters stay as they are.
- Keep the original character order.
- Don't use external libraries.

Examples:
compress("aaabbc")        -> "a3b2c"
compress("Helloooo!!!")   -> "Hel2o4!3"
compress("abcd")          -> "abcd"
compress("")              -> ""
"""

def compress(text):
    if not text:
        return ""
    count = 0
    last = text[0]
    result = text[0]
    for char in text:
        if char == last:
            count += 1
        else:
            if count > 1:
                result += str(count)
            result += char
            last = char
            count = 1
    if count > 1:
        result += str(count)
        
    return result

print(compress("aaabbc"))#        -> "a3b2c"
print(compress("Helloooo!!!"))#   -> "Hel2o4!3"
print(compress("abcd"))#          -> "abcd"
print(compress(""))#              -> ""
