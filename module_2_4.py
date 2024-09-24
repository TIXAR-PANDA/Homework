# Домашняя работа по уроку:"Цикл for. Элементы списка. Полезные функции в цикле

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in numbers:
    if i < 2:
        continue
    for j in primes:
        if i % j == 0:
            is_prime = False
            break
    else:
        is_prime = True
    if not (is_prime):
        not_primes.append(i)
    else:
        primes.append(i)
print(f'Простые числа: {primes} \nСоставные числа: {not_primes}')

