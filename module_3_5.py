# Самостоятельная работа по уроку "Рекурсия"

def get_multiplied_digits(number):
    str_number = str (number)
    first = int(str_number[0])
    if not len(str_number[1:]) > 1:
        return first
    else:
        return first * get_multiplied_digits(int(str_number[1:]))




pp = 40203
result = get_multiplied_digits(pp)
print(f'Число: {pp} , произведение цифр этого числа: {result}')