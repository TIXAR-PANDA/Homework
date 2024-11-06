# Оператор "with".
# Задача "Найдёт везде"

import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        """
        Подготовительный метод.
        Перебирает названия файлов и открывает каждый из них.
        Для каждого файла считывает единые строки, переводя их в нижний регистр.
        Избавляемся от пунктуации [',', '.', '=', '!', '?', ';', ':', '-'] в строке.
        Разбиваем строку на элементы списка методом split().
        :return: all_words: словарь, ключ - название файла, значение - список из слов этого файла.
        """
        all_words = { }
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                text = text.translate(str.maketrans('', '', string.punctuation.replace('-', '')))
                words = text.split()
                all_words[file_name] = words
        return all_words

    def find(self, word_d):
        """
        :param word_d: искомое слово
        :return:results - словарь, где ключ - название файла, значение - позиция первого
         такого слова в списке слов этого файла.
        """
        results = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            if word_d.lower() in words:
                results[file_name] = words.index(word_d.lower()) + 1  # Позиция с 1
        return results

    def count(self, word_d):
        """
        :param word_d:искомое слово.
        :return:Словарь, где ключ - название файла,
        значение - количество слова word в списке слов этого файла.
        """
        results = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            count = words.count(word_d.lower())
            if count > 0:
                results[file_name] = count
        return results

ww = WordsFinder('test.txt', 'test1.txt')
print(ww.get_all_words())
print('Слово - TEXT')
print(ww.find('TEXT'))
print(ww.count('TEXT'))
print('---Новая проверка---')
wf = WordsFinder('Walt_Whitman_O Captain!_My_Captain!.txt',
                 'Rudyard_Kipling_If.txt',
                 'Mother_Goose_Mondays_Child.txt'
                 )
print('Какое по счету слово "the"')
print(wf.find('the'))
print('Сколько раз в стихах встречается слово "the"')
print(wf.count('the'))
"""
ОТВЕТ для проверки:
{'Walt Whitman - O Captain! My Captain!.txt': 14, 'Rudyard Kipling - If.txt': 109, 'Mother Goose - Monday’s Child.txt': 41}
{'Walt Whitman - O Captain! My Captain!.txt': 18, 'Rudyard Kipling - If.txt': 7, 'Mother Goose - Monday’s Child.txt': 2}
"""