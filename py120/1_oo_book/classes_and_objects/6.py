"""
Exercise 6
Going back to your solution to exercise 1, refactor the code to replace any methods that can be converted to static methods. 
Once you have done that, ask yourself whether the conversion to a static method makes sense.
"""

class Car:
    @staticmethod
    def engine_start():
        print('The engine is on!')

honda = Car()
Car.engine_start()
honda.engine_start()
