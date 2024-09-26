# Домашняя работа по уроку "Пространство имён"


def count_calls():
    global calls
    calls += 1


def string_info(string):
    string = str(string)
    report = (len(string), string.upper(), string.lower())
    count_calls()
    return report


def is_contains(string, list_to_search):
    global report
    string = str(string).lower()
    list_to_search = list(list_to_search)
    count_calls()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:
            report = True
            break
        else:
            report = False
            continue
    #return report
    if report == True:
        print ( 'Строка: ','"', string , '"' , 'уже существует' )
    else: print (  string , '-', 'такой строки нет' )


calls = 0
print(string_info('Анатольевна'))
print(string_info('тОваРИЩ'))
is_contains('ВАЛЕНТИН', ['Иванов', 'иван', 'вАлентинович'])
is_contains('ВАЛЕНТИН', ['валентин', 'сергеевич', 'Петров'])
is_contains('Bdfy', ['валентин', 'сергеевич', 'Петров'])


print ('Обращений к функциям:', calls )

