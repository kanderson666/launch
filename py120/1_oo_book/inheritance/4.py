"""
Exercise 4
Print the method resolution order for cars, trucks, boats, and vehicles as defined in the previous exercise.
"""

class SignalMixin:
    def signal_left(self):
        print('signalling left')
    def signal_right(self):
        print('signalling right')
    def signal_off(self):
        print('signal is now off')

class Vehicle:
    num_vehicles = 0
    def __init__(self):
        Vehicle.num_vehicles += 1

    @classmethod
    def vehicles(cls):
        return Vehicle.num_vehicles

class Car(SignalMixin, Vehicle):
    def __init__(self):
        super().__init__()


class Truck(SignalMixin, Vehicle):
    def __init__(self):
        super().__init__()

class Boat(Vehicle):
    def __init__(self):
        super().__init__()

car1 = Car()
truck1 = Truck()
boat1 = Boat()

print(Car.mro())
print(Truck.mro())
print(Boat.mro())
print(Vehicle.mro())
