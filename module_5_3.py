# Атрибуты и методы объекта
# >>>  Специальные методы классов

def checking_the_class(other):
    if not isinstance ( other, (int, House)):
        raise ArithmeticError ( "Второй операнд должен быть типом int или объектом House")


class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('"Такого этажа не существует"')
        else:
            for new_floor in range(new_floor+1):
                if new_floor < 1:
                    continue
                print(new_floor)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name} , кол-во этажей: {self.number_of_floors}'

    # >>> Перегрузка операторов

    def __eq__(self, other):
        checking_the_class(other)
        other = other if isinstance(other, int) else other.number_of_floors
        return self.number_of_floors == other


    def __add__(self, other):
        checking_the_class(other)
        self.number_of_floors = self.number_of_floors + other
        return self

    def __sub__(self, other):
        checking_the_class(other)
        other = other if isinstance(other, int) else other.number_of_floors
        self.number_of_floors = self.number_of_floors  - other
        return self

    def __iadd__(self, other):
        checking_the_class(other)
        other = other if isinstance(other, int) else other.number_of_floors
        self.number_of_floors += other
        return self

    def __radd__(self, other):
        checking_the_class(other)
        other = other if isinstance(other, int) else other.number_of_floors
        self.number_of_floors = other + self.number_of_floors
        return self

    def __lt__(self, other):
        checking_the_class(other)
        other = other if isinstance(other, int) else other.number_of_floors
        return self.number_of_floors < other

    def __gt__(self, other):
        checking_the_class(other)
        other = other if isinstance(other, int) else other.number_of_floors
        return self.number_of_floors > other

    def __ge__(self, other):
        checking_the_class(other)
        other = other if isinstance(other, int) else other.number_of_floors
        return self.number_of_floors >= other

    def __le__(self, other):
        checking_the_class(other)
        other = other if isinstance(other, int) else other.number_of_floors
        return self.number_of_floors <= other


    def __ne__(self, other):
        checking_the_class(other)
        other = other if isinstance(other, int) else other.number_of_floors
        return self.number_of_floors != other









h1 = House('ЖК "Горский"', 18)
h2 = House('Домик в деревне', 2)
#h1.go_to(4)
#h2.go_to(6)


h3 = House('ЖК Эльбрус', 10)
h4 = House('ЖК Акация', 20)

#print(len (h3))
#print(len (h4))

print (" h3 = ", h3)
print (" h2 = ", h2)
print (" h1= ", h1)


print('h1 == h2 :', h1 == h2 ) # __eq__

h1 = h1 + 10   # __add__
print( 'h1 + 10 = ', h1)
h1 = h1 - 5   # __add__
print( 'h1 - 5 = ', h1)


h2 += 10   # __iadd__
print('h1 += 10  ', h2)

h3 = 10 + h3 # __radd__
print(' 10 + h3 =', h3)
print (" h4 = ", h4)

print('h3 > h4 :' , h3 > h4) # __gt__
print('h3 >= h4 :', h3 >= h4) # __ge__
print('h3 < h4 :', h3 < h4) # __lt__
print('h3 <= h4 :', h3 <= h4) # __le__
print('h3 != h4 :', h3 != h4) # __ne__
print('h1 != h2 :', h1 != h2) # __ne__
print('h1 != 10 :', h1 != 10 )
print('h3 < 6 :', h3 < 6)