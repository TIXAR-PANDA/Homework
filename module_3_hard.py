# Задание "Раз, два, три, четыре, пять .... Это не всё?":


def calculate_structure_sum(structure_):
    n = len(structure_)
    ss = 0
    for i in range(0, n):
       if isinstance (structure_[i],dict):
            '''идем к словарям----'''
            keys = list(structure_[i].keys())
            values_ = list(structure_[i].values())
            structure_dict = [keys,values_]
            ss1 = calculate_structure_sum(structure_dict)
            ss = ss + ss1
           
        if isinstance(structure_[i], (list,  tuple)):
            '''идем к спискам , к кортежу -----'''
            ss1 = calculate_structure_sum(structure_[i])
            ss = ss +  ss1
            
        if isinstance(structure_[i], int):
           '''идем к числам'''
            ss = ss + int(structure_[i])
            print('ss = ', ss)

        if isinstance(structure_[i], str):
            '''идем к строкам----'''
            ss = ss + len(structure_[i])
            print('ss = ', ss)

        if isinstance(structure_[i], set ):
            '''идем к множеству----'''
            structure_1 = list (structure_[i])
            ss1 = calculate_structure_sum(structure_1)
            ss = ss + ss1

    return ss







data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

print( calculate_structure_sum(data_structure) )

