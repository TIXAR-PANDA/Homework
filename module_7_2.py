
import io
from pprint import pprint
def custom_write(file_name, strings):
    """
    Записывает в файл file_name все строки из списка strings, каждая на новой строке.
    :param file_name: название файла для записи
    :param strings: список строк для записи
    :return: strings_positions - словарь,
    где ключом будет кортеж (<номер строки>, <байт начала строки>),
    а значением - записываемая строка.
    """
    strings_positions = {}
    with open(file_name, 'w', encoding='utf-8') as file:
        for i, str_ in enumerate(strings, start=1):
            n = file.tell()
            file.write(str_ + '\n')
            strings_positions[(i, n)] = str_
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for i in result.items():
  print(i)
