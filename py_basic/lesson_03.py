"""Выполнение задания к уроку № 3. Функции."""


def division(a, b):
    """Задание № 1: Функция, выполняющая деление 2-х позиционных аргументов.

    Числа запрашиваются у пользователя.
    Предусмотрена обработка ситуации деления на ноль.

    """
    try:
        c = a / b
    except ZeroDivisionError as err:
        print('Error: ', err)
    else:
        return round(c, 2)


my_div = (lambda num_1, num_2: num_1 / num_2)


def user(l_name, f_name, city, birth, email='', phone=''):
    """Задание № 2: Функция выводит данные о пользователе одной строкой.

    Именованные параметры:
    f_name -- имя,
    l_name -- фамилия,
    birth -- год рождения,
    city -- город проживания,
    email -- email,
    phone -- телефон.

    """
    print(f'Пользователь: {f_name} {l_name}, {birth} г.р., проживает в городе {city}, '
          f'email - {email if email != "" else "None"}, телефон - {phone if phone != "" else "None"}')


def my_func(*args):
    """Задание № 3: Функция возвращает сумму 2-х найбольших позиционных аргументов."""

    my_list = list(args)
    my_list.remove(min(my_list))

    return sum(my_list)


def degree(x, y):
    """Задание № 4: Функция возводит число x в степень y.

    Позиционные параметры:
    x -- действительное положительное число,
    y -- целое отрицательное число.

    """
    print('pow(x, y) = ', pow(x, y))
    print('x ** y = ', x ** y)

    deg = 1
    for i in range(abs(y)):
        deg = deg * x

    return 1 / deg


def sum_numbers(str1):
    """Задание № 5: Функция выводит сумму чисел последовательности.

    str1 -- строка чисел, разделённых пробелом.
    Функция осуществляет очистку введённой строки от символов, которые не являются цифрами.

    """
    try:
        my_list = list(map(float, str1.split()))
    except ValueError:
        print('Error: В строке есть символы, которые не являются цифрами. Очистка строки!')
        str2 = str1
        for s in str1:
            try:
                if s != ' ':
                    float(s)
                else:
                    continue
            except ValueError:
                str2 = str2.replace(s, '')
        my_list = list(map(float, str2.split()))
        print('Подготовленный список чисел для суммы: ', my_list)
        return sum(my_list)
    else:
        print('Подготовленный список чисел для суммы: ', my_list)
        return sum(my_list)


def int_func(world):
    """Задания № 6, 7: Функция выводит любое слово с прописной буквы.

    world -- слово из маленьких латинских букв.
    Функция осуществляет очистку слова от символов, которые не являются латинскими буквами.

    """
    w1 = world
    for w in world:
        if ord(w) in range(97, 123):
            continue
        else:
            w1 = w1.replace(w, '')
    return w1.title()


while True:
    task = input('Enter the task number (1-7): ')
    if task == '1':
        print(f'Задание № {task}:')
        while True:
            num = input('Введите два числа через пробел (10 20): ').split()
            print(num)
            try:
                num = list(map(float, num))
                num1, num2 = num[0], num[1]
            except ValueError as error:
                print('Error: ', error)
            else:
                print(division(num1, num2))
                try:
                    print((lambda num_1, num_2: num_1 / num_2)(num1, num2))
                    print(my_div(num1, num2))
                except ZeroDivisionError as err0:
                    print('Error: ', err0)

            print('=' * 50)
            if input('Для выхода из задания нажмите "Q", для продолжения "Enter": ').upper() == "Q":
                break

    elif task == '2':
        print(f'Задание № {task}:')
        while True:
            params = ('Имя', 'Фамилия', 'Год рождения', 'Город проживания', 'Email', 'Телефон')
            data = []
            print('Введите данные пользователя:')
            for par in params:
                data.append(input(f'{par}: '))

            user(f_name=data[0], l_name=data[1], birth=data[2], city=data[3], email=data[4], phone=data[5])

            print('=' * 50)
            if input('Для выхода из задания нажмите "Q", для продолжения "Enter": ').upper() == "Q":
                break

    elif task == '3':
        print(f'Задание № {task}:')
        while True:
            num = input('Введите три числа через пробел (10 20 30): ').split()
            print(num)
            try:
                num = list(map(int, num))
                num1, num2, num3 = num[0], num[1], num[2]
            except ValueError as error:
                print('Error: ', error)
            else:
                print(my_func(num1, num2, num3))

            print('=' * 50)
            if input('Для выхода из задания нажмите "Q", для продолжения "Enter": ').upper() == "Q":
                break

    elif task == '4':
        print(f'Задание № {task}:')
        while True:
            try:
                num1 = abs(float(input('Введите основание степени в виде действительного числа: ')))
                num2 = int(input('Введите показатель степени в виде целого отрицательного числа: '))
                num2 = -abs(num2)
            except ValueError:
                print(f'Ошибка ввода! Повторите ввод.')
                continue
            print(f'{num1} в степени {num2}: ', degree(num1, num2))

            print('=' * 50)
            if input('Для выхода из задания нажмите "Q", для продолжения "Enter": ').upper() == "Q":
                break

    elif task == '5':
        print(f'Задание № {task}:')
        sum_num = 0
        while True:
            print('Введите строку чисел через пробел (10 20 1). Для выхода используйте "Q"')
            string = input('Введите строку чисел: ').upper()
            if 'Q' in string:
                ind = string.index('Q')
                sum_num = sum_num + sum_numbers(string[:ind])
                print('Окончательная сумма введённых чисел: ', sum_num)
                break
            else:
                sum_num = sum_num + sum_numbers(string)
                print('Предварительная сумма введённых чисел: ', sum_num)
                print('-' * 50)
                continue

        print('=' * 50)

    elif task == '6':
        print(f'Задание № {task}:')
        while True:
            n_world = input('Введите слово из маленьких латинских букв: ').lower()
            if ' ' in n_world:
                print('Error: Введено несколько слов. Повторите ввод!')
            else:
                print(int_func(n_world))

            print('=' * 50)
            if input('Для выхода из задания нажмите "Q", для продолжения "Enter": ').upper() == "Q":
                break

    elif task == '7':
        print(f'Задание № {task}:')
        while True:
            string = input('Введите латинскими буквами строку из слов, разделённых пробелом: ')
            string = string.lower().split()
            n_string = ''
            for n_world in string:
                n_string += int_func(n_world) + ' '
            print(n_string[:-1])

            print('=' * 50)
            if input('Для выхода из задания нажмите "Q", для продолжения "Enter": ').upper() == "Q":
                break

    else:
        print('Программа завершена!')
        break
