# задание по теме "Множественное наследование"
# Задача "Мифическое наследование":

class Horse:
    """
    Horse - класс описывающий лошадь. Объект этого класса обладает следующими атрибутами:
    x_distance = 0 - пройденный путь.
    sound = 'Frrr' - звук, который издаёт лошадь.
    """
    def __init__(self):
        self.sound = 'Frrr'
        self.x_distance = 0
        super().__init__()

    def run(self, dx):
        """ run(self, dx), где dx - изменение дистанции, увеличивает x_distance на dx """
        self.x_distance = self.x_distance + dx
        return self.x_distance

class Eagle:
    """
    Eagle - класс описывающий орла. Объект этого класса обладает следующими атрибутами:
    y_distance = 0 - высота полёта
    sound = 'I train, eat, sleep, and repeat' - звук, который издаёт орёл
    """
    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep and repeat'

    def fly(self, dy):
        self.y_distance = self.y_distance + dy
        return self.y_distance



class Pegasus(Horse,Eagle):
    """
    Pegasus - класс описывающий пегаса. Наследуется от Horse и Eagle.
    """
    def __init__(self):
        super().__init__( )

    def __repr__(self):
        return f'Пегас'

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)
        return

    def get_pos(self):
        return f'  Координаты:{(self.x_distance, self.y_distance)}'

    def voice(self):
        print(f' {self} кричит : "{self.sound}"')

moli = Pegasus()

print(moli.get_pos())
moli.move(10, 15)
print(moli.get_pos())
moli.move(-5, 20)
print(moli.get_pos())

moli.voice()