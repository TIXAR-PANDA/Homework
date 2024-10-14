
def test_function():
    print ('----Работает test_function')

    def inner_function():
        print ("--------Я в области видимости функции test_function")

    print ('----Вызываем inner_function')
    inner_function()

print('Работает основная программа ----')
#inner_function() >>> NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
                      #Ошибка: имя 'inner_function' не определено. Вы имели в виду 'test_function'?
test_function()
