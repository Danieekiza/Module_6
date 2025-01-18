import math


class Figure:
    __sides = []  # список сторон целые числа
    __color = []  # список цветов в формате rgb
    filled = False  # закрашенный

    def chec_args(self, *args, sides_count=1):
        if type(args[0]) is tuple:  # проверка на наличие первого арг. типа tuple
            if len(args[0]) == 3:
                self.set_color(*args[0])
            else:
                print(f'Неверные аргументы переданы в параметры цвета объекту класса {self.__class__}')
        else:
            print(f'Неверные аргументы переданы в параметры цвета объекту класса {self.__class__} \n'
                  f'Тип первого аргумента - не tuple ')
            exit()
        if self.__class__ == Cub: # для класса куб отдлеьная проверка
            self.set_args_cub(*args[1:])
        else:
            if len(args[1:]) == sides_count:
                self.set_sides(*args[1:])
            else:
                self.set_sides(1 * sides_count)
                print(f'Неверные аргументы переданы в параметры строн объекту класса {self.__class__}\n'
                      f'Заданы стороны поумолчанию = 1')

    def get_color(self):  # возвращает список RGB цветов
        return self.__color

    def set_args_cub(self, *args): # проверяем,что переданные стороны куба равны
        _list = []
        for i in range(len(args) - 1):
            if args[i] != args[i + 1] or args[i] < 1:
                for i in range(12): _list.append(1)
                self.__sides = _list # если не равны, то по умолчанию стороны = 1
                _list = []
                break
        else:
            a = 1 if  args[0] < 1 else args[0] # проверка значение на валидность
            for i in range(12): _list.append(a)
            self.__sides = _list # передаем заданную сторону 12 раз
            _list = []


    def __is_valid_color(self, *colors):  # проверка корректности параметров цвет
        if len(colors) == 3:
            for i in colors:
                if str(i).isalpha():  # проверка на наличие не цифр
                    return False
                elif i != int(i):  # проверк на наличие нецелых чисел
                    return False
                elif i < 0 or i > 255:  # проверка на вещественное число
                    return False
            else:
                return True
        else:
            return False

    def set_color(self, *colors):  # устанавливает цвета
        if self.__is_valid_color(*colors):  # если цвета валидные
            self.__color = list(colors)
            self.filled = True  # теперь объект закрашенный

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

    def set_sides(self, *new_sides): # метод определяет размер сторон фигуры
        if self.__class__ == Cub: # для класса куб отдлеьная проверка
            self.set_args_cub(*new_sides)
        elif self.__is_valid_sides(*new_sides):
            self.__sides = []  # перезаписываем список
            [self.__sides.append(i) for i in new_sides]
        else:
            self.__sides = [1] * self.sides_count

    def __len__(self):  # периметр фигуры
        res = 0
        for i in self.__sides:
            res += i
        return res


class Circle(Figure):
    def __init__(self, *args):
        self.sides_count = 1
        self.chec_args(*args, sides_count=self.sides_count)

    def get_square(self):
        self.__radius = len(self) / 2 * math.pi
        square = self.__radius ** 2 / math.pi * 4
        return round(square, 4)


class Triangle(Figure):
    def __init__(self, *args):
        self.sides_count = 3
        self.chec_args(*args, sides_count=self.sides_count)

    def get_square(self):
        if not self.get_sides():  # проверка на наличие заданных сторон
            print('Сначало задайте значения сторон методом get_sides()')
        else:
            a, b, c = self.get_sides()  # присвоим 3м переменным заданные стороны
            if (a + b) > c and (b + c) > a and (a + c) > b:  # если из сторон можно сложить теугльник
                p = self.__len__() / 2  # полупериметр
                square = math.sqrt(p * (p - a) * (p - b) * (p - c))  # плозадь по формуле герона
                return round(square, 4)
            else:
                print('Из заданных вами сторон невозможно сложить треугольник.\n'
                      'Удаите эту ошибку математики ')

class Cub(Figure): # класс Куб
    def __init__(self, *args):
        self.sides_count = 12
        self.chec_args(*args, sides_count=self.sides_count)

    def get_volume(self): # метод объем куба
        return self.get_sides()[0] ** 3


a = Circle((1, 2, 3), 2, 3)
print('a.color:', a.get_color())
print('a.filled:', a.filled)
print('a.sides:', a.get_sides())
print('a.get_square:', a.get_square())
a.set_sides(4)
print('a.sides:',a.get_sides())
print('len(a):', len(a))
print('a.get_square:', a.get_square())
print()

b = Triangle((1, 2, 3), 2, 3, 2)
print('b.color:', b.get_color())
print('b.filled:', b.filled)
print('b.sides:', b.get_sides())
print('b.get_square:', b.get_square())
b.set_sides(4)
print('b.sides:', b.get_sides())
print('len(b):', len(b))
print('b.get_square:', b.get_square())
print()

c = Cub((1, 1, 1), 4, 4, 4)
print('c.sides: ', c.get_sides())
print('c.color: ', c.get_color())
print('c.get_volume:', c.get_volume())
c.set_sides(3, 3)
c.set_color(255, 255, 255)
print('c.sides: ', c.get_sides())
print('c.color: ', c.get_color())
print('c.get_volume:', c.get_volume())
