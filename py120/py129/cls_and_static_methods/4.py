"""
Problem 4: Class-level configuration with class methods

Create a Logger class with a class-level configuration.

Requirements:

Use a class variable level with a default value, e.g., 'INFO'.
Provide class methods:
get_level() → returns the current logging level.
set_level(new_level) → sets the logging level.
Provide an instance method log(message) that prints the message prefixed with the current level, e.g., "[INFO] hello".
If you want, you can capture printed output with io.StringIO and test the actual strings, but that’s optional.
"""

class Logger:
    level = 'INFO'

    @classmethod
    def get_level(cls):
        return cls.level
    
    @classmethod
    def set_level(cls, new_level):
        cls.level = new_level

    def log(self, message):
        print(f'[{self.__class__.level}] {message}')

# Test cases
if __name__ == '__main__':
    assert Logger.get_level() == 'INFO'

    logger1 = Logger()
    logger2 = Logger()

    # You can visually inspect these prints or just ensure no errors:
    logger1.log("First message")  # should include [INFO]

    Logger.set_level('DEBUG')
    assert Logger.get_level() == 'DEBUG'

    # Instance should see the updated level too
    logger2.log("Second message")  # should include [DEBUG]

    # Should reflect the same class variable
    assert logger1.get_level() == 'DEBUG'

    print("Problem 4 tests (basic checks) passed.")
