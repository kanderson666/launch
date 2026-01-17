"""
Given the following data structure, write some code to return a list 
that contains the colors of the fruits and the sizes of the vegetables. 
The sizes should be uppercase, and the colors should be capitalized.
'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    }
"""
dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

# new_lst = []
# for qualities in dict1.values():
#     if qualities['type'] == 'fruit':
#         new_lst.append([color.capitalize() for color in qualities['colors']])
#     else:
#         new_lst.append(qualities['size'].upper())

def fruit_or_veg(qualities):
    if qualities['type'] == 'fruit':
        return [color.capitalize() for color in qualities['colors']]
    else:
        return qualities['size'].upper()

new_lst = [fruit_or_veg(qualities) for qualities in dict1.values()]
print(new_lst)



# Expected:
# [["Red", "Green"], "MEDIUM", ["Orange"], "LARGE"]
