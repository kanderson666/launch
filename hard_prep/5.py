# Consider this function intended to check if any permutation of a string s1 appears as a substring of s2:

def has_permutation(s1, s2):
    if len(s1) > len(s2):
        return False

    s1_sorted = sorted(s1)

    for i in range(len(s2) - len(s1) + 1):
        window = s2[i:i+len(s1)]
        if sorted(window) == s1_sorted:
            return True

    return False

print(has_permutation("ab", "eidbaooo"))
print(has_permutation("ab", "eidboaoo"))

# Questions:
# a) What does this code print?
# b) Can you think of a more efficient approach (describe it in words; you don’t need full code)?