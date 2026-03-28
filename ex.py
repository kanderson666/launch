import re

text = ("A grey cat\n" +
    "A blue caterpillar\n" +
    "The lazy dog\n" +
    "The white cat\n" +
    "A loud dog\n" +
    "--A loud dog\n" +
    "Go away dog\n" +
    "The ugly rat\n" +
    "The lazy, loud dog")

print(re.findall(r"^(A|The) [a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z] (cat|dog)$", text, flags=re.M))
