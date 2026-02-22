"""
Exercise 2
Using decorators, add getter and setter methods to your Car class so you can view and change the color of your car. 
You should also add getter methods that let you view but not modify the car's model and year. Don't forget to write some tests.
"""

# Your code goes here
class Car:
    def __init__(self, model, year, colour):
        self._model = model
        self._year = year
        self.colour = colour
        self.speed = 0
        self.engine_on = False
    def turn_on_engine(self):
        if self.engine_on:
            print("The engine is already on")
        else:
            self.engine_on = True
            print("The engine turns on.")
    def turn_off_engine(self):
        if self.engine_on:
            self.engine_on = False
            print("The engine turns off.")
        else:
            print("The engine is already on")
    def accelerate(self):
        if self.engine_on:
            print("The car accelerates.")
            self.speed += 5
        else:
            print("The car is not on.")
    def brake(self):
        if self.speed > 0:
            self.speed -= 5
            print("The car slows.")
        else:
            print("The car is already stopped.")
    def current_speed(self):
        print(f"Current speed: {self.speed}")
    @property
    def colour(self):
        return self._colour
    @colour.setter
    def colour(self, colour):
        self._colour = colour
    @property
    def model(self):
        return self._model
    @property
    def year(self):
        return self._year

honda = Car('crv', 2019, 'black')
print(honda.model)
print(honda.year)
print(honda.colour)
honda.colour = 'white'
print(honda.colour)

# honda.turn_on_engine()
# honda.accelerate()
# honda.current_speed() # 5
# honda.turn_off_engine()
# honda.accelerate()
# honda.current_speed() # 5
# honda.turn_on_engine()
# honda.accelerate()
# honda.current_speed() # 10
# honda.brake()
# honda.brake()
# honda.brake()
# honda.brake()
# honda.current_speed() # 0

