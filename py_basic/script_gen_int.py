from sys import argv, exit
from itertools import count

try:
    script_name, start, finish = argv
    print("Имя скрипта: ", script_name)
    print("Стартовое число списка: ", start)
    print("Конечное число списка: ", finish)
except ValueError:
    print('Error: Неверное количество параметров!')
    exit()
else:
    try:
        start, finish = int(start), int(finish)
        for el in count(start):
            if el > finish:
                break
            else:
                print(el)
    except ValueError as error:
        print('Error: ', error)
