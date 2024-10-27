# Доступ к свойствам родителя. Переопределение свойств.


class Vehicle:
    """
    Класс Vehicle - это любой транспорт
    Атрибут owner(str) - владелец транспорта. (владелец может меняться)
    Атрибут __model(str) - модель (марка) транспорта. (мы не можем менять название модели)
    Атрибут __engine_power(int) - мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
    Атрибут __color(str) - название цвета. (мы не можем менять цвет автомобиля своими руками)
    Атрибут класса __COLOR_VARIANTS, в который записан список допустимых цветов для окрашивания
    """

    def __init__(self,owner,__model,__engine_power,__color):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color
        self.__COLOR_VARIANTS = ['синий', 'красный', 'зеленый', 'черный', 'белый']


    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print("Информация об автотранспорте.")
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        """  Метод set_color - принимает аргумент new_color(str)
           если он есть в списке __COLOR_VARIANTS, меняет цвет __color на new_color
           в противном случае выводит на экран надпись: 'Нельзя сменить цвет'"""
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color.lower()
        else:
            print(f'Нельзя сменить цвет на {new_color.lower()}')

class Sedan(Vehicle):
    """ Sedan(седан) - наследник класса Vehicle """
    __PASSENGERS_LIMIT = 5



vehicle1 = Sedan('Федот', 'Toyota Mark II', 500, 'синий')

# Изначальные свойства
vehicle1.print_info()
print("---------------")

# Меняем свойства (в т.ч. вызывая методы)
print('Меняем информацию')
vehicle1.set_color('Розовый')
vehicle1.set_color('ЧЕРНЫЙ')
vehicle1.owner = 'Васёк'
print("______________")
print(f'\nПроверяем что изменилось\n')
vehicle1.print_info()

