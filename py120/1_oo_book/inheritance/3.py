"""
Exercise 3
Create a mix-in for the Car and Truck classes from the previous exercise that lets you operate the turn signals: 
    signal left, signal right, and signal off. 
Use the following code to test your code.
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

car1.signal_left()       # Signalling left
truck1.signal_right()    # Signalling right
car1.signal_off()        # Signal is now off
truck1.signal_off()      # Signal is now off
boat1.signal_left()
# AttributeError: 'Boat' object has no attribute
# 'signal_left'
