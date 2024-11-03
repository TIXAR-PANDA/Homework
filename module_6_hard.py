# Дополнительное практическое задание по модулю: "Наследование классов."
# Задание "Они все так похожи"


import math

class Figure:
    """
    Класс Figure(родительский)
    Атрибуты (инкапсулирование):
    __sides(список сторон (целые числа)),
    __color(список цветов в формате RGB)
    Атрибуты(публичные): filled(закрашенный, bool)
    """
    sides_count = 0

    def __init__(self, color, sides, filled=False):
        self.__sides = sides if self.__is_valid_sides(sides) else [1] * self.sides_count
        self.__color = color if len(color) == 3 and self.__is_valid_color(*color) else [255, 255, 255]
        self.filled = filled

    def get_color(self):
        """
        Метод get_color, возвращает список RGB цветов.
        """
        return self.__color

    def set_color(self, r, g, b):
        """
        Метод set_color принимает параметры r, g, b - числа
        и изменяет атрибут __color на соответствующие значения,
        предварительно проверив их на корректность.
        Если введены некорректные данные, то цвет остаётся прежним.
        """
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
            print(f'Цвет изменился')
        else:
            print(f'Некорректно заданы цвета')


    def __is_valid_color(self, r, g, b):
        """
        Метод __is_valid_color - служебный,
        проверяет корректность переданных значений перед установкой нового цвета.
        Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
        return: True или False
        """
        return all(isinstance(c, int) and 0 <= c <= 255 for c in [r, g, b])


    def __is_valid_sides(self, sides):
        """
        Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон,
        возвращает True если все стороны целые положительные числа и
        кол-во новых сторон совпадает с текущим,
        возвращает False - во всех остальных случаях.
        :param sides:

        """
        return all(isinstance(side, int) and side > 0 for side in sides) and len(sides) == self.sides_count

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        """
        Метод set_sides(self, *new_sides) должен принимать новые стороны,
        если их количество не равно sides_count, то не изменять,
        в противном случае - менять.
        :param new_sides
        :return:
        """
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)
            print(f'Изменились размеры: {self.__sides}')
        else:
            print(f'-- Неправильно указано количество сторон\n'
                  f'   всего сторон: {self.sides_count}\n'
                  f'   дано: {len(new_sides)} -----')

    def __len__(self):
        return sum(self.__sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color=[255, 255, 255], circumference=0, filled=False):
        super().__init__(color=color, sides=[circumference], filled=filled)
        self.__radius = circumference / (2 * math.pi)

    def get_radius(self):
        print(f'Радиус окружности {self.__radius}')

    def get_square(self):
        print (f'Площадь круга = {math.pi * (self.__radius ** 2)}')


class Triangle(Figure):
    """
    класс Triangle - треугольник.
    """
    sides_count = 3

    def __init__(self,color, *sides):
        super().__init__(color, sides)

    def get_square(self):
        """
        Метод get_square возвращает площадь треугольника по формуле Герона.
        """
        s = sum(self.get_sides()) / 2
        square_ = math.sqrt(s * (s - self.get_sides()[0]) * (s - self.get_sides()[1])
                         * (s - self.get_sides()[2]))
        return f'площадь треугольника(со сторонами {self.get_sides()} = {square_}'


class Cube(Figure):
    """
    Класс Куб. Все атрибуты и методы класса Figure.
     __sides список из 12 одинаковы сторон (передаётся 1 сторона)
    """
    sides_count = 12

    def __init__(self, color, sides, filled=False):
        super().__init__(color=color, sides=[sides] * 12, filled=filled)

    def get_volume(self):
        """
        Возвращает объем куба
        """
        volume_= self.get_sides()[0] ** 3
        return f'объем куба = {volume_}'


# Код для проверки:
triangle = Triangle((200, 200, 100), 10, 6, 13)
triangle1 = Triangle((20, 150, 100), 4, 6, 8)
circle1 = Circle((200, 200, 100), 17) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
cube2 = Cube((212, 49, 130), 12)
print(f'Длина окружности: {circle1.get_sides()[0]}')
circle1.get_radius()
circle1.get_square()
print(f'Изменить длину окружности: circle1.set_sides(21) ')
circle1.set_sides(21)
print(f'Изменить длину окружности: circle1.set_sides(2,4,5) ')
circle1.set_sides(2,4,5)
print ('Проверка на изменение цветов')
print(f'Было {circle1.get_color()}')
print('Хотим изменить: circle1.set_color(55, 66, 77)')
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
print(f'Было {cube1.get_color()}')
print('Хотим изменить: cube1.set_color(300, 70, 15)')
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

print('Проверка на изменение сторон: cube1.set_sides(5, 3, 12, 4, 5)')
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
circle1.set_sides(15) # Изменится
cube1.get_sides()
circle1.get_sides()

print('Проверка периметра (круга), это и есть длина:len(circle1)')
print(f'периметр круга = {len(circle1)}')
print(f'Треугольник: {triangle.get_sides()}')
print(f'периметр треугольника = {len(triangle)}')
print('Проверка объёма (куба):')
print(cube1.get_sides())
print(cube1.get_volume())
print(cube2.get_sides())
print(cube2.get_volume())
print('изменить куб: cube2.set_sides(2)')
cube2.set_sides(2)

print('Проверка на изменение сторон треугольника: triangle1.set_sides(2)')
triangle1.set_sides(2)
print(triangle1.get_square())
print('Проверка на изменение сторон треугольника: triangle1.set_sides(5, 3, 12, 4, 5)')
triangle1.set_sides(5, 3, 12, 4, 5)
triangle2 = Triangle((200, 200, 100), 4, 6, 3)
triangle2.get_sides()
# Площадь треугольника
print(triangle2.get_square())



