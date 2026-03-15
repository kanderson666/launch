"""
Problem 3: Static method for validation

Create a User class that uses a static method to validate usernames.

Requirements:

The constructor takes a username string and stores it on self.username.
A valid username:
is at least 3 characters long
contains only letters, digits, or underscores (you can use str.isalnum() plus allow _, or whatever approach you like).
Write a static method is_valid_username(username) that returns True or False.
In __init__, use this static method to validate the given username.
If invalid, raise a ValueError.
"""

class User:
    def __init__(self, username):
        if not self.__class__.is_valid_username(username):
            raise ValueError
        self.username = username

    @staticmethod
    def is_valid_username(username):
        if len(username) < 3:
            return False

        username = username.replace('_', '')
        if not username.isalnum():
            return False

        return True


# Test cases
if __name__ == '__main__':
    u1 = User('alice_1')
    assert u1.username == 'alice_1'

    u2 = User('Bob')
    assert u2.username == 'Bob'

    # Directly testing the static method
    assert User.is_valid_username('abc') is True
    assert User.is_valid_username('a') is False
    assert User.is_valid_username('a b') is False

    # Invalid usernames should raise ValueError
    invalid_usernames = ['a', 'ab', 'inv@lid', 'with space']
    for name in invalid_usernames:
        try:
            User(name)
            assert False, f"Expected ValueError for username: {name}"
        except ValueError:
            pass

    print("Problem 3 tests passed.")
