class Number:
    def __init__(self, val):
        self.__val = val  # Using __ as prefix to member variable, we can make it private to class

    # Getter
    @property
    def value(self):
        return self.__val

    # Setter
    @value.setter
    def value(self, val):
        self.__val = val

    def is_even(self):
        return self.__val % 2 == 0

    def is_odd(self):
        return not self.is_even()

    def is_prime(self):
        if self.is_even() or self.__val == 1:
            return False
        for i in range(3, int(self.__val**0.5)+1):
            if self.__val % i == 0:
                return False
        return True

    def reverse(self):
        num, temp = self.__val, 0
        while num > 0:
            d = num % 10
            temp += d*10**(len(str(num))-1)
            num //= 10
        return temp


num = Number(10)
print(num.is_even())
print(num.is_odd())

# __member_property can be still accessed outside the class using the follwing instruction
# print(num._Number__val)
print(num.value)

num.value = 13
print(num.is_even())
print(num.is_prime())

num.value = 12345
print(num.reverse())
