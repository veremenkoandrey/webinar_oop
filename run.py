class Test():

    def add(self, other):
        return self.data + other.data

    @classmethod
    def class_method(cls):
        print('class method')
        print(cls)

    @staticmethod
    def static_method():
        print('static method')


Test.class_method()
Test.static_method()
t = Test()
t.static_method()
t.class_method()
