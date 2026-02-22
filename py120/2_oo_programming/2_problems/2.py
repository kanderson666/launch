"""
Modify the class definition from above to facilitate the following methods. Note that there is no name= setter method now.
Hint: let first_name and last_name be "states" and create a property that uses those states.
"""

class Person:
    def __init__(self, first_name):
        self.first_name = first_name
        self.last_name = ""

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'
    
    # @name.setter
    # def name(self, name):
    #     self._name = name
    
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, name):
        self._first_name = name
    
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, name):
        self._last_name = name

bob = Person('Robert')
print(bob.name)             # Robert
print(bob.first_name)       # Robert
print(repr(bob.last_name))  # ''
bob.last_name = 'Smith'
print(bob.name)             # Robert Smith





















# class Person:
#     def __init__(self, name):
#         parts = name.split()
#         self.first_name = parts[0]
#         self.last_name = ''
#         if len(parts) > 1:
#             self.last_name = parts[1]

#     @property
#     def name(self):
#         return f'{self.first_name} {self.last_name}'.strip()

#     @property
#     def first_name(self):
#         return self._first_name

#     @first_name.setter
#     def first_name(self, first_name):
#         self._first_name = first_name

#     @property
#     def last_name(self):
#         return self._last_name

#     @last_name.setter
#     def last_name(self, last_name):
#         self._last_name = last_name
