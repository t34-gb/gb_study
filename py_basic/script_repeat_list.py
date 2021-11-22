from sys import argv, exit
from itertools import cycle

try:
    script_name, my_list, finish = argv
    print("Имя скрипта: ", script_name)
    print("Элементы списока для повтора: ", my_list)
    print("Количество итераций цикла: ", finish)
except ValueError:
    print('Error: Неверное количество параметров!')
    exit()
else:
    try:
        finish = int(finish)
        c = 1
        for el in cycle(my_list):
            if c > finish:
                break
            print(el)
            c += 1
    except ValueError as error:
        print('Error: ', error)
