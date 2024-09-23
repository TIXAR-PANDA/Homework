# Домашняя работа по уроку:"Цикл for. Элементы списка. Полезные функции в цик

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i < 2:
        continue
    for j in primes:
        if i % j == 0:
            not_primes.append(i)
            break
    else:
            primes.append(i)
print(f'Простые числа: {primes} \nСоставные числа: {not_primes}')