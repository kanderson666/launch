def transform(strings):
    new_list = []
    for s in strings:
        if len(s) > 3:
            s = s.upper()
        new_list.append(s)
    return new_list

words = ["hi", "there", "cat", "python"]
result = transform(words)
print(result) # [hi, THERE, cat, PYTHON]
print(words) # ["hi", "there", "cat", "python"]
# Questions:
# a) What is printed?
# b) If we wanted to modify words in place so that it reflects the transformed values, 
#    how could we change transform without returning a new list? (Describe the changes in words or code.)