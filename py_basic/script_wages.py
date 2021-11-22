import sys
from sys import argv

try:
    script_name, output, rate, bonus = argv
    print("Имя скрипта: ", script_name)
    print("Выработка в часах: ", output)
    print("Ставка в час: ", rate)
    print("Премия: ", bonus)
except ValueError:
    print('Error: Неверное количество параметров!')
    sys.exit()


def wages():
    try:
        my_list = list(map(float, (output, rate, bonus)))
        print('Заработная плата сотрудника: ', my_list[0] * my_list[1] + my_list[2])
    except ValueError as error:
        print('Error: ', error)


wages()
