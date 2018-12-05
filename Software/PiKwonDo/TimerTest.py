#! /bin/env/python3
# David Wright
# Copyright 2017
# Written for Python 3.5.6
import sys
import queue
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel
from PyQt5.QtCore import Qt
import os
import GPIOListener

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Testing Timer Board'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 200
        self.button_statuses = None
        self.initUI()
        self.start_gpio_scan()
        self.dropbox = queue.Queue()
        refresh_thread = GPIOListener.PeriodicActionThread(self.read_queue,1000)

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        grid_layout = QGridLayout()

        self.labels = []
        self.statuses = []
        for i in range(0,5):
            label = QLabel("Button %i"%(i+1),self)
            label.setAlignment(Qt.AlignCenter)
            grid_layout.addWidget(label,0,i)
            status = QLabel("",self)
            status.setStyleSheet("background: red")
            grid_layout.addWidget(status,1,i)
            self.statuses.append(status)

        self.setLayout(grid_layout)
        self.show()

    def start_gpio_scan(self):
        self.scanner = GPIOListener.HardwareControllerScanner()

    def read_queue(self):
        try:
            data = self.dropbox.get(block=False)
            self.button_statuses = [x[0] for x in data]
            self.update_UI()
        except queue.Empty:
            # print('Queue is empty, not redrawing')
            pass

    def update_UI(self):
        [set_label_color(label,value) for label, value in zip(self.statuses,self.button_statuses)]

    def set_label_color(self,label,value):
        if value == 1:
            label.setStyleSheet('background: green')
        else:
            label.setStyleSheet('background: red')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
