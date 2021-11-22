"""Выполнение задания к уроку № 4. Полезные инструменты."""
from functools import reduce


def mul_func(num1, num2):
    return num1 * num2


def fact(n):
    """Функция реализует генератор факториала любого числа

    :param n: любое целое положительное число
    :return: объект-генератор факториала числа
    """
    try:
        n = abs(int(n))
        for i in [j for j in range(1, n + 1)]:
            k = 1
            for el in range(1, i + 1):
                k *= el
            yield k
    except ValueError as error:
        print('Error: ', error)


while True:
    task = input('Enter the task number (1-7): ')
    if task == '1':
        print(f'Задание № {task}:')
        print('Для проверки скрипта в командной строке набрать: python script_wages.py 10 20 30')
        print('=' * 50)

    elif task == '2':
        print(f'Задание № {task}:')
        my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
        new_list = [i for i in my_list[1:] if my_list[my_list.index(i)] > my_list[my_list.index(i) - 1]]
        print(f"Исходный список: {my_list}")
        print(
            f"Новый список, состоящий из элементов исходного списка, "
            f"значения которых больше предыдущего элемента:\n{new_list}")
        print('=' * 50)

    elif task == '3':
        print(f'Задание № {task}:')
        new_list = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]
        print(f"Список из чисел в пределах от 20 до 240, кратных 20 или 21:\n{new_list}")
        print('=' * 50)

    elif task == '4':
        print(f'Задание № {task}:')
        my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
        new_list = [el for el in my_list if my_list.count(el) == 1]
        print(f"Исходный список: {my_list}")
        print(f"Новый список, состоящий из элементов исходного списка, не имеющих повторений:\n{new_list}")
        print('=' * 50)

    elif task == '5':
        print(f'Задание № {task}:')
        mul_list = reduce(mul_func, [el for el in range(100, 1001) if el % 2 == 0])
        print(f"Произведение элементов списока из чётных чисел в пределах от 100 до 1000:\n{mul_list}")
        print('=' * 50)

    elif task == '6':
        print(f'Задание № {task}:')
        print('Для проверки скрипта в командной строке набрать: python script_gen_int.py 10 20')
        print('Для проверки скрипта в командной строке набрать: python script_repeat_list.py abc 10')
        print('=' * 50)

    elif task == '7':
        print(f'Задание № {task}:')
        num = input('Для расчёта факториала введите целое число: ')
        c = 1
        for el in fact(num):
            print(f'{c}! = {el}')
            c += 1
        print('=' * 50)

    else:
        print('Программа завершена!')
        break
