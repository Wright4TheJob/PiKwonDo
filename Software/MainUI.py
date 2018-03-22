# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'threading_design.ui'
#
# Created: Thu Aug  6 13:47:18 2015
#      by: PyQt4 UI code generator 4.10.4

from PyQt5 import QtCore, QtGui
#from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import (QWidget,QAction,QMainWindow,QApplication)
#, QTreeView, QMessageBox, QHBoxLayout,
#							 QFileDialog, QLabel, QSlider, QCheckBox,
#							 QLineEdit, QVBoxLayout, , QPushButton,
#							 QTableWidget, QTableWidgetItem,QSizePolicy,
#							 QGridLayout,QGroupBox, QHeaderView,QComboBox,QProgressBar)
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt, QTimer, QCoreApplication, QRect
#from matplotlib.figure import Figure
#from matplotlib import rcParams
#import matplotlib.image as image
import math

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

"""
try:
	_encoding = QtGui.QApplication.UnicodeUTF8
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig)
"""

#rcParams.update({'figure.autolayout': True})

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		#Builds GUI
		MainWindow.setObjectName(_fromUtf8("MainWindow"))
		MainWindow.resize(1000, 800)
		#MainWindow.showFullScreen()
		self.centralwidget = QWidget(MainWindow)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

		# Start Button
		#self.startButton = QPushButton('Start',self)
		# Stop Button
		#self.stopButton = QPushButton('Stop',self)
		#self.stopButton.setEnabled(False)
		#self.redBackground = QLabel()
		#self.redBackground.setStyleSheet("background-color: rgb(255, 0, 0);")
		#self.blueBackground = QLabel()
		#self.blueBackground.setStyleSheet("background-color: rgb(0, 0, 255);")

		#Now we can set all the previously defined boxes into the main window
		#master_layout = QGridLayout()
		#master_layout.addWidget(self.startButton,0,0)
		#master_layout.addWidget(self.stopButton,0,1)
		#master_layout.addWidget(self.redBackground,1,0)
		#master_layout.addWidget(self.blueBackground,1,1)
		#self.centralwidget.addWidget(master_layout)
		#self.centralwidget.setLayout(master_layout)
		self.width = MainWindow.frameGeometry().width()
		self.height = MainWindow.frameGeometry().height()
		self.text = "Лев Николаевич Толстой\nАнна Каренина"
		self.redScore = "0"
		self.blueScore = "0"
		self.setWindowTitle('PiKwonDo')
		self.activateWindow()
		self.raise_()
		self.show()
		MainWindow.setCentralWidget(self.centralwidget)

		menuBar = self.menuBar()

		file_menu = menuBar.addMenu('&File')

		open_file = QAction('&Open', self)
		open_file.setShortcut('Ctrl+O')
		open_file.setStatusTip('Load Truss Design')
		#open_file.triggered.connect(self.load_data)
		file_menu.addAction(open_file)

		saveInput_file = QAction('&Save Input Design',self)
		saveInput_file.setStatusTip('Save Optimized Design')
		#saveInput_file.triggered.connect(self.saveInputData)
		file_menu.addAction(saveInput_file)

		exit_action = QAction('&Exit', self)
		exit_action.setShortcut('Ctrl+Q')
		exit_action.setStatusTip('Exit application')
		exit_action.triggered.connect(self.close) #This is built in
		file_menu.addAction(exit_action)

		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def paintEvent(self, e):
		qp = QPainter()
		qp.begin(self)
		self.drawBackground(qp)
		self.drawRedScore(e,qp)
		self.drawBlueScore(e,qp)
		qp.end()

	def drawBackground(self, qp):
		col = QColor(0, 0, 0, 1)
		col.setNamedColor('#d4d4d4')
		qp.setPen(Qt.NoPen)

		qp.setBrush(QColor(255, 0, 0))
		qp.drawRect(0, 0, self.width/2, self.height+1)

		qp.setBrush(QColor(0, 0, 255))
		qp.drawRect(self.width/2, 0, self.width/2+2, self.height+1)

		penaltyBarHeight = 50
		timeHeight = 100
		qp.setBrush(QColor(0, 0, 0,100))
		qp.drawRect(0, 0, self.width, penaltyBarHeight)

		qp.setBrush(QColor(0, 0, 0, 255))
		qp.drawRect(self.width/4, penaltyBarHeight, self.width/2, timeHeight)

	def drawRedScore(self, event, qp):
		qp.setPen(QColor(255, 255, 255))
		qp.setFont(QFont('Decorative', 100))
		qp.drawText(QRect(0, 0, self.width/2, self.height), Qt.AlignCenter, self.redScore)

	def drawBlueScore(self, event, qp):
		qp.setPen(QColor(255, 255, 255))
		qp.setFont(QFont('Decorative', 100))
		qp.drawText(QRect(self.width/2, 0, self.width/2+2, self.height), Qt.AlignCenter, self.blueScore)
