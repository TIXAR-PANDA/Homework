# Домашняя работа по уроку "Стиль кода часть II. Цикл While."

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
print ('Список:', my_list)
n = 0
print (" Положительные числа ")
while n < len(my_list):
    pn = my_list[n]
    n = n + 1
    if pn == 0:
        continue
    elif pn < 0:
        print('Встретилось отрицательное число')
        break
    elif n == len(my_list):
        print('   ', pn)
        print('Список закончился')
    else:
        print('   ', pn)
