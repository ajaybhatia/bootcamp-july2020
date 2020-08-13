def greeting(name):
    return f"Hello, {name}"


def is_positive(num):
    return num > 0


def is_even(num):
    return num % 2 == 0


class MyClass:
    def __init__(self, val):
        self.__val = val


obj = MyClass(10)
print(obj.__val)
