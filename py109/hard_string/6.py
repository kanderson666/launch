# 1. Normalize and compare sentences

"""
Write a function `same_sentence(str1, str2)` that returns True if
two sentences are the same up to:

- case differences (ignore case)
- extra spaces (treat multiple spaces as one)
- leading and trailing whitespace
- punctuation differences: ignore `.`, `!`, and `?` at the end of the sentence

Examples:
same_sentence(" Hello   world! ", "hello world")          -> True
same_sentence("Python is fun.", "python   is   fun?!")    -> True
same_sentence("Launch School", "Launch  School!")         -> True
same_sentence("Hi there", "Hi there buddy")               -> False
"""
def clean_string(str):
    str = str.strip()
    
    str = str.rstrip(".!?")
    str = " ".join(str.split())
    print(f"'{str}'")
    return str

def same_sentence(str1, str2):
    str1 = clean_string(str1)
    str2 = clean_string(str2)

    return str1.casefold() == str2.casefold()

print(same_sentence(" Hello   world! ", "hello world"))        #   -> True
print(same_sentence("Python is fun.", "python   is   fun?!")) #    -> True
print(same_sentence("Launch School", "Launch  School!")) #         -> True
print(same_sentence("Hi there", "Hi there buddy")) #               -> False
