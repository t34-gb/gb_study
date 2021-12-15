from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QTableWidgetItem

from models import *

Form, Window = uic.loadUiType("warehouse.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

# Устанавливаем заголовки таблицы
form.table_wh.setHorizontalHeaderLabels(["Тип товара", "Модель",
                                         "Стоимость", "Количество", "Объём"])

# Устанавливаем всплывающие подсказки на заголовки
form.table_wh.horizontalHeaderItem(0).setToolTip("Тип оргтехники ")
form.table_wh.horizontalHeaderItem(1).setToolTip("Модель оргтехники ")
form.table_wh.horizontalHeaderItem(2).setToolTip("Стоимость в руб. ")
form.table_wh.horizontalHeaderItem(3).setToolTip("Количество шт. ")
form.table_wh.horizontalHeaderItem(4).setToolTip("Габаритные размеры в м.куб. ")

# Устанавливаем выравнивание на заголовки
form.table_wh.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)


# функция для обновление данных на складе
def update_goods(data):
    # print(data)
    wh_volume = data.pop('wh_volume')
    list_1 = []
    for key_1, value in data.items():
        name = key_1
        for key_2, value_2 in value.items():
            model = key_2
            cost = value_2['cost']
            quantity = value_2['quantity']
            volume = value_2['volume']
            list_1.append((name, model, cost, quantity, volume))

    form.table_wh.setRowCount(len(list_1))      # определяем количество строк в таблице
    # заполняем таблицу данными
    for i, value1 in enumerate(list_1):
        for j, value2 in enumerate(value1):
            form.table_wh.setItem(i, j, QTableWidgetItem(f'{value2}'))

    data.update({'wh_volume': wh_volume})
    capacity = int(round(wh_volume / WareHouse.wh_capacity * 100))
    form.progressBar.setValue(capacity)  # процент заполнения склада

    # делаем ресайз колонок по содержимому
    form.table_wh.resizeColumnsToContents()


# заполнение формы данными из json-файла
with open('warehouse.json', 'r', encoding='utf-8') as file_js:
    dict_str = file_js.read()
    form.text_json.setText(dict_str)    # вывод текста из json-файла о товаре на складе
    dict_data = json.loads(dict_str)    # десериализация данных из json-файла в словарь

update_goods(dict_data)  # заполнение таблицы данными из json-файла
WareHouse.wh_dict = dict_data
print(WareHouse.wh_dict)

list_batch = []
list_request = []
list_req = []

form.btn_batch.clicked.connect(lambda: form_batch())
form.btn_request.clicked.connect(lambda: create_request())
form.btn_add.clicked.connect(lambda: add_goods())
form.btn_delivery.clicked.connect(lambda: delivery_goods())


# функция для добавления товара на склад согласно списка словарей запросов
def add_goods():
    # print(list_request)
    for request in list_req:                # добавления товара на склад
        WareHouse.add_goods(request)
        # print(request.wh_dict)
    form.btn_add.setEnabled(False)          # деактивация кнопки
    form.btn_delivery.setEnabled(False)     # деактивация кнопки
    form.text_batch.clear()                 # очистка текста с партией товара
    with open('warehouse.json', 'r', encoding='utf-8') as file:
        form.text_json.setText(file.read())  # вывод текста из json-файла о товаре на складе

    update_goods(WareHouse.wh_dict)          # обновление данных на складе


# функция для выдачи товара со склада согласно списка словарей запросов
def delivery_goods():
    # print(list_request)
    for request in list_req:                # выдача товара со склада
        WareHouse.delivery_goods(request)
        form.progressBar.setValue(request.capacity)
        # print(request.wh_dict)
    form.btn_add.setEnabled(False)          # деактивация кнопки
    form.btn_delivery.setEnabled(False)     # деактивация кнопки
    form.text_batch.clear()                 # очистка текста с партией товара
    with open('warehouse.json', 'r', encoding='utf-8') as file:
        form.text_json.setText(file.read())  # вывод текста из json-файла о товаре на складе

    update_goods(WareHouse.wh_dict)         # обновление данных на складе


# функция для создания из списка партий товара запроса на склад в виде списка словарей
def create_request():
    global list_request, list_req
    list_request = []
    list_req = []
    for batch in list_batch:
        my_request = WareHouse.set_data(batch)
        list_request.append(my_request.dict_request)
        list_req.append(my_request)
    form.btn_add.setEnabled(True)       # активация кнопки
    form.btn_delivery.setEnabled(True)  # активация кнопки
    form.btn_request.setEnabled(False)  # деактивация кнопки
    return list_request


# функция для формирования партий товара в виде списка из данных пользователя с формы
def form_batch():
    global list_batch
    list_batch = []
    form.text_batch.clear()
    if form.ch_printer.checkState():
        p = BatchPrinters(form.p_model.text(), float(form.p_cost.text()),
                          int(form.p_quantity.text()), float(form.p_volume.text()))
        form.text_batch.setText(form.text_batch.toPlainText() + f'{p.set_batch}\n')
        list_batch.append(p.set_batch)
    if form.ch_scanner.checkState():
        s = BatchScanners(form.s_model.text(), float(form.s_cost.text()),
                          int(form.s_quantity.text()), float(form.s_volume.text()))
        form.text_batch.setText(form.text_batch.toPlainText() + f'{s.set_batch}\n')
        list_batch.append(s.set_batch)
    if form.ch_copier.checkState():
        c = BatchCopiers(form.c_model.text(), float(form.c_cost.text()),
                         int(form.c_quantity.text()), float(form.c_volume.text()))
        form.text_batch.setText(form.text_batch.toPlainText() + f'{c.set_batch}\n')
        list_batch.append(c.set_batch)
    else:
        pass

    form.btn_request.setEnabled(True)   # активация кнопки
    return list_batch


app.exec_()
