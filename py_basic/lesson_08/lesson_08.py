# -*- coding: utf-8 -*-
"""Выполнение задания к уроку № 8. ООП. Полезные дополнения."""


class MyDate:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def set_date(cls, string):
        try:
            day, month, year = list(map(int, string.split('-')))
        except ValueError as error:
            print('Error: ', error)
        else:
            return cls(day, month, year)

    @staticmethod
    def val_date(obj):
        dict_day = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        # day, month, year = MyDate(obj.date).set_date(obj.date)
        if obj.month not in dict_day.keys():
            return 'Ошибка ввода месяца'
        elif obj.day not in range(1, dict_day.get(obj.month) + 1):
            return 'Ошибка ввода дня'
        elif obj.year not in range(1900, 2022):
            return 'Ошибка ввода года'
        elif obj.month == 2 and obj.year % 4 == 0 and obj.day not in range(1, dict_day.get(obj.month) + 2):
            return 'Ошибка ввода дня'
        else:
            return f'День:  {obj.day:2}\nМесяц: {obj.month:2}\nГод: {obj.year}'
# ======================================================================================
# task № 2


class MyZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt

    def __str__(self):
        return f'{self.txt}'


def my_division():
    try:
        div = list(map(float, input('Введите делимое и делитель через пробел: ').split()))
        if div[1] == 0:
            raise MyZeroDivisionError('Деление на ноль!')
    except (ValueError, MyZeroDivisionError) as error:
        print('Error: ', error)
    else:
        print(round(div[0] / div[1], 2))
# ====================================================================================
# task № 3


class MyTypeError(Exception):
    def __init__(self, txt):
        self.txt = txt

    def __str__(self):
        return f'{self.txt} - недопустимый ввод! Допустимы только целые или вещественные числа'


class CustomIntFloatList:
    my_list = []

    def __init__(self, string=None):
        if string:
            self.set_list(string)

    def set_list(self, string):
        try:
            for word in string.split():
                num_str = ''.join([letter for letter in word if letter.isdigit() or letter == '.'])
                if num_str != '':
                    if '.' in num_str:
                        value = float(num_str)
                    else:
                        value = int(num_str)
                    self.my_list.append(value)
                value_str = ''.join([letter for letter in word if not letter.isdigit()]).replace('.', '')
                if value_str != '':
                    raise MyTypeError(value_str)
        except MyTypeError as error:
            print(error)

    def get_list(self):
        return self.my_list
# ====================================================================================
# task № 7


class ComplexNumer:
    def __init__(self, real, imaginary):
        self.c_num = complex(real, imaginary)

    def __str__(self):
        return f'Комплексное число: {self.c_num}'

    def __add__(self, other):
        sum_complex = complex(self.c_num.real + other.c_num.real, self.c_num.imag + other.c_num.imag)
        return f'Сумма 2-х комплексных чисел: {self.c_num + other.c_num}; {sum_complex}'

    def __mul__(self, other):
        mul_complex = complex(self.c_num.real * other.c_num.real - self.c_num.imag * other.c_num.imag,
                              self.c_num.real * other.c_num.imag + self.c_num.imag * other.c_num.real)
        return f'Произведение 2-х комплексных чисел: {self.c_num * other.c_num}; {mul_complex}'
# ====================================================================================


while True:
    task = input('Enter the task number (1-7): ')
    if task == '1':
        print(f'Задание № {task}:')
        while True:
            my_date = input('Введите дату в формате - день-месяц-год: ')
            print(my_date)
            date = MyDate.set_date(my_date)
            print(date)
            print(MyDate.val_date(date))

            print('=' * 50)
            if input('Для выхода - "Q", для продолжения "Enter": ').upper() == "Q":
                break

    elif task == '2':
        print(f'Задание № {task}: Проверка деления 2-х чисел.')
        while True:
            my_division()

            print('=' * 50)
            if input('Для выхода - "Q", для продолжения "Enter": ').upper() == "Q":
                break

    elif task == '3':
        print(f'Задание № {task}: Заполнение списка числами.')
        while True:
            new_str = input('Введите число или несколько через пробел. Для выхода - "stop": ').upper()
            if "STOP" in new_str:
                ind = new_str.index("STOP")
                if ind != 0:
                    new_list = CustomIntFloatList(new_str[:ind])
                new_list2 = CustomIntFloatList()
                print(f'Ваш список из целых и вещественных чисел:\n{new_list2.get_list()}')
                break
            else:
                new_list = CustomIntFloatList(new_str)

        print('=' * 50)

    elif task == '4':
        print(f'Задание № {task}:')
        while True:
            pass
            print('=' * 50)
            if input('Для выхода - "Q", для продолжения "Enter": ').upper() == "Q":
                break

    elif task == '5':
        print(f'Задание № {task}:')
        while True:
            pass

            print('=' * 50)
            if input('Для выхода - "Q", для продолжения "Enter": ').upper() == "Q":
                break

    elif task == '6':
        print(f'Задание № {task}:')
        while True:
            pass
            print('=' * 50)
            if input('Для выхода - "Q", для продолжения "Enter": ').upper() == "Q":
                break

    elif task == '7':
        print(f'Задание № {task}: Операции с комплексными числами')
        while True:
            try:
                real_num = input('Введите действительные части комплексного числа через пробел: ').split()
                real_num = list(map(float, real_num))
                r_num, im_num = real_num[0], real_num[1]
                complex_num_1 = ComplexNumer(r_num, im_num)
                print(complex_num_1)

                real_num = input('Введите действительные части комплексного числа через пробел: ').split()
                real_num = list(map(float, real_num))
                r_num, im_num = real_num[0], real_num[1]
                complex_num_2 = ComplexNumer(r_num, im_num)
                print(complex_num_2)
            except ValueError as err:
                print('Error: ', err)
            else:
                print(complex_num_1 + complex_num_2)
                print(complex_num_1 * complex_num_2)

            print('=' * 50)
            if input('Для выхода - "Q", для продолжения "Enter": ').upper() == "Q":
                break

    else:
        print('Программа завершена!')
        break
