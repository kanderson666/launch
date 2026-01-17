"""
https://launchschool.com/lessons/76ecb255/assignments/12259fac
Compute and display the total age of the family's male members. Try working out the answer two ways: 
- first with an ordinary loop, then
- with a comprehension.
The result should be 444.
"""

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}
total_age = 0
for info in munsters.values():
    if info['gender'] == 'male':
        total_age += info['age']
print(total_age)

ages = [info['age'] for info in munsters.values() if info['gender'] == 'male']
print(sum(ages))