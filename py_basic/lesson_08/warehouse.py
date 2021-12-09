# -*- coding: utf-8 -*-
"""Выполнение задач №№ 4-6 к уроку № 8. Проект 'Склад оргтехники' """
from abc import ABC, abstractmethod


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
    name = 'printer'

    @property
    def set_batch(self):
        if self.data_valid():
            volume = round(self.quantity * self.volume, 2)
            return self.name, self.model, self.cost, self.quantity, volume
        else:
            return None


class BatchScanners(OfficeEquipment):
    name = 'scanner'

    @property
    def set_batch(self):
        if self.data_valid():
            volume = round(self.quantity * self.volume, 2)
            return self.name, self.model, self.cost, self.quantity, volume
        else:
            return None


class BatchCopiers(OfficeEquipment):
    name = 'copier'

    @property
    def set_batch(self):
        if self.data_valid():
            volume = round(self.quantity * self.volume, 2)
            return self.name, self.model, self.cost, self.quantity, volume
        else:
            return None


class WareHouse(dict):
    wh_dict = {}        # словарь для хранения данных о наличии оргтехники на складе
    wh_capacity = 30    # ёмкость склада в м.куб.

    def __init__(self, dict_request):
        self.dict_request = dict_request

    @classmethod
    def set_data(cls, *subjects):
        set_wh = {el[0]: {el[1]: {'cost': el[2], 'quantity': el[3]}} for el in subjects if el != []}
        set_wh.update({'volume': [el[4] for el in subjects if el != []]})
        print(set_wh)
        return cls(set_wh)

    def add_goods(self):
        wh_copy = self.wh_dict
        volume_request = sum(self.dict_request['volume'])
        if wh_copy == {}:
            wh_copy.update(self.dict_request)
            wh_copy.update({'volume': volume_request})
        else:
            try:
                volume = wh_copy['volume'] + volume_request
                if volume >= self.wh_capacity:
                    raise WareHouseCapacityError(volume, round(self.wh_capacity - wh_copy['volume'], 2))
            except WareHouseCapacityError as error:
                print(f'Error: {error}\r\033[39m')  # \r\033[39m - сброс цвета текста по умолчанию
                return self.wh_dict
            else:
                wh_copy['volume'] = volume
                self.dict_request.pop('volume')

                for key_1, value in self.dict_request.items():
                    if key_1 in wh_copy.keys():
                        for key_2 in value.keys():
                            if key_2 in wh_copy[key_1].keys():
                                wh_copy[key_1][key_2]['quantity'] += self.dict_request[key_1][key_2]['quantity']
                            else:
                                wh_copy[key_1][key_2] = self.dict_request[key_1][key_2]
                    else:
                        wh_copy.update(self.dict_request)

        capacity = round(wh_copy['volume'] / self.wh_capacity * 100, 2)
        print(f'Склад заполнен на: {capacity}%')

        return self.wh_dict

    def delivery_goods(self):
        wh_copy = self.wh_dict
        try:
            if wh_copy == {}:
                raise WareHouseQuantityError(0)

            volume_request = self.dict_request.pop('volume')
            print(self.dict_request.keys())
            for key_1, value in self.dict_request.items():
                if key_1 in wh_copy.keys():
                    for i, key_2 in enumerate(value.keys()):
                        if key_2 in wh_copy[key_1].keys():
                            quantity = wh_copy[key_1][key_2]['quantity'] - self.dict_request[key_1][key_2]['quantity']
                            if quantity >= 0:
                                wh_copy[key_1][key_2]['quantity'] = quantity
                                wh_copy['volume'] -= volume_request[i]
                            else:
                                raise WareHouseQuantityError(key_2)
                        else:
                            raise WareHouseQuantityError(1)
                else:
                    raise WareHouseQuantityError(1)
        except WareHouseQuantityError as error:
            print(f'Error: {error}\r\033[39m')  # \r\033[39m - сброс цвета текста по умолчанию
            return f'{self.wh_dict}'
        else:
            capacity = round(wh_copy['volume'] / self.wh_capacity * 100, 2)
            print(f'Склад заполнен на: {capacity}%')
            return self.wh_dict


p = BatchPrinters('hp', 10000, 15, 0.3)
print(f'Новая партия принтеров:\n{p}')
print(f'Сформирована партия торара: {p.set_batch}')

s = BatchScanners('hp', 5000, 12, 0.1)
print(f'Новая партия сканеров:\n{s}')
print(f'Сформирована партия торара: {s.set_batch}')

c = BatchCopiers('hp', 4000, 13, 0.2)
print(f'Новая партия ксероксов:\n{c}')
print(f'Сформирована партия торара: {c.set_batch}')

set_dict = WareHouse.set_data(p.set_batch, s.set_batch)
print(WareHouse.add_goods(set_dict))
set_dict = WareHouse.set_data(c.set_batch)
print(WareHouse.add_goods(set_dict))

p = BatchPrinters('hp', 10000, 10, 0.3)
print(f'Новая партия принтеров:\n{p}')
print(f'Сформирована партия торара: {p.set_batch}')
set_dict = WareHouse.set_data(p.set_batch)
print(WareHouse.add_goods(set_dict))

p = BatchPrinters('canon', 12000, 10, 0.35)
print(f'Новая партия принтеров:\n{p}')
print(f'Сформирована партия торара: {p.set_batch}')
s = BatchScanners('hp', 5000, 10, 0.1)
print(f'Новая партия сканеров:\n{s}')
print(f'Сформирована партия торара: {s.set_batch}')
set_dict = WareHouse.set_data(p.set_batch, s.set_batch)
print(WareHouse.add_goods(set_dict))

p = BatchPrinters('canon', 12000, 5, 0.35)
print(f'Новая партия принтеров:\n{p}')
print(f'Сформирована партия торара: {p.set_batch}')
s = BatchScanners('cannon', 6000, 10, 0.18)
print(f'Новая партия сканеров:\n{s}')
print(f'Сформирована партия торара: {s.set_batch}')
c = BatchCopiers('siemens', 5000, 15, 0.25)
print(f'Новая партия ксероксов:\n{c}')
print(f'Сформирована партия торара: {c.set_batch}')
set_dict = WareHouse.set_data(p.set_batch, s.set_batch, c.set_batch)
print(WareHouse.add_goods(set_dict))

c = BatchCopiers('siemens', 5000, 35, 0.25)
print(f'Новая партия ксероксов:\n{c}')
print(f'Сформирована партия торара: {c.set_batch}')
set_dict = WareHouse.set_data(c.set_batch)
print(WareHouse.add_goods(set_dict))

p = BatchPrinters('canon', 12000, 5, 0.35)
print(f'Новая партия принтеров:\n{p}')
print(f'Сформирована партия торара: {p.set_batch}')
s = BatchScanners('cannon', 6000, 5, 0.18)
print(f'Новая партия сканеров:\n{s}')
print(f'Сформирована партия торара: {s.set_batch}')
c = BatchCopiers('siemens', 5000, 25, 0.25)
print(f'Новая партия ксероксов:\n{c}')
print(f'Сформирована партия торара: {c.set_batch}')
set_dict = WareHouse.set_data(p.set_batch, s.set_batch, c.set_batch)
print(WareHouse.delivery_goods(set_dict))
