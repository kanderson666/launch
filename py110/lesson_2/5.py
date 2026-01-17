# Given the object shown below, print the name, age, and gender of each family member:
# ex: Herman is a 32-year-old male.

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

for person in munsters:
    age = munsters[person]['age']
    gender = munsters[person]['gender']
    print(f'{person} is a {age}-year-old {gender}.')

# solution
"""
for name, info in munsters.items():
    print(f"{name} is a {info['age']}-year-old {info['gender']}.")
"""