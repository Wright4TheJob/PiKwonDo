#!/bin/env/python
# David Wright
# Copyright 2017
# Written for Python 3.5.2


#Import
import sys
import datetime
from PyQt5.QtWidgets import (QWidget, QTreeView, QMessageBox, QHBoxLayout,
							 QFileDialog, QLabel, QSlider, QCheckBox,
							 QLineEdit, QVBoxLayout, QApplication, QPushButton,
							 QTableWidget, QTableWidgetItem,QSizePolicy,
							 QGridLayout,QGroupBox, QMainWindow,QAction)
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt, QTimer, QCoreApplication, QThread, QRect
import MainUI
import os
import math
import csv

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

class MainWindow(QMainWindow):
	def __init__(self):
		self.programLoaded = False
		super(self.__class__, self).__init__()

		# Initialize variables
		self.redScore = 0
		self.blueScore = 0
		self.redPenalties = 0
		self.bluePenalties = 0
		self.round = 1
		self.roundLength = 90 # seconds
		self.timeLeft = self.roundLength

		self.drawUI(self)
		#self.startButton.clicked.connect(self.startOptimization)

		self.programLoaded = True

	def drawUI(self, MainWindow):
		#Builds GUI
		MainWindow.setObjectName(_fromUtf8("MainWindow"))
		MainWindow.resize(1000, 800)
		#MainWindow.showFullScreen()
		self.centralwidget = QWidget(MainWindow)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

		self.width = MainWindow.frameGeometry().width()
		self.height = MainWindow.frameGeometry().height()
		self.penaltyBarHeight = 50
		self.timeHeight = 100

		self.redPenaltyText = "Penalies: "
		for i in range(0,self.redPenalties):
			self.redPenaltyText += "X"
		self.bluePenaltyText = "Penalies: "
		for i in range(0,self.bluePenalties):
			self.bluePenaltyText += "X"
		self.timeString = str(datetime.timedelta(seconds=self.timeLeft))
		self.timeString = ':'.join(str(self.timeString ).split(':')[1:])
		self.timeString = self.timeString[1:]
		self.setWindowTitle('PiKwonDo')
		self.activateWindow()
		self.raise_()
		self.show()
		MainWindow.setCentralWidget(self.centralwidget)

		menuBar = self.menuBar()

		file_menu = menuBar.addMenu('&File')

#		open_file = QAction('&Open', self)
#		open_file.setShortcut('Ctrl+O')
#		open_file.setStatusTip('Load Truss Design')
#		#open_file.triggered.connect(self.load_data)
#		file_menu.addAction(open_file)

#		saveInput_file = QAction('&Save Input Design',self)
#		saveInput_file.setStatusTip('Save Optimized Design')
		#saveInput_file.triggered.connect(self.saveInputData)
