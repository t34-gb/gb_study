"""Выполнение задания к уроку № 6. Объектно-ориентированное программирование."""
from time import sleep
from random import choice


class TrafficLight:
    __color = {7: "31m", 2: "33m", 5: "32m"}

    def running(self):
        text = "Цвет светофора"
        num = 0
        while num != 2:
            for timer, color in self.__color.items():
                for i in range(timer, -1, -1):
                    sleep(1)
                    print(f'\r\033[{color} {text}  {str(i)}', end='')
            num += 1
        print()


class Road:
    mass = 25

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mass(self, height=5):
        mass_asphalt = self._length * self._width * self.mass * height // 1000
        print(f'Масса асфальта, необходимого для покрытия всей дороги: {mass_asphalt} т.')


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = str(name).title()
        self.surname = str(surname).title()
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"Полное имя сотрудника: {self.surname} {self.name}"

    def get_total_income(self):
        try:
            return f"Доход сотрудника: {sum(map(float, self._income.values()))}"
        except TypeError as err:
            print('Error! ', err)


class Car:
    direction = ['вперёд', 'назад', 'налево', 'направо']

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Автомобиль {self.name} цвета "{self.color}" поехал')

    def stop(self):
        print(f'Автомобиль {self.name} остановился')

    def turn(self):
        print(f'Автомобиль {self.name} повернул {choice(self.direction)}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name}: {self.speed} км.')


class TownCar(Car):
    def purpose(self, purpose):
        print(f'Городской автомобиль {self.name} для - {purpose}')

    def show_speed(self):
        if self.speed > 60:
            print(f'Внимание! Автомобиль {self.name} превысил скорость на {self.speed - 60} км.')
        else:
            super().show_speed()


class SportCar(Car):
    def purpose(self, purpose):
        print(f'Гоночный автомобиль {self.name} для - {purpose}')


class WorkCar(Car):
    def purpose(self, purpose):
        print(f'Городской автомобиль {self.name} - {purpose}')

    def show_speed(self):
        if self.speed > 40:
            print(f'Внимание! Автомобиль {self.name} превысил скорость на {self.speed - 40} км.')
        else:
            super().show_speed()


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)

    def purpose(self):
        if self.is_police:
            print(f'Полицейский автомобиль {self.name}')


class Stationery:
    def __init__(self, title="канцелярская принадлежность"):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки для "{self.title}"')


class Pen(Stationery):
    def draw(self):
        print(f'Отрисовка для "{self.title}" класса Pen')


class Pencil(Stationery):
    def draw(self):
        print(f'Отрисовка для "{self.title}" класса Pencil')


class Handle(Stationery):
    def draw(self):
        print(f'Отрисовка для "{self.title}" класса Handle')


while True:
    task = input('Enter the task number (1-5): ')
    if task == '1':
        print(f'Задание № {task}:')
        while True:
            tr_light = TrafficLight()
            tr_light.running()
            if input('Для выхода нажмите "Q", для продолжения "Enter": ').upper() == "Q":
                break

        print('=' * 50)

    elif task == '2':
        print(f'Задание № {task}:')
        while True:
            print('Расчёт массы асфальта, необходимого для покрытия дороги.')
            my_height = int(input('Введите толщину покрытия асфальтом в сатниметрах. '))
            my_length = int(input('Введите длину дороги для асфальтирования в метрах. '))
            my_width = int(input('Введите ширину дороги для асфальтирования в метрах. '))
            my_road = Road(my_length, my_width)
            my_road.calc_mass(my_height)

            if input('Для выхода нажмите "Q", для продолжения "Enter": ').upper() == "Q":
                break

        print('=' * 50)

    elif task == '3':
        print(f'Задание № {task}:')
        while True:
            params = ('Имя', 'Фамилия', 'Должность', 'Оклад', 'Премия')
            data = []
            print('Введите данные пользователя:')
            for par in params:
                data.append(input(f'{par}: '))
            n_name, n_surname, n_position, n_wage, n_bonus = data
            pers = Position(n_name, n_surname, n_position, n_wage, n_bonus)
            print(pers.name)
            print(pers.surname)
            print(pers.position)
            print(pers._income)
            print(pers.get_full_name())
            print(pers.get_total_income())

            if input('Для выхода нажмите "Q", для продолжения "Enter": ').upper() == "Q":
                break

        print('=' * 50)

    elif task == '4':
        print(f'Задание № {task}:')
        while True:
            params = ('Скорость', 'Цвет', 'Марка', 'Назначение')
            print('Введите данные городского автомобиля:')
            data = [input(f'{par}: ') for par in params]
            n_speed, n_color, n_name, n_purpose = data
            town_car = TownCar(float(n_speed), n_color, n_name)
            town_car.purpose(n_purpose)
            town_car.go()
            town_car.show_speed()
            town_car.turn()
            town_car.stop()
            print('Введите данные спортивного автомобиля:')
            data = [input(f'{par}: ') for par in params]
            n_speed, n_color, n_name, n_purpose = data
            sport_car = SportCar(float(n_speed), n_color, n_name)
            sport_car.purpose(n_purpose)
            sport_car.go()
            sport_car.show_speed()
            sport_car.turn()
            sport_car.stop()
            print('Введите данные рабочего автомобиля:')
            data = [input(f'{par}: ') for par in params]
            n_speed, n_color, n_name, n_purpose = data
            work_car = WorkCar(float(n_speed), n_color, n_name, n_purpose)
            work_car.purpose(n_purpose)
            work_car.go()
            work_car.show_speed()
            work_car.turn()
            work_car.stop()
            print('Введите данные полицейского автомобиля:')
            data = [input(f'{par}: ') for par in params[:-1]]
            n_speed, n_color, n_name = data
            police_car = PoliceCar(float(n_speed), n_color, n_name)
            police_car.purpose()
            police_car.go()
            police_car.show_speed()
            police_car.turn()
            police_car.stop()

            if input('Для выхода нажмите "Q", для продолжения "Enter": ').upper() == "Q":
                break

        print('=' * 50)

    elif task == '5':
        print(f'Задание № {task}:')

        stationery = Stationery()
        pen = Pen("ручка")
        pencil = Pencil("карандаш")
        handle = Handle("маркер")
        supplies = [stationery, pen, pencil, handle]
        for k in supplies:
            k.draw()

        print('=' * 50)

    else:
        print('Программа завершена!')
        break
