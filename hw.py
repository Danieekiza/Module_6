import math


class Figure:
    __sides = []  # список сторон целые числа
    __color = []  # список цветов в формате rgb
    filled = False  # закрашенный

    def get_color(self):  # возвращает список RGB цветов
        return f'color: {self.__color}'

    def __is_valid_color(self, *colors):  # проверка корректности параметров цвет
            for i in colors:
                if str(i).isalpha():  # проверка на наличие не цифр
                    return False
                elif i != int(i):  # проверк на наличие нецелых чисел
                    return False
                elif i < 0 or i > 255:  # проверка на вещественное число
                    return False
            else:
                return True

    def set_color(self, *colors):  # устанавливает цвета
        if self.__is_valid_color(*colors):  # если цвета валидные
            self.__color = list(colors)
            self.filled = True  # теперь объект закрашенный
        # return f'{self}: {self.__color}'

    def __is_valid_sides(self, *new_sides):  # проверяет ддлины сторон на вещественность и
        # совпадения с кол-вом текуших сторон
        if len(new_sides) == self.sides_count:
            for i in new_sides:
                if str(i).isalpha():  # проверка на наличие не цифр
                    return False
                elif i != int(i):  # проверк на наличие нецелых чисел
                    return False
                elif i < 1:  # проверка на вещественное число
                    return False
            else:
                return True
        else:
            return False

    def get_sides(self):  # возвращать значение атрибута __sides
        return self.__sides

    def set_sides(self, *new_sides):
        """
        должен принимать новые стороны, если их количество не равно sides_count,
        то не изменять, в противном случае - менять.
        :param new_sides:
        :return: sides
        """
        if self.__is_valid_sides(*new_sides):
            self.__sides = []  # перезаписываем список
            # print(self.__sides, Figure.__sides)
            [self.__sides.append(i) for i in new_sides]

    def __len__(self):  # периметр фигуры
        res = 0
        for i in self.__sides:
            res += i
        return res



class Circle(Figure):
    def __init__(self):
        self.sides_count = 1


    def get_square(self):
        self.__radius = len(self) / 2 * math.pi
        square = self.__radius ** 2 / math.pi * 4
        return round(square, 4)


class Triangle(Figure):
    def __init__(self):
        self.sides_count = 3


    def get_square(self):
            if not self.get_sides():  # проверка на наличие заданных сторон
                print('Сначало задайте значения сторон методом get_sides()')
            else:
                a, b, c = self.get_sides() # присвоим 3м переменным заданные стороны
                if (a + b) > c and (b + c) > a and (a + c) > b: # если из сторон можно сложить теугльник
                    p = self.__len__()/2 # полупериметр
                    square = math.sqrt(p*(p-a)*(p-b)*(p-c))  # плозадь по формуле герона
                    return round(square, 4)
                else:
                    print('Из заданных вами сторон невозможно сложить треугольник.\n'
                          'Удаите эту ошибку математики ')

a = Triangle()
# a.set_sides(1, 2, 4)
print(a.get_square())
a.set_sides(2, 2, 3)
a.set_sides(2.1, 2, 3)
a.set_color(255, 255, 255)
print(a.get_square())
print(len(a))
print(a.get_color())
print(a.get_sides())

b = Circle()
b.set_sides(4)
print(b.get_sides())
# print(b.side)
print(len(b))
print(b.get_square())
