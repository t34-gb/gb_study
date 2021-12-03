# -*- coding: utf-8 -*-
"""Выполнение задания к уроку № 7. ООП. Продвинутый уровень."""
from random import randint
# from numpy import array
from abc import ABC, abstractmethod


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        str_matrix = []
        for row in self.matrix:
            str_matrix.append(''.join(['%7s' % str(x) for x in row]))
        return '\n'.join([row for row in str_matrix])

    def __add__(self, other):
        # result = array(self.matrix) + array(other.matrix)
        # result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
        result = [map(sum, zip(*i)) for i in zip(self.matrix, other.matrix)]
        return result
# =================================================================================


class Clothes(ABC):
    result = 0

    def __init__(self, param):
        self.param = param

    @abstractmethod
    def calculation_fabric(self):
        pass

    def __add__(self, other):
        Clothes.result += self.calculation_fabric + other.calculation_fabric
        return Suit(0)

    def __str__(self):
        res = Clothes.result
        Clothes.result = 0
        return f'Необходимо {res} метров ткани'


class Coat(Clothes):

    @property
    def calculation_fabric(self):
        return round(self.param / 6.5 + 0.5, 2)


class Suit(Clothes):

    @property
    def calculation_fabric(self):
        return round(2 * self.param + 0.3)
# ==================================================================================


class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __str__(self):
        return '*' * self.cell + f' ({self.cell})'

    def __add__(self, other):
        return self.cell + other.cell

    def __sub__(self, other):
        return self.cell - other.cell if self.cell > other.cell else "Отрицательный результат"

    def __mul__(self, other):
        return self.cell * other.cell

    def __truediv__(self, other):
        return self.cell // other.cell

    def make_order(self, row):
        x, y = divmod(self.cell, row)
        return '\n'.join(['*' * row for _ in range(x)]) + '\n' + '*' * y


while True:
    task = input('Enter the task number (1-3): ')
    if task == '1':
        print(f'Задание № {task}:')
        while True:
            my_matrix1 = []
            my_matrix2 = []
            size_matrix = input('Введите через пробел размер матрицы (3 2): ').split()
            try:
                size_matrix = list(map(int, size_matrix))
            except ValueError as error:
                print('Error: ', error)
            else:
                my_matrix1 = [[randint(-10, 40) for _ in range(size_matrix[1])] for _ in range(size_matrix[0])]
                my_matrix2 = [[randint(-10, 40) for _ in range(size_matrix[1])] for _ in range(size_matrix[0])]
                print(my_matrix1)
                print(my_matrix2)
                matrix_1 = Matrix(my_matrix1)
                matrix_2 = Matrix(my_matrix2)
                print(f'Строковое представление матрицы № 1:\n{matrix_1}')
                print(f'Строковое представление матрицы № 2:\n{matrix_2}')
                sum_matrix = matrix_1 + matrix_2
                print(f'Строковое представление суммарной матрицы:\n{Matrix(sum_matrix)}')

            print('=' * 50)
            if input('Для выхода - "Q", для продолжения "Enter": ').upper() == "Q":
                break

    elif task == '2':
        print(f'Задание № {task}:')
        while True:
            coat = Coat(152)
            print(coat.calculation_fabric)
            suit = Suit(170)
            print(suit.calculation_fabric)
            print(coat + suit)

            print('=' * 50)
            if input('Для выхода - "Q", для продолжения "Enter": ').upper() == "Q":
                break

    elif task == '3':
        print(f'Задание № {task}:')
        while True:
            try:
                cell_1 = Cell(int(input('Введите количество ячеек в 1-й клетке: ')))
                cell_2 = Cell(int(input('Введите количество ячеек во 2-й клетке: ')))
                my_row = int(input('Введите количество ячеек в ряду: '))
            except ValueError as error:
                print('Error: ', error)
            else:
                print('Строковое представление клетки № 1: '.rjust(50), cell_1)
                print('Строковое представление клетки № 2: '.rjust(50), cell_2)
                print('Сложение. Объединение двух клеток: '.rjust(50), cell_1 + cell_2)
                print('Вычитание. Выполняется при  № 1 > № 2: '.rjust(50), cell_1 - cell_2)
                print('Умножение. Создается общая клетка: '.rjust(50), cell_1 * cell_2)
                print('Деление. Целочисленное деление: '.rjust(50), cell_1 / cell_2)
                print(f'Организация ячеек клетки по рядам:\n{cell_1.make_order(5)}')

            print('=' * 50)
            if input('Для выхода - "Q", для продолжения "Enter": ').upper() == "Q":
                break

    else:
        print('Программа завершена!')
        break
