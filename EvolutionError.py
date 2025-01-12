from random import randint


class Animals:
    alive = True  # живой
    sound = None  # что говорит
    _DEGREE_OF_DANGER = 0  # уровень апасности

    def __init__(self, speed):
        self._cords = [0, 0, 0]  # координаты в пространстве
        self.speed = speed  # скорость передвижения

    def move(self, dx, dy, dz):  # записывает координаты * speed
        if (self._cords[2] + dz * self.speed) >= 0:  # Z: не может быть меньше 0
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] += dz * self.speed
        else:
            print("It's too deep, i can't dive :(")

    def get_cords(self):  # печать координатов
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self):  # функция атаки, если опасность >=5
        print("Sorry, i'm peaceful :)") if self._DEGREE_OF_DANGER < 5 else print("Be careful, i'm attacking you 0_0")

    def speak(self):  # крикнуть
        print(self.sound)

    # def about(self):
    #     print(f'class: {self.__class__}\n'
    #           f'speed: {self.speed}\n'
    #           f'coords: {self._cords}\n'
    #           f'DANGER: {self._DEGREE_OF_DANGER}\n'
    #           f'sound: {self.sound}\n'
    #           f'beak: {self.beak}')


class Bird(Animals):
    beak = True  # Наличие клюва

    def lay_eggs(self):  # откладывание яиц
        print(f"Here are(is) {randint(1, 4)} eggs for you")


class AquaticAnimal(Animals):
    _DEGREE_OF_DANGER = 3  # уровень опасности

    def dive_in(self, dz):  # погружение, dz всегда уменьшается
        self._cords[2] -= abs(dz) * self.speed / 2


class PoisonousAnimal(Animals):
    _DEGREE_OF_DANGER = 8  # уровень опасности


class Duckbill(PoisonousAnimal, Bird, AquaticAnimal, Animals):

    def __init__(self, speed):
        super().__init__(speed)  # сразу обращается к Animals.__init__
        self.sound = "Click-click-click"  # объект класса должен обадать атр. "Click-click"


if __name__ == '__main__':
    db = Duckbill(10)  # утконос, скорость 10

    print('Утконос лежит на солнышке')
    db.get_cords()
    print('Утконос предупреждающе пищит')
    db.speak()
    print('Утконос атакует!')
    db.attack()
    print('Утконос пытается скрыться')
    db.move(3, 4, 2)
    db.get_cords()
    print('Утконос пытается зарыться под корягу')
    db.move(20, 10, -30)
    print('Утконос ныряет в водоем')
    db.dive_in(6)
    db.get_cords()
    print('Утконос в безопасном месте оставляет кладку')
    db.lay_eggs()
