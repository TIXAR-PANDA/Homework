# Зачем нужно наследование
#Задача "Съедобное, несъедобное"

class  Animal:
    """
    Класс Animal - животное. Атрибуты: alive = True(живой) и fed = False(накормленный),
    name - индивидуальное название каждого животного.
    """
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

    def __repr__(self):
        return f'{self.name}'

    def eat(self, food):
        """ Если животному дать съедобное растение, то животное насытится,
         если не съедобное - погибнет.
        """
        if food.edible is False:
            print(f'{self} не стал есть {food} и умер от голода')
            self.alive = False
        else:
            print(f'{self} cъел {food} и насытился')
            self.fed = True
            return

class  Mammal(Animal) :
    """Класс  Mammal - млекопитающее."""


class Predator(Animal):
    """ Класс Predator - хищник. """
    



class Plant:
    """
    Класс Plant - растение. Атрибуты: edible - съедобность,
    name - индивидуальное название каждого растения
    """
    def __init__(self, name):
        self.name = name


    def __repr__(self):
        return f'{self.name}'


class Flower(Plant):
    """Класс Flower - Цветок. edible = False (несъедобный)"""
    edible = False

class Fruit(Plant):
    """ Класс Fruit - фрукты. edible = True( съедобный) """
    edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(f'Животные:{a1}, {a2}')
print(f'Растения: {p1}, {p2}')

print(f' {a1} живой? >>> {a1.alive}')
print(f' {a2} не голодный? >>> {a2.fed}')
print(f' {p1} съедобный? >>> {p1.edible}')
print(f' {p2} съедобный? >>> {p2.edible}')
a1.eat(p1)
a2.eat(p2)
print(f' {a1} живой? >>> {a1.alive}')
print(f' {a2} не голодный? >>> {a2.fed}')
