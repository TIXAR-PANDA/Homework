# Дополнительное практическое задание по второму модулю*
def pass_word():
    list_value = []  # Список для  пар значений
    list_password = []  # Список для хранения значиний после объеденения списков внутри list_value
    n = int(input('Введите число от 3 до 20: '))
    if n < 3 or n > 20:
        print('Введено неверное число.')
        print()
        pass_word()

    else:
        for i in range(1, n):
            for j in range(1, n):
                if all([n % (i + j) == 0,
                        i != j,
                        [j, i] not in list_value]):
                    list_value.append([i, j])  # подобрали уникальные значения пар

        for i in list_value:
            list_password.extend(i)  # распаковали внутренние списки и объеденили их в один список
        password = ''.join(str(x) for x in list_password)  # перебрали значения из списка, присвоили их переменой
        print('пароль : ', password)


pass_word()
