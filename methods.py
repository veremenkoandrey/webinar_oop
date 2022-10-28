class Bird:
    """Test"""
    def __init__(self):
        pass

    def show(self):
        print('I\'m bird!')
        self._protected()

    def _protected(self):
        print('I\'m protected!')

    def __private(self):
        print('I\'m private!')

b = Bird()
b._protected()
print(b.__doc__)
print(dir(b))
