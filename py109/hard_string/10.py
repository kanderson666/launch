# 5. Check if two strings are isomorphic (by pattern)

"""
Write a function `is_isomorphic(s1, s2)` that returns True if
you can replace each character in s1 with a unique character
to get s2.

Rules:
- Each character in s1 always maps to the same character in s2.
- No two different characters in s1 can map to the same character in s2.
- Lengths must match.
- You must solve this using only basic operations and string methods
  (no external libraries).

Examples:
is_isomorphic("egg", "add")      -> True   (e->a, g->d)
is_isomorphic("foo", "bar")      -> False  (o would need to map to two chars)
is_isomorphic("paper", "title")  -> True
is_isomorphic("ab", "aa")        -> False  (a->a, b->a: two map to same)
"""

def is_isomorphic(s1, s2):
    def conversion_match(char1, char2, dict1):
        if char1 in dict1 and dict1[char1] != char2:
            return False
        return True
    
    if len(s1) != len(s2):
        return False
    
    c1_to_c2, c2_to_c1 = {}, {}
    zipped = zip(s1, s2)
    for c1, c2 in zipped:
        if not conversion_match(c1, c2, c1_to_c2):
            return False
        if not conversion_match(c2, c1, c2_to_c1):
            return False
        
        if c1 not in c1_to_c2 and c2 not in c2_to_c1:
            c1_to_c2[c1] = c2
            c2_to_c1[c2] = c1
            
    return True

print(is_isomorphic("egg", "add"))#      -> True   (e->a, g->d)
print(is_isomorphic("foo", "bar"))#      -> False  (o would need to map to two chars)
print(is_isomorphic("paper", "title"))#  -> True
print(is_isomorphic("ab", "aa"))#        -> False  (a->a, b->a: two map to same)
