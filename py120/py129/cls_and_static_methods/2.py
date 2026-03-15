"""
Problem 2: Alternate constructor with class method

Create a Temperature class that stores temperature in Celsius, but allows creating instances from Fahrenheit using a class method.

Requirements:

The main constructor __init__ takes a single celsius value and stores it on an instance attribute (e.g., self.celsius).
Define a class method from_fahrenheit that:
takes a Fahrenheit value
converts it to Celsius
returns a new Temperature instance.

Provide an instance method to_fahrenheit that returns the temperature in Fahrenheit.
Conversion formulas:

C = (F - 32) * 5/9
F = C * 9/5 + 32
"""

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    
    # create class object using fahrenheit provided, instead of celsius
    @classmethod
    def from_fahrenheit(cls, fahr):
        celsius = (fahr - 32) * 5/9
        return cls(celsius)
    
    def to_fahrenheit(self):
        fahr = self.celsius * 9/5 + 32
        return fahr


# Test cases
if __name__ == '__main__':
    t1 = Temperature(0)
    assert round(t1.to_fahrenheit(), 2) == 32.00

    t2 = Temperature(100)
    assert round(t2.to_fahrenheit(), 2) == 212.00

    t3 = Temperature.from_fahrenheit(32)
    assert round(t3.celsius, 2) == 0.00

    t4 = Temperature.from_fahrenheit(212)
    assert round(t4.celsius, 2) == 100.00

    print("Problem 2 tests passed.")
