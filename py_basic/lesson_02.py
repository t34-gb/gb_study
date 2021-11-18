print('Выполнение задания: "Урок 2. Встроенные типы и операции с ними."')

while True:
    task = input('Enter the task number (1-6): ')
    if task == '1':
        print(f'Задание № {task}:')
        while True:
            my_list = [45, 12.7, 'Python string', (1, 2, 3, 6, 12, 24), True,
                       {1, 3, 8, 0, 1, 3}, {0: 5, 1: 0.5, 'name': 'Kat'}, None,
                       [12, 'qwerty', 2.05]]
            for i in my_list:
                print(f'{i} type:', type(i))

            print('=' * 50)
            fl = input('Continue the task (y/n): ')
            if fl == 'y' or fl == 'Y':
                continue
            else:
                break

    elif task == '2':
        print(f'Задание № {task}:')
        while True:
            new_list = []
            num_list = int(input('Enter the number of list items: '))
            i = 0
            while i != num_list:
                new_list.append(input(f'Enter {i} element: '))
                i += 1
            print('The list is full. Your list:\n', new_list)

            for i in range(0, (len(new_list) // 2) * 2, 2):
                new_list[i], new_list[i + 1] = new_list[i + 1], new_list[i]

            print('New list:\n', new_list)
            print('=' * 50)
            fl = input('Continue the task (y/n): ')
            if fl == 'y' or fl == 'Y':
                continue
            else:
                break

    elif task == '3':
        print(f'Задание № {task}:')
        while True:
            list_season = ['winter', 'spring', 'summer', 'autumn']
            list_months = [(12, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11)]
            dic_months = {'winter': (12, 1, 2),
                          'spring': (3, 4, 5),
                          'summer': (6, 7, 8),
                          'autumn': (9, 10, 11)}

            # вариант решения с использованием словаря
            month = int(input('Enter the month number: '))
            for season, months in dic_months.items():
                if month in months:
                    print('Time of the year: ', season)

            # вариант решения с использованием списков
            for months in list_months:
                if month in months:
                    print('Time of the year: ', list_season[list_months.index(months)])

            print('=' * 50)
            fl = input('Continue the task (y/n): ')
            if fl == 'y' or fl == 'Y':
                continue
            else:
                break

    elif task == '4':
        print(f'Задание № {task}:')
        while True:
            my_str = input('Enter any text: ')
            setStr = my_str.split()
            num = 0
            for world in setStr:
                print(f'{num}. {world[:10]}')
                num += 1

            print('=' * 50)
            fl = input('Continue the task (y/n): ')
            if fl == 'y' or fl == 'Y':
                continue
            else:
                break

    elif task == '5':
        print(f'Задание № {task}:')
        my_list = [7, 5, 3, 3, 2]
        print('Initial list: ', my_list)
        while True:
            rating = int(input('Enter any natural number: '))
            my_list.reverse()
            for i in my_list:
                if rating == i:
                    my_list.insert(my_list.index(i), float(rating))
                    break
                elif rating < i:
                    my_list.insert(my_list.index(i), float(rating))
                    break
                elif rating > i and rating > my_list[len(my_list) - 1]:
                    my_list.append(float(rating))
                    break
                else:
                    continue

            my_list.reverse()
            print(f'The user entered a number {rating}. Result: {my_list}')
            print('=' * 50)
            fl = input('Continue the task (y/n): ')
            if fl == 'y' or fl == 'Y':
                continue
            else:
                break

    elif task == '6':
        print(f'Задание № {task}:')

        # Реализация структуры данных «Товары»
        print('Введите через пробел данные о товаре: название, цена, количество, единица измерения')
        print('Пример: компьютер 20000 5 шт.')
        list_products = []
        num = 1
        while True:
            product = input('Enter product: ').split()
            dic_product = {
                'название': product[0],
                'цена': product[1],
                'количество': product[2],
                'eд': product[3]
            }
            desc_product = (num, dic_product)
            list_products.append(desc_product)
            num += 1

            fl = input('Ввести следующий товар (д/н): ')
            if fl == 'д' or fl == 'Д':
                continue
            else:
                break

        # сбор и вывод аналитики о товарах
        key_pr = []
        val_pr = []
        name_pr = []
        price_pr = []
        number_pr = []
        unit_pr = []
        for decs_product in list_products:
            print(decs_product)
            key_pr.clear()
            val_pr.clear()
            for key in decs_product[1].keys():
                key_pr.append(key)
            for value in decs_product[1].values():
                val_pr.append(value)
            name_pr.append(val_pr[0])
            price_pr.append(val_pr[1])
            number_pr.append(val_pr[2])
            unit_pr.append(val_pr[3])

        dic_char = {
            key_pr[0]: name_pr,
            key_pr[1]: price_pr,
            key_pr[2]: number_pr,
            key_pr[3]: list(set(unit_pr)),
        }
        print('dic_char: ', dic_char)

    else:
        print('Программа завершена!')
        break