#		file_menu.addAction(saveInput_file)

		exit_action = QAction('&Exit', self)
		exit_action.setShortcut('Ctrl+Q')
		exit_action.setStatusTip('Exit application')
		exit_action.triggered.connect(self.close) #This is built in
		file_menu.addAction(exit_action)

		control_menu = menuBar.addMenu('&Control')

		redPointAction = QAction('&Red Point', self)
		redPointAction.setShortcut('r')
		#bluePointAction.setStatusTip('Exit application')
		redPointAction.triggered.connect(lambda: self.redPoint(1)) #This is built in
		control_menu.addAction(redPointAction)

		bluePointAction = QAction('&Blue Point', self)
		bluePointAction.setShortcut('b')
		#bluePointAction.setStatusTip('Exit application')
		bluePointAction.triggered.connect(lambda: self.bluePoint(1)) #This is built in
		control_menu.addAction(bluePointAction)

		startAction = QAction('&Start Round', self)
		#bluePointAction.setStatusTip('Exit application')
		startAction.triggered.connect(self.startRound) #This is built in
		control_menu.addAction(startAction)

		pauseAction = QAction('&Pause Round', self)
		#pauseAction.setStatusTip('Exit application')
		pauseAction.triggered.connect(self.pauseRound) #This is built in
		control_menu.addAction(pauseAction)

		resumeAction = QAction('&Resume Round', self)
		#bluePointAction.setStatusTip('Exit application')
		resumeAction.triggered.connect(self.resumeRound) #This is built in
		control_menu.addAction(resumeAction)

		resetAction = QAction('&Reset Round', self)
		#bluePointAction.setStatusTip('Exit application')
		resetAction.triggered.connect(self.resetRound) #This is built in
		control_menu.addAction(resetAction)

		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def paintEvent(self, e):
		qp = QPainter()
		qp.begin(self)
		self.drawBackground(qp)
		self.drawScores(e,qp)
		self.drawPenalties(e,qp)
		self.drawTime(e,qp)
		qp.end()

	def drawBackground(self, qp):
		col = QColor(0, 0, 0, 1)
		col.setNamedColor('#d4d4d4')
		qp.setPen(Qt.NoPen)

		qp.setBrush(QColor(255, 0, 0))
		qp.drawRect(0, 0, self.width/2, self.height+1)

		qp.setBrush(QColor(0, 0, 255))
		qp.drawRect(self.width/2, 0, self.width/2+2, self.height+1)

		# Penalty bar
		qp.setBrush(QColor(0, 0, 0,100))
		qp.drawRect(0, 0, self.width, self.penaltyBarHeight)

		# Time box
		qp.setBrush(QColor(0, 0, 0, 255))
		qp.drawRect(self.width/4, self.penaltyBarHeight, self.width/2, self.timeHeight)

	def drawScores(self, event, qp):
		qp.setPen(QColor(255, 255, 255))
		qp.setFont(QFont('Decorative', 100))
		qp.drawText(QRect(0, 0, self.width/2, self.height), Qt.AlignCenter, str(int(self.redScore)))
		qp.drawText(QRect(self.width/2, 0, self.width/2+2, self.height), Qt.AlignCenter, str(int(self.blueScore)))

	def drawPenalties(self,event,qp):
		offset = 10
		qp.setPen(QColor(255, 255, 255))
		qp.setFont(QFont('Decorative', 20))
		qp.drawText(QRect(offset, 0, self.width/2, self.penaltyBarHeight), (Qt.AlignLeft | Qt.AlignVCenter), self.redPenaltyText)
		qp.drawText(QRect(self.width/2+offset, 0, self.width/2, self.penaltyBarHeight), (Qt.AlignLeft | Qt.AlignVCenter), self.bluePenaltyText)

	def drawTime(self,event,qp):
		qp.setPen(QColor(255, 255, 255))
		qp.setFont(QFont('Decorative', 50))
		qp.drawText(QRect(self.width/4, self.penaltyBarHeight, self.width/2, self.timeHeight), Qt.AlignCenter, self.timeString)

	def load_data(self):
		#Write this function
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		fileName, _ = QFileDialog.getOpenFileName(self,
			"QFileDialog.getOpenFileName()",
			"","All Files (*);;Text Files (*.txt)",
			options=options)
		if fileName:
			self.initialNodeArray = []
			self.initialBeamArray = []
			with open(fileName, 'r') as fin:
				reader = csv.reader(fin, delimiter=',')
				for line in reader:
					#print(line)
					if len(line) == 8:
						self.initialNodeArray.append([float(line[0]),float(line[1]),int(line[2]),int(line[3]),int(line[4]),int(line[5]),float(line[6]),float(line[7])])
					elif len(line) == 5:
						self.initialBeamArray.append([int(line[0]),int(line[1]),float(line[2]),float(line[3]),float(line[4])])
					else:
						print('Unexpected line length')
			self.redrawInputTables()
			self.graph_canvas.plotTruss(self.initialNodeArray,self.initialBeamArray)

	def bluePoint(self,pointValue):
		self.blueScore	+= pointValue

	def redPoint(self,pointValue):
		self.redScore	+= pointValue

	def startRound(self):
		print("Starting Round")

	def pauseRound(self):
		print("Pausing Round")

	def resumeRound(self):
		print("Resuming Round")

	def resetRound(self):
		print("Resetting Round")

def main():
	app = QApplication(sys.argv)
	form = MainWindow()
	form.show()
	app.exec_()

if __name__ == '__main__':
	main()
