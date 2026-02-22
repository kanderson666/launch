"""
Using the class definition from problem 3, let's create some more people (Person objects):
    Without adding any code to the Person class, we want to compare bob and rob to see whether they both have the same name. How can we make this comparison?
"""
class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'
    
    @name.setter
    def name(self, name):
        split = name.split()
        self.first_name = split[0]
        self.last_name = ""
        if len(split) > 1:
            self.last_name = split[1]

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


bob = Person('Robert Smith')
rob = Person('Robert Smith')

print(bob.name == rob.name)






























# print(bob.name == rob.name)         # True

# str1 = 'hello world'
# str2 = 'hello world'

# print(str1 == str2)            # True