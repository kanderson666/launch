"""
Exercise 5
Create a Person class with two instance variables to hold a person's first and last names. 
The names should be passed to the constructor as arguments and stored separately. 
The first and last names are required and must consist entirely of alphabetic characters.

The class should also have a getter method that returns the person's name as a full name 
(the first and last names are separated by spaces), with both first and last names capitalized correctly.

The class should also have a setter method that takes the name from a two-element tuple. 
These names must meet the requirements given for the constructor.

Yes, this class is somewhat contrived.

You can use the following code snippets to test your class. 
Since some tests cause exceptions, we've broken them into separate snippets.
"""

class Person:
    NAME_ERROR = 'Names must only be alphabetic characters'

    def __init__(self, first_name, last_name):
        self.name = (first_name, last_name)

    @property
    def name(self):
        return f"{self._first_name} {self._last_name}"

    @name.setter
    def name(self, full_name):
        first_name, last_name = full_name
        if not first_name.isalpha() or not last_name.isalpha():
            raise ValueError(Person.NAME_ERROR)

        self._first_name = first_name.capitalize()
        self._last_name = last_name.capitalize()

actor = Person('Mark', 'Sinclair')
character = Person('annIE', 'HAll')
friend = Person('Lynn', 'Blake')

print(actor.name)              # Mark Sinclair
actor.name = ('Vin', 'Diesel')
print(actor.name)              # Vin Diesel
print(character.name)          # Annie Hall
print(friend.name)             # Lynn Blake

# actor.name = ('', 'Diesel')
# ValueError: Name must be alphabetic.

# character = Person('Da5id', 'Meier')
# # ValueError: Name must be alphabetic.

# friend.name = ('Lynn', 'Blake-John')
# # ValueError: Name must be alphabetic.
