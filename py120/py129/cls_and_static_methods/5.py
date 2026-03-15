"""
Problem 5: Utility static methods in a math helper class

Create a MathHelper class that groups some utility functions as static methods.

Requirements:

Implement the following static methods (no self or cls):
is_even(n) → returns True if n is even, else False.
is_prime(n) → returns True if n is a prime number, else False (assume n >= 0).
clamp(value, min_value, max_value) → returns value clamped between min_value and max_value.
These methods should not depend on any instance or class state.
"""

class MathHelper:
    @staticmethod
    def is_even(n):
        return not n % 2
        
    @staticmethod
    def is_prime(n):
        if n < 2:
            return False

        for num in range (2, n):
            if n % num == 0:
                return False
        return True
        
    @staticmethod
    def clamp(value, min_value, max_value):
        if value < min_value:
            return min_value
        if value > max_value:
            return max_value
        else:
            return value


# Test cases
if __name__ == '__main__':
    # is_even
    assert MathHelper.is_even(0) is True
    assert MathHelper.is_even(1) is False
    assert MathHelper.is_even(2) is True
    assert MathHelper.is_even(15) is False

    # is_prime (simple checks)
    assert MathHelper.is_prime(0) is False
    assert MathHelper.is_prime(1) is False
    assert MathHelper.is_prime(2) is True
    assert MathHelper.is_prime(3) is True
    assert MathHelper.is_prime(4) is False
    assert MathHelper.is_prime(17) is True

    # clamp
    assert MathHelper.clamp(5, 0, 10) == 5
    assert MathHelper.clamp(-1, 0, 10) == 0
    assert MathHelper.clamp(100, 0, 10) == 10

    print("Problem 5 tests passed.")
