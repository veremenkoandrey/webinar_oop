class A:
    def __init__(self, a):
        self.a = a


class B:
    def __init__(self, b):
        self.b = b


class C(A, B):
    def __init__(self, a, b):
        A.__init__(self, a)
        B.__init__(self, b)


c = C(1, 2)
print(c.a)
print(c.b)
