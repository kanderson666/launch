class MyError(Exception):
    def __init__(self, message='Uh-ohhh'):
        super().__init__(message)

test = {}
try:
    try:
        test[2]
    except KeyError as e:
        print(e)
        print(e.__cause__)
        raise MyError from e
except MyError as e:
    print(e)
    print(e.__cause__)
