# Tracing Exceptions 

Consider the following code:

```
from abc import ABC, abstractmethod
import math

class Mammal(ABC):
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    @abstractmethod
    def move(self, distance, time):
        pass

    def get_speed(self, distance, time, dims):
        # Euclidean distance based on number of dimensions moved
        actual_distance = math.sqrt(dims * (distance ** 2))
        return actual_distance / time  # Potential ZeroDivisionError

    def describe(self, distance, time, dims):
        speed = self.get_speed(distance, time, dims)
        return f"{self.name} at ({self.x}, {self.y}) moves at {speed} units/time"


class Dog(Mammal):
    def move(self, distance, time):
        self.x += distance
        self.y += distance
        return self.describe(distance, time, 2)

    def bark(self):
        return "Woof!"


class Bat(Mammal):
    def __init__(self, name, x, y, z):
        super().__init__(name, x, y)
        self.z = z

    def move(self, distance, time):
        return self.fly(distance, time)

    def fly(self, distance, time):
        # Moves equally in x, y, z (3D movement)
        self.x += distance
        self.y += distance
        self.z += distance
        return self.describe(distance, time, 3)

    def describe(self, distance, time, dims):
        speed = self.get_speed(distance, time, dims)
        return f"{self.name} at ({self.x}, {self.y}, {self.z}) flies at {speed} units/time"


if __name__ == '__main__':
    animals = [
        Dog("Buddy", 0, 0),
        Bat("Bruce", 0, 0, 0),
        Dog("Max", 5, 5)
    ]

    moves = [
        (animals[0], 100, 10),
        (animals[1], 50, 0),
        (animals[2], 30, 5)
    ]

    for move in moves:
        a, d, t = move
        try:
            print(a.move(d, t))
        except ArithmeticError:
            print(f"Arithmetic issue with {a.name}")
        except ZeroDivisionError:
            print(f"Cannot divide by zero for {a.name}")
        except Exception:
            print(f"General error with {a.name}")
        else:
            print("Cool cool cool")
        finally:
            print(f"Finished processing {a.name}")

        print(a.x)
        print(a.y)
        try:
            print(a.z)
        except AttributeError:
            continue
```

What is the output of the code?


<br><br><br><br><br><br>



