"""
Exercise 1
Create a Car class that makes the following code work as indicated:
"""

class Car:
    def __init__(self, id, year, colour):
        self.id = id
        self.year = year
        self.colour = colour

    def __str__(self):
        return f"{self.colour.capitalize()} {self.year} {self.id}"
        
    def __repr__(self):
        return f"Car({repr(self.id)}, {repr(self.year)}, {repr(self.colour)})"

vwbuzz = Car('ID.Buzz', 2024, 'red')
print(vwbuzz)        # Red 2024 ID.Buzz
print(repr(vwbuzz))  # Car('ID.Buzz', 2024, 'red')
