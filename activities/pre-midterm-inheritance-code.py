class Animal:
    def __init__(self, name):
        self._x = 0
        self._y = 0
        self._name = name

    def speak(self):
        print(f'{self._name} says hello from ({self._x},{self._y})')

    def move(self):
        self._x += 1
        self._y += 1

class Dog(Animal):
    def speak(self):
        print("woof woof")
        super().speak()

    def move(self):
        self._x += 2
        self._y += 2


class Cat(Animal):
    def __init__(self, name):
        self._z = 0
        super().__init__(name)

    def speak(self):
        print(f'meow from height {self._z}')
        super().speak()

    
    def jump(self):
        self._z += 2


if __name__ == '__main__':
    a = Animal('Bob')
    d = Dog('Chewie')
    c = Cat('Coco')

    print('A:')
    a.move()
    a.speak()

    print('D:')
    d.move()
    d.speak()

    print('C:')
    c.move()
    c.speak()
    c.jump()
    c.speak()

    print('A again:')
    a.jump()
