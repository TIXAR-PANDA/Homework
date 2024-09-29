
# Задача "Однокоренные"

def single_root_words( root_word, *other_words):
    same_words = []
    word = str (root_word).lower()
    print( 'Список слов: ', other_words)
    n = int(len(other_words))
    i = 0
    for i in range(0, n):
        word1 = other_words[ i ].lower()
        if word in word1 or word1 in word:
            same_words.append ( other_words[ i ] )
    print(' Наше слово: ', root_word )
    print( ' Результат: ', same_words)


single_root_words('rich', 'riChest', 'orichalcum', 'cheers', 'riches')
print( )
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print( )
single_root_words('Роза', 'роса', 'рОЗарий', 'купороза', 'ОЗА')
