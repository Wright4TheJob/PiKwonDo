#! /bin/env/python3
# David Wright
# Copyright 2017
# Written for Python 3.5.2
from PyQt5.QtCore import QThread
import PyQt5.QtCore as QtCore
import os

# PointListener.py
from PyQt5.QtCore import *
import datetime
import time
import traceback, sys
import threading
import sys

from PyQt5.QtWidgets import (QWidget, QTreeView, QMessageBox, QHBoxLayout,
                             QFileDialog, QLabel, QSlider, QCheckBox,
                             QLineEdit, QVBoxLayout, QApplication, QPushButton,
                             QTableWidget, QTableWidgetItem,QSizePolicy,
                             QGridLayout,QGroupBox, QMainWindow,QAction)
from PyQt5.QtCore import Qt, QTimer, QCoreApplication, QThread
from PyQt5 import QtCore, QtGui
from scipy import stats
from sympy import *
import numpy as np
import os
import cmath
import math
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import rcParams
import matplotlib.mlab as mlab
import csv
import GPIOListener

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Testing Timer Board'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 200
        self.initUI()
        self.start_gpio_scan()

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
        scanner = GPIOListener.HardwareControllerScanner()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
