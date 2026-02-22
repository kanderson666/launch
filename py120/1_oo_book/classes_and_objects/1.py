"""
Exercise 1
Create a Car class that meets these requirements:

Each Car object should have a model, model year, and color provided at instantiation time.
You should have an instance variable that keeps track of the current speed. Initialize it to 0 when you instantiate a new car.
Create instance methods that let you turn the engine on, accelerate, brake, and turn the engine off. Each method should display an appropriate message.
Create a method that prints a message about the car's current speed.
Write some code to test the methods.
"""

# Your code goes here
class Car:
    def __init__(self, model, year, colour):
        self.model = model
        self.year = year
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

honda = Car('crv', 2019, 'black')
honda.turn_on_engine()
honda.accelerate()
honda.current_speed() # 5
honda.turn_off_engine()
honda.accelerate()
honda.current_speed() # 5
honda.turn_on_engine()
honda.accelerate()
honda.current_speed() # 10
honda.brake()
honda.brake()
honda.brake()
honda.brake()
honda.current_speed() # 0

