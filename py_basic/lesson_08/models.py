# -*- coding: utf-8 -*-
"""Выполнение задач №№ 4-6 к уроку № 8. Проект 'Склад оргтехники' """
from abc import ABC, abstractmethod
import json


class TypeFloatError(Exception):
    def __init__(self, txt):
        self.txt = txt

    def __str__(self):
        return f'\r\033[31m{self.txt} - недопустимый ввод! Только целые или вещественные числа'


class TypeIntError(Exception):
    def __init__(self, txt):
        self.txt = txt

    def __str__(self):
        return f'\r\033[31m{self.txt} - недопустимый ввод! Только целые числа'


class WareHouseCapacityError(Exception):
    def __init__(self, txt, value):
        self.txt = txt
        self.value = value

    def __str__(self):
        return f'\r\033[31m{self.txt} - Превышена ёмкость склада! Можно принять только {self.value} м.куб. товара'


class WareHouseQuantityError(Exception):
    """Класс собственных исключений.
    Выдаёт ошибку при отсутствии товара на складе.
    """
    def __init__(self, txt):
        self.txt = txt

    def __str__(self):
        if self.txt == 0:
            return f'\r\033[31m{self.txt} - Склад пуст!!!'
        elif self.txt == 1:
            return f'\r\033[31m{self.txt} - Такого товара на складе нет!!!'
        else:
            return f'\r\033[31m{self.txt} - Такого количества товара на складе нет!!!'


class OfficeEquipment(ABC):
    """Родительский класс для всех типов оргтехники.
    __init__ - метод описывает аргументы (параметры).
    set_batch - abstractmethod, контролирует наличие метода у потомков.
    data_valid - метод для проверки входных параметров.
    """

    def __init__(self, model, cost, quantity, volume):
        self.model = model
        self.cost = cost
        self.quantity = quantity
        self.volume = volume

    @abstractmethod
    def set_batch(self):
        pass

    def data_valid(self):
        try:
            if not isinstance(self.cost, (int, float)):
                raise TypeFloatError(self.cost)
            elif not isinstance(self.volume, (int, float)):
                raise TypeFloatError
            elif not isinstance(self.quantity, int):
                raise TypeIntError(self.quantity)
        except (TypeFloatError, TypeIntError) as error:
            print(f'Error: {error}\r\033[39m')  # \r\033[39m - сброс цвета текста по умолчанию
            return False
        else:
            return True

    def __str__(self):
        return f'модель - "{self.model}" стоимостью {self.cost} руб. в количестве {self.quantity} шт.'


class BatchPrinters(OfficeEquipment):
    """Класс потомок описывает партию принтеров.
    set_batch - property, возвращает проверенные методом data_valid и преобразованные
                данные по партии принтеров.
    """
    name = 'printer'

    @property
    def set_batch(self):
        if self.data_valid():
            volume = round(self.quantity * self.volume, 2)
            return self.name, self.model, self.cost, self.quantity, volume
        else:
            return None


class BatchScanners(OfficeEquipment):
    """Класс потомок описывает партию сканеров.
    set_batch - property, возвращает проверенные методом data_valid и преобразованные
                данные по партии сканеров.
    """
    name = 'scanner'

    @property
    def set_batch(self):
        if self.data_valid():
            volume = round(self.quantity * self.volume, 2)
            return self.name, self.model, self.cost, self.quantity, volume
        else:
            return None


class BatchCopiers(OfficeEquipment):
    """Класс потомок описывает партию ксероксов.
    set_batch - property, возвращает проверенные методом data_valid и преобразованные
                данные по партии ксероксов.
    """
    name = 'copier'

    @property
    def set_batch(self):
        if self.data_valid():
            volume = round(self.quantity * self.volume, 2)
            return self.name, self.model, self.cost, self.quantity, volume
        else:
            return None


