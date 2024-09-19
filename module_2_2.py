# Условная конструкция. Операторы if, elif, else."

first = int(input("первое число:"))
second = int(input("второе число:"))
third = int(input("третье число:"))
if first == second and second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
# elif first != second and second != third and first != third:
# print(0)
else:
    print(0)
