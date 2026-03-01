class Silly:
    def __init__(self, value):
        if isinstance(value, int):
            self.value = value
        else:
            self.value = str(value)

    def __str__(self):
        return f'Silly({repr(self.value)})'

    def __add__(self, other):
        if not isinstance(other, (str, int)):
            return NotImplemented
        value_is_num = self._is_num(self.value)
        other_is_num = self._is_num(other)
        
        if value_is_num and other_is_num:
            return Silly(int(self.value) + int(other))
        else:
            return Silly(str(self.value) + str(other))
            
    @staticmethod
    def _is_num(value):
        if isinstance(value, int) or value.isdigit():
            return True
        return False

print(Silly('abc') + 'def')        # Silly('abcdef')
print(Silly('abc') + 123)          # Silly('abc123')
print(Silly(123) + 'xyz')          # Silly('123xyz')
print(Silly('333') + 123)          # Silly(456)
print(Silly(123) + '222')          # Silly(345)
print(Silly(123) + 456)            # Silly(579)
print(Silly('123') + '456')        # Silly(579)