class WareHouse(dict):
    """Основной класс описывающий наличие, поступление и выдачу товара.
    wh_dict - словарь для хранения данных о наличии оргтехники на складе.
    wh_capacity = 30 - ёмкость склада в м.куб (постоянная величина).
    __init__ - метод принимающий словарь с параметрами запроса от метода set_data.
    set_data - classmethod, преобразует входные данные в словарь с параметрами запроса dict_request.
    add_goods - метод добавляет товар на склад wh_dict согласно запроса dict_request.
    delivery_goods - метод убирает товар со склада wh_dict согласно запроса dict_request.
    json_goods - метод записывает json-файл с содержимым на складе wh_dict.
    """
    wh_dict = {}  # словарь для хранения данных о наличии оргтехники на складе
    wh_capacity = 30  # ёмкость склада в м.куб.
    capacity = 0

    def __init__(self, dict_request):
        self.dict_request = dict_request

    @classmethod
    def set_data(cls, *subjects):
        set_wh = {el[0]: {el[1]: {'cost': el[2], 'quantity': el[3], 'volume': el[4]}} for el in subjects if el != []}
        set_wh.update({'wh_volume': el[4] for el in subjects if el != []})
        print(set_wh)
        return cls(set_wh)

    def add_goods(self):
        wh_copy = self.wh_dict
        volume_request = self.dict_request['wh_volume']
        if wh_copy == {}:
            wh_copy.update(self.dict_request)
        else:
            try:
                volume = wh_copy['wh_volume'] + volume_request
                if volume >= self.wh_capacity:
                    raise WareHouseCapacityError(volume, round(self.wh_capacity - wh_copy['wh_volume'], 2))
            except WareHouseCapacityError as error:
                print(f'Error: {error}\r\033[39m')  # \r\033[39m - сброс цвета текста по умолчанию
                return self.wh_dict
            else:
                wh_copy['wh_volume'] = round(volume, 2)

                self.dict_request.pop('wh_volume')
                for key_1, value in self.dict_request.items():
                    if key_1 in wh_copy.keys():
                        for key_2 in value.keys():
                            if key_2 in wh_copy[key_1].keys():
                                wh_copy[key_1][key_2]['quantity'] += self.dict_request[key_1][key_2]['quantity']
                                wh_copy[key_1][key_2]['volume'] += round(self.dict_request[key_1][key_2]['volume'], 2)
                            else:
                                wh_copy[key_1][key_2] = self.dict_request[key_1][key_2]
                    else:
                        wh_copy.update(self.dict_request)

        self.capacity = int(round(wh_copy['wh_volume'] / self.wh_capacity * 100))
        print(f'Склад заполнен на: {self.capacity}%')
        self.json_goods(self.wh_dict)
        return self.wh_dict

    def delivery_goods(self):
        wh_copy = self.wh_dict
        try:
            if wh_copy == {}:
                raise WareHouseQuantityError(0)

            volume_request = self.dict_request.pop('wh_volume')
            for key_1, value in self.dict_request.items():
                if key_1 in wh_copy.keys():
                    for key_2 in value.keys():
                        if key_2 in wh_copy[key_1].keys():
                            quantity = wh_copy[key_1][key_2]['quantity'] - self.dict_request[key_1][key_2]['quantity']
                            volume = wh_copy[key_1][key_2]['volume'] - self.dict_request[key_1][key_2]['volume']
                            if quantity >= 0:
                                wh_copy[key_1][key_2]['quantity'] = quantity
                                wh_copy[key_1][key_2]['volume'] = round(volume, 2)
                                wh_copy['wh_volume'] = round(wh_copy['wh_volume'] - volume_request, 2)
                            else:
                                raise WareHouseQuantityError(key_2)
                        else:
                            raise WareHouseQuantityError(1)
                else:
                    raise WareHouseQuantityError(1)
        except WareHouseQuantityError as error:
            print(f'Error: {error}\r\033[39m')  # \r\033[39m - сброс цвета текста по умолчанию
        else:
            self.capacity = int(round(wh_copy['wh_volume'] / self.wh_capacity * 100))
            print(f'Склад заполнен на: {self.capacity}%')
        self.json_goods(self.wh_dict)
        return self.wh_dict

    def json_goods(self, wh_dict):
        with open('warehouse.json', 'w', encoding='utf-8') as file_js:
            # json.dump(wh_dict, file_js, ensure_ascii=False, indent=4)
            # file_js.write(f'\n{json.dumps(wh_dict)}')
            file_js.write(json.dumps(wh_dict))
