# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic

from PyQt5.QtCore import QThread, QTimer
from time import sleep


class TrafficLight(QThread):
    __colors = ["#dcdcdc", "#dcdcdc", "#dcdcdc"]
    timers = ['', '', '']

    def __init__(self, time_colors):
        QThread.__init__(self)
        self.time_colors = time_colors

    def run(self):
        colors = ["#ff0000", "#ffff00", "#55ff00", "#dcdcdc"]
        while True:
            for i, t in enumerate(self.time_colors):
                for j in range(0, 3):
                    if j != i:
                        self.__colors[j] = colors[3]
                        self.timers[j] = ''
                    else:
                        self.__colors[j] = colors[i]
                        self.timers[j] = str(self.time_colors[i])
                for k in range(t, -1, -1):
                    sleep(1)
                    self.timers[i] = str(k)


class App(QWidget):
    show_more = True
    tic = False

    def __init__(self, time_colors):
        QWidget.__init__(self)
        self.color = TrafficLight(time_colors)
        self.color.start()
        self.setColor = self.color._TrafficLight__colors
        self.t = self.color.timers
        self.tr_light = uic.loadUi('tr_light.ui')
        self.tr_light.show()
        self.set_light()
        # запускаем таймер для отображения мигающих : на времени
        self.timer = QTimer()
        self.timer.timeout.connect(self.set_light)
        self.timer.start(1000)  # обновление данных из setData каждую секунду

    # метод изменяет цвета и отображает обратный отчёт времени
    def set_light(self):
        self.tr_light.l_red.setStyleSheet(
            f"background-color: {self.setColor[0]};\n"
            "border-radius: 25px;")
        self.tr_light.l_yellow.setStyleSheet(
            f"background-color: {self.setColor[1]};\n"
            "border-radius: 25px;")
        self.tr_light.l_green.setStyleSheet(
            f"background-color: {self.setColor[2]};\n"
            "border-radius: 25px;")
        self.tr_light.l_red.setText(self.t[0])
        self.tr_light.l_yellow.setText(self.t[1])
        self.tr_light.l_green.setText(self.t[2])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App([7, 2, 5])
    app.exec_()
