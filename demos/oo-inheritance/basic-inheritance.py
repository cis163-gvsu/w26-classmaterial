class Animal:
    def __init__(self, name):
        self.name = name

    def random(self):
        print('aaaaaah')

class Fish(Animal):
    def __init__(self, name):
        self.x = 0
        self.y = 0
        self.random() # calls child random
        super().random() # calls parent random
        super().__init__(name) # calls Animal constructor

    def random(self):
        print('noooooo')

    def move(self, xchange, ychange):
        self.x += xchange
        self.y += ychange

    def __str__(self):
        part1 = f'Fish named {self.name} '
        part2 = f'at location ({self.x},{self.y})'
        return part1 + part2

if __name__ == '__main__':
    flounder = Fish('flounder')
    bob = Animal('bob')
    bob.move(2,3)
