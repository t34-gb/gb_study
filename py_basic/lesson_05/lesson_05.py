"""Выполнение задания к уроку № 5. Работа с файлами."""
from random import randint, random
import json

while True:
    task = input('Enter the task number (1-7): ')
    if task == '1':
        print(f'Задание № {task}:')
        file = open("text_1.txt", "w", encoding="utf-8")
        while True:
            new_str = input('Введите строку для записи в файл. Для выхода - пустая строка: ')
            if new_str != '':
                print(new_str, file=file)
            else:
                file.close()
                break
        print('=' * 50)

    elif task == '2':
        print(f'Задание № {task}. Предварительно выполнить задание № 1:')
        try:
            with open("text_1.txt", "r", encoding="utf-8") as file:
                for num, new_str in enumerate(file.readlines()):
                    print(f'{num}-я строка состоит из {len(new_str.split())} слов')
                print(f'Количество строк в файле "{file.name}": ', num + 1)
        except FileNotFoundError as err:
            print(err)
        print('=' * 50)

    elif task == '3':
        print(f'Задание № {task}:')
        with open("text_3.txt", "r", encoding="utf-8") as file:
            name_list = []
            middle_salary = 0
            for i, line in enumerate(file.readlines()):
                if float(line.split()[1]) < 20000:
                    name_list.append(line.split()[0])
                middle_salary += float(line.split()[1])

            print('Сотрудники: ', end='')
            for name in name_list:
                print(name, end=', ')
            print('имеют зарплату меньше 20 тыс.')
            print(f'Средний оклад сотрудников: {middle_salary / (i + 1):.2f}')
        print('=' * 50)

    elif task == '4':
        print(f'Задание № {task}:')
        my_dict = {'1': 'Один', '2': 'Два', '3': 'Три', '4': 'Четыре'}
        new_file = open("text_4n.txt", "w", encoding='utf-8')
        with open("text_4.txt", "r", encoding="utf-8") as file:
            for line in file.readlines():
                new_str = ''
                line_list = line.split()
                line_list[0] = my_dict.get(line_list[2])
                for i in range(len(line_list)):
                    if i != len(line_list) - 1:
                        new_str += line_list[i] + ' '
                    else:
                        new_str += line_list[i] + '\n'
                new_file.write(new_str)
        new_file.close()
        print('Создан новый файл "text_4n.txt"')
        print('=' * 50)

    elif task == '5':
        print(f'Задание № {task}:')
        with open("text_5.txt", "w", encoding='utf-8') as file:
            while True:
                line_list = [str(round(random() * 10, 2)) for _ in range(0, randint(5, 20))]
                print(line_list)
                new_str = ' '.join(line_list) + '\n'
                file.write(new_str)
                if input('Для выхода нажмите "Q", для продолжения "Enter": ').upper() == "Q":
                    break
        print('Создан новый файл "text_5.txt"')
        sum_file = []
        with open("text_5.txt", "r", encoding='utf-8') as file:
            for line in file.readlines():
                sum_line = sum(list(map(float, line.split())))
                sum_file.append(sum_line)
            print(f'Сумма чисел в файле: {sum(sum_file):.2f}')
        print('=' * 50)

    elif task == '6':
        print(f'Задание № {task}:')
        subj_study = {}
        with open("text_6.txt", "r", encoding="utf-8") as file:
            for line in file.readlines():
                sum_num = 0
                line_list = line.split()
                for word in line_list:
                    num = ''.join([letter for letter in word if letter.isdigit()])
                    if num != '':
                        sum_num += int(num)
                subj_study.update({line_list[0][:-1]: sum_num})

        print(f'\n Словарь с названиями предметов и количеством занятий по ним: \n {"*" * 30}')
        print(subj_study)
        for key, value in subj_study.items():
            print(f'{key:>15}: {value}')
        print("*" * 30)
        print('=' * 50)

    elif task == '7':
        print(f'Задание № {task}:')
        profit_list = []
        dict_companies = {}
        companies = []
        with open('text_7.txt', 'r', encoding='utf-8') as file:
            for line in file.readlines():
                line_list = line.split()
                profit = int(line_list[2]) - int(line_list[3])
                dict_companies.update({line_list[0]: profit})
                if profit >= 0:
                    profit_list.append(profit)

            companies.append(dict_companies)
            companies.append({'average_profit': sum(profit_list) / len(profit_list)})
            print(companies)
        with open('text_7.json', 'w', encoding='utf-8') as file_js:
            json.dump(companies, file_js, ensure_ascii=False, indent=4)
        print('=' * 50)

    else:
        print('Программа завершена!')
        break
