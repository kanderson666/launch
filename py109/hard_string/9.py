# 4. Custom strip: remove characters from both ends

"""
Implement a function `custom_strip(s, chars)` that behaves like
`str.strip(chars)` but without calling `strip` directly.

- `chars` is a string of characters to remove from both the start and end.
- Remove those characters repeatedly from the beginning and end.
- Do not remove characters from the middle.

Examples:
custom_strip("--hello--", "-")            -> "hello"
custom_strip("..,,hi..", ".,")            -> "hi"
custom_strip("xyxxyabcxy", "xy")          -> "abc"
custom_strip("###", "#")                  -> ""  (everything stripped)
"""

def custom_strip(s, chars = " "):
    if not s:
        return ""
    for idx, char in enumerate(s):
        if char not in chars:
            s = s[idx:]
            break
        if idx == len(s) - 1:
            return ""
    for idx, char in enumerate(s[::-1]):
        if char not in chars:
            if idx != 0:
                s = s[:-idx]
            break
    return s


print(custom_strip("--hello--", "-"))#            -> "hello"
print(custom_strip("..,,hi..", ".,"))#            -> "hi"
print(custom_strip("xyxxyabcxy", "xy"))#          -> "abc"
print(custom_strip("###", "#"))#                  -> ""  (everything stripped)

