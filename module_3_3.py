# Самостоятельная работа по уроку "Распаковка позиционных параметров".

def  print_params(a = 1, b = 'строка', c = True):
    print( a, b, c )

print_params( b = 25 )  # 1 25 True
print_params( c = [1,2,3] ) # 1 строка [1, 2, 3]
print_params( )             # 1 строка True

# Создали список
values_list = ( 2, 'Nata', [1,2,3] )
# Создали словарь
values_dict = {'a':62.6 , 'b':'строка','c':True}

print_params(**values_dict) # 62.6 строка True
print_params(*values_list)  # 2 Nata [1, 2, 3]

# второй список
values_list_2 = [62.3, 'Строка' ]
print_params(*values_list_2, 44)  # 62.3 Строка 44
print_params(44, *values_list_2)  #  44 62.3 Строка