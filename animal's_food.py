class Animal():

    def __init__(self, name):  # создается в первую очередь
        self.name = name
        self.alive = True
        self.fed = False

    def __str__(self):
        return f'name: {self.name}; feed: {self.fed}; alive: {self.alive}'

    def eat(self, food):
        if food.edible:
            self.fed = True
            print(f'\033[3m{self.name}\033[0m съел \033[3m{food.name}\033[0m')
        else:
            self.alive = False
            print(f'\033[3m{self.name}\033[0m не стал есть \033[3m{food.name}\033[0m')


class Plant:
    edible = False  # создается в тертью очередь

    def __init__(self, name):  # создается в первую очередь
        self.name = name

    def __str__(self):
        return f'name: {self.name}; edible: {self.edible}'


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True  # создается во вторую очередь


if __name__ == '__main__':
    animal1 = Mammal('The Cow')
    animal2 = Predator('The Tiger')
    plant1 = Flower('a rouse')
    plant2 = Fruit('an apple')

    print(animal1)
    print(animal2)
    print(plant1)
    print(plant2)
    print()

    animal1.eat(plant1)
    animal2.eat(plant2)
    print()

    print(animal1)
    print(animal2)
