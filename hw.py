import math


class Figure:
    __sides = []  # список сторон целые числа
    __color = []  # список цветов в формате rgb
    filled = True # закрашенный
    var = 0

    def get_color(self):  # возвращает список RGB цветов
        return f'self.__color: {self.__color}'

    def __is_valid_color(self, *args):  # проверка корректности параметров цвет
       

    def set_color(self, *args):  # устанавливает цвета
        if self.__is_valid_color(args): # если цвета валидные
            self.__color.append(args)
        return f'self.__color: {self.__color}'



    def __is_valid_sides(self, *new_sides):  # проверяет ддлины сторон на вещественность и совпадения с кол-вом текуших сторон
        if len(new_sides) == self.sides_count:
            for i in new_sides:
                if str(i).isalpha(): # проверка на наличие не цифр
                    return False
                elif i != int(i): # проверк на наличие нецелых чисел
                    return False
                elif i < 1: # проверка на вещественное число
                    return False
            else:
                return True
        else:
            return False

    def get_sides(self):  # возвращать значение атрибута __sides
        return f'__sides: {self.__sides}'


    def set_sides(self, *new_sides):
        """
        должен принимать новые стороны, если их количество не равно sides_count,
        то не изменять, в противном случае - менять.
        :param new_sides:
        :return: sides
        """
        if self.__is_valid_sides(*new_sides):
            self.__sides = [] # перезаписываем список
            # print(self.__sides, Figure.__sides)
            [self.__sides.append(i) for i in new_sides]

    def __len__(self):  # периметр фигуры
        res = 0
        print(self.__sides)
        for i in self.__sides:
            res += i
        return res


class Circle(Figure):
    def __init__(self, side):
        self.sides_count = 1
        self.side = side
        self.__radius = self.side / 2 * math.pi

    def get_square(self, side):
        square = side ** 2 / math.pi * 4
        return square


class Triangle(Figure):
    def __init__(self):
        self.sides_count = 3

    def get_square(self, sides_count):
        pass

a = Triangle()
a.set_sides(1, 2, 4)
a.set_sides(1, 2, 3232)
a.set_color(255, 255, 255)

print(len(a))
print(a.get_color())
print(a.get_sides())