class Vehicle:
    __COLOR_VARIANTS = ['default', 'red', 'blue', 'white', 'black', 'grey', 'green', 'yellow', 'marin']

    def __init__(self, onwer='no onwer', model='no model', engine_power=100, color='default'):
        self.onwer = onwer
        self.__model = model
        self.__engine_power = int(engine_power)
        if str(color).lower() in Vehicle.__COLOR_VARIANTS:  # проверка на доступность цвета
            self.__color = color
        else:
            self.__color = Vehicle.__COLOR_VARIANTS[0]
            print(f'цвет: "{color}" нет в доступных, сolor = {Vehicle.__COLOR_VARIANTS[0]}\n'
                  f'Для просмотра доступных цветов воспользуйтесь методом get_colors_variants()')

    def get_model(self):
        return f'model: {self.__model}'

    def get_horsepower(self):
        return f'engin power: {self.__engine_power}'

    def get_color(self):
        return f'color: {self.__color}'

    def print_info(self):
        print(f"{self.get_model()} \n{self.get_horsepower()} \n{self.get_color()} \nВладелец: '{self.onwer}'\n")

    def set_color(self, new_color):  # перекраска автомобиля
        if new_color.lower() in Vehicle.__COLOR_VARIANTS:  # временно
            self.__color = new_color
        else:
            print(f'Нельзя менять цвет на "{new_color}"')

    def get_colors_variants(self):
        print(Vehicle.__COLOR_VARIANTS)


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5  # констанка, пишется Caps Lock


car1 = Vehicle('Fedor', 'Toyota', 300, 'Red')
car2 = Sedan('Dan', 'Lada', 115, 'blue')
car3 = Sedan('Yarik', 'Ford', 150, 'Orange')  # orange нет в __COLOR_VARIANTS

car1.print_info()
car2.print_info()
car3.print_info()
car3.get_colors_variants()  # показать доступные цвета
car3.set_color('Orange')  # цвет Ornge нет в списке __COLOR_VARIANTS
car3.set_color('Marin')
car3.print_info()  # color: Marin
car3.onwer = 'Sergey'  # смена владельца
car3.print_info()
print('__PASSENGERS_LIMIT =', Sedan._Sedan__PASSENGERS_LIMIT)
Sedan._Sedan__PASSENGERS_LIMIT += 1
print('__PASSENGERS_LIMIT =', Sedan._Sedan__PASSENGERS_LIMIT)
