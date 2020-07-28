class Room:
    # Constructor
    def __init__(self, length, width, height):
        self.length = length  # Memeber variables or instance variables
        self.width = width
        self.height = height

    def volume(self):  # Member method or instance method
        return self.length*self.width*self.height

    def __str__(self):
        return f"Room length={self.length}, width={self.width}, height={self.height}"

# Variable is used with implicit (in-built) types
# Instance or object is used with classes


room = Room(10, 20, 10)
print(f"Volume of room is {room.volume()}")
print(room)


class Fruit:
    def __init__(self, name="Apple"):
        self._name = name

    @property
    def name(self):
        return self._name


fruit1 = Fruit()
print(fruit1.name)

fruit2 = Fruit("Banana")
print(fruit2.name)
