print('Выполнение задания: "Урок 1. Знакомство с Python"')

name = input('Enter your name: ')
print(f'Hi, {name}!')
bl = True

while bl:
    task = input('Enter the task number (1-6): ')
    if task == '1':
        print(f'Задание № {task}:')
        year = 2021
        year_birth = input('Enter your year of birth: ')
        print(f'You are {year - int(year_birth)} years old.')
        while True:
            a = input('Enter a number "a": ')
            b = input('Enter a number "b": ')
            sign = input('Enter a mathematical sign (-,+,*,/): ')
            if sign == '-':
                print(f'a - b = {a} {sign} {b} =', int(a) - int(b))
            elif sign == '+':
                print(f'a + b = {a} {sign} {b} =', int(a) + int(b))
            elif sign == '*':
                print(f'a * b = {a} {sign} {b} =', int(a) * int(b))
            elif sign == '/':
                print(f'a / b = {a} {sign} {b} =', int(a) / int(b))
            else:
                print('ERROR: Incorrect data entry!')
            fl = input('Continue the task (y/n): ')
            if fl == 'y' or fl == 'Y':
                continue
            else:
                break

    elif task == '2':
        print(f'Задание № {task}:')
        while True:
            num_seconds = int(input('Enter the time in seconds: '))
            hours = num_seconds // 3600
            minutes = (num_seconds - hours * 3600) // 60
            seconds = num_seconds - hours * 3600 - minutes * 60
            if hours // 10 == 0:
                hours = '0' + str(hours)
            else:
                hours = str(hours)
            if minutes // 10 == 0:
                minutes = '0' + str(minutes)
            else:
                minutes = str(minutes)
            if seconds // 10 == 0:
                seconds = '0' + str(seconds)
            else:
                seconds = str(seconds)
            # print(f'Hours: {hours}\nMinutes: {minutes}\nSeconds: {seconds}')
            print(f'The time (hh:mm:ss) - {hours}:{minutes}:{seconds}')
            print('The time (hh:mm:ss) - %s:%s:%s' % (hours, minutes, seconds))
            print('The time (hh:mm:ss) - {}:{}:{}'.format(hours, minutes, seconds))
            fl = input('Continue the task (y/n): ')
            if fl == 'y' or fl == 'Y':
                continue
            else:
                break

    elif task == '3':
        print(f'Задание № {task}:')
        while True:
            num = input('Enter any integer: ')
            sum = int(num) + int(num + num) + int(num + num + num)
            print(f'Sum of numbers: n + nn + nnn = {num} + {num + num} + {num + num + num} =', sum)
            fl = input('Continue the task (y/n): ')
            if fl == 'y' or fl == 'Y':
                continue
            else:
                break

    elif task == '4':
        print(f'Задание № {task}:')
        while True:
            num = int(input('Enter any positive integer: '))
            if num < 0:
                print('ERROR: Incorrect data entry! Repeat the input.')
                continue
            max_num = 0
            while num * 10 // 10 != 0:
                current_num = num - (num // 10) * 10
                num = num // 10
                if max_num <= current_num:
                    max_num = current_num
            print('Maximum digit: ', max_num)
            fl = input('Continue the task (y/n): ')
            if fl == 'y' or fl == 'Y':
                continue
            else:
                break

    elif task == '5':
        print(f'Задание № {task}:')
        while True:
            revenue = int(input('Введите выручку компании: '))
            costs = int(input('Введите издержки компании: '))
            profit = revenue - costs
            if profit > 0:
                print(f'Компания сработала с прибылью. '
                      f'Прибыль состовляет: {profit}, рентабельность: {profit / revenue}')
                staff = int(input('Введите количество сотрудников компании: '))
                print(f'Прибыль компании в расчете на одного сотрудника: {profit / staff}')
            else:
                print('Компания сработала в убыток, который составил', profit)
            fl = input('Continue the task (y/n): ')
            if fl == 'y' or fl == 'Y':
                continue
            else:
                break

    elif task == '6':
        print(f'Задание № {task}:')
        while True:
            a = int(input('Введите результат пробежки в первый день: '))
            b = int(input('Введите результат, к которому стремится спортсмен: '))
            day = 1
            while a < b:
                # print(f'{day}-й день: {a} км')
                a = a + a * 0.1
                day += 1
            # print(f'{day}-й день: {a} км')
            print(f'На {day}-й день спортсмен достиг результата — не менее {b} км')
            fl = input('Continue the task (y/n): ')
            if fl == 'y' or fl == 'Y':
                continue
            else:
                break
    else:
        print('Программа завершена!')
        bl = False
