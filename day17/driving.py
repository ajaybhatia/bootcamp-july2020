class DrivingTest:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_allowed(self):
        return self.age >= 18 and self.age <= 60

    def result(self):
        if (self.is_allowed()):
            print(f"{self.name} is allowed to drive")
        else:
            print(
                f"{self.name} is not allowed to drive because of age which is {self.age}")


test1 = DrivingTest("Ajay", 91)
# if (test1.is_allowed()):
#             print(f"{test1.name} is allowed to drive")
#         else:
#             print(
#                 f"{test1.name} is not allowed to drive because of age which is {test1.age}")
test1.result()


test2 = DrivingTest("Alka", 61)
# if (test2.is_allowed()):
#             print(f"{test2.name} is allowed to drive")
#         else:
#             print(
#                 f"{test2.name} is not allowed to drive because of age which is {test2.age}")
test2.result()
