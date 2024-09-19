print('Работа со словарями')

my_dict = {'Johnny': 1998, 'Khendrik': 1999, 'Steve': 2007}
print('Dict:', my_dict)
print('Existing value;', my_dict.get('Khendrik'))
print('Not existing value:', my_dict.get('Anna'))
# my_dict['Serge']=2005
# my_dict['Charles']=2000
my_dict.update({'Serge': 2005, 'Charles': 2000})  # Добавляем несколько заначений
print('Deleted value:', my_dict.pop('Johnny'))
print(my_dict)

print('Работа  с множествами')

my_set = {'Множество:', 1, 2.2, 23, 1, 2, 1, 3}
print('Set: ', my_set)
my_set.add("Nata")  # Добавляем элемент
my_set.add((7, 4))
my_set.discard('Множество:')  # Удалили элемент
print('Modified set:', my_set)