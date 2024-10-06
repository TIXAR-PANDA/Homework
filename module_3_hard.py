# Задание "Раз, два, три, четыре, пять .... Это не всё?":


def calculate_structure_sum(structure_):
    print(structure_)
    n = len(structure_)
    ss = 0
    for i in range(0, n):
        print ('    ', i )
        print(structure_[i])
        print(type(structure_[i]))

        if isinstance (structure_[i],dict):
            print ('идем к словарям----')
            keys = list(structure_[i].keys())
            values_ = list(structure_[i].values())
            structure_dict = [keys,values_]
            print(' ------------' ,structure_dict )
            ss1 = calculate_structure_sum(structure_dict)
            ss = ss + ss1
            print('ss = ', ss)
        if isinstance(structure_[i], list):
            print('идем к спискам-----')
            ss1 = calculate_structure_sum(structure_[i])
            ss = ss +  ss1
            print ('ss = ', ss)
        if isinstance(structure_[i], int):
            print('идем к числам')
            ss = ss + int(structure_[i])
            print('ss = ', ss)

        if isinstance(structure_[i], str):
            print('идем к строкам')
            ss = ss + len(structure_[i])
            print('ss = ', ss)

        if isinstance(structure_[i], tuple):
            print('идем к кортежу')
            ss1 = calculate_structure_sum(structure_[i])
            ss = ss + ss1

            print('ss = ', ss)
        if isinstance(structure_[i], set ):
            print('идем к множеству')
            structure_1 = list (structure_[i])
            ss1 = calculate_structure_sum(structure_1)
            ss = ss + ss1
    print ('rez = ', ss)
    return ss







data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

calculate_structure_sum(data_structure)

