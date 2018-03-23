#!/bin/env/python
# David Wright
# Copyright 2017
# Written for Python 3.5.2


#Import
from PyQt5 import QtCore
from PyQt5.QtCore import QThreadPool,Qt, QTimer, QCoreApplication, QThread, QRect
from PyQt5.QtWidgets import (QWidget, QFileDialog, QApplication,QMainWindow,QAction)
from PyQt5.QtGui import QPainter, QColor, QFont
import sys
import datetime
import time
import os
import math
import csv
import Timer

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

class MainWindow(QMainWindow):
	def __init__(self):
		self.programLoaded = False
		super(self.__class__, self).__init__()

		# Settings
		self.roundLength = 90 # seconds
		self.timeLeft = self.roundLength
		self.roundQuantity = 2
		self.breakLength = 30 # seconds

		# Initialize variables
		self.redScore = 0
		self.blueScore = 0
		self.redPenalties = 0
		self.bluePenalties = 0
		self.currentSection = 1
		self.timerRunning = False
		self.setupUI(self)
		self.sectionDurations = [self.roundLength]
		for i in range(0,self.roundQuantity-1):
			self.sectionDurations.append(self.breakLength)
			self.sectionDurations.append(self.roundLength)
		self.sections = len(self.sectionDurations)
		print(self.sectionDurations)
		#self.startButton.clicked.connect(self.startOptimization)

		self.threadpool = QThreadPool()

		self.programLoaded = True

	def setupUI(self, MainWindow):
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

		self.setWindowTitle('PiKwonDo')
		self.activateWindow()
		self.raise_()
		self.show()
		MainWindow.setCentralWidget(self.centralwidget)

		menuBar = self.menuBar()

		file_menu = menuBar.addMenu('&File')

		exit_action = QAction('&Exit', self)
		exit_action.setShortcut('Ctrl+Q')
		exit_action.setStatusTip('Exit application')
		exit_action.triggered.connect(self.close) #This is built in
		file_menu.addAction(exit_action)

		round_menu = menuBar.addMenu('&Match')
		startAction = QAction('&Start Match', self)
		#bluePointAction.setStatusTip('Exit application')
		startAction.triggered.connect(self.startRound) #This is built in
		round_menu.addAction(startAction)

		pauseAction = QAction('&Pause Match', self)
		#pauseAction.setStatusTip('Exit application')
		pauseAction.triggered.connect(self.pauseRound) #This is built in
		round_menu.addAction(pauseAction)

		resumeAction = QAction('&Resume Match', self)
		#bluePointAction.setStatusTip('Exit application')
		resumeAction.triggered.connect(self.resumeRound) #This is built in
		round_menu.addAction(resumeAction)

		resetAction = QAction('&Reset Match', self)
		#bluePointAction.setStatusTip('Exit application')
		resetAction.triggered.connect(self.resetRound)
		round_menu.addAction(resetAction)


		red_menu = menuBar.addMenu('&Red')

		redPointAction = QAction('&Point', self)
		redPointAction.setShortcut('r')
		#bluePointAction.setStatusTip('Exit application')
		redPointAction.triggered.connect(lambda: self.redPoint(1))
		red_menu.addAction(redPointAction)

		redPenaltyAction = QAction('&Penalty',self)
		#redPenaltyAction.setShortcut('')
		#bluePointAction.setStatusTip('Exit application')
		redPenaltyAction.triggered.connect(self.redPenalty)
		red_menu.addAction(redPenaltyAction)

		blue_menu = menuBar.addMenu('&Blue')
		bluePointAction = QAction('&Point', self)
		bluePointAction.setShortcut('b')
		#bluePointAction.setStatusTip('Exit application')
		bluePointAction.triggered.connect(lambda: self.bluePoint(1))
		blue_menu.addAction(bluePointAction)

		bluePenaltyAction = QAction('&Penalty',self)
		#redPenaltyAction.setShortcut('')
		#bluePointAction.setStatusTip('Exit application')
		bluePenaltyAction.triggered.connect(self.bluePenalty)
		blue_menu.addAction(bluePenaltyAction)

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
		qp.setFont(QFont('Decorative', self.width/4))
		qp.drawText(QRect(0, 0, self.width/2, self.height), Qt.AlignCenter, str(int(self.redScore)))
		qp.drawText(QRect(self.width/2, 0, self.width/2+2, self.height), Qt.AlignCenter, str(int(self.blueScore)))

	def drawPenalties(self,event,qp):
		offset = 10
		self.redPenaltyText = "Penalties: "
		for i in range(0,self.redPenalties):
			self.redPenaltyText += "X"
		self.bluePenaltyText = "Penalties: "
		for i in range(0,self.bluePenalties):
			self.bluePenaltyText += "X"
		qp.setPen(QColor(255, 255, 255))
		qp.setFont(QFont('Decorative', 20))
		qp.drawText(QRect(offset, 0, self.width/2, self.penaltyBarHeight), (Qt.AlignLeft | Qt.AlignVCenter), self.redPenaltyText)
		qp.drawText(QRect(self.width/2+offset, 0, self.width/2, self.penaltyBarHeight), (Qt.AlignLeft | Qt.AlignVCenter), self.bluePenaltyText)

	def drawTime(self,event,qp):
		self.timeString = str(datetime.timedelta(seconds=self.timeLeft))
		self.timeString = ':'.join(str(self.timeString ).split(':')[1:])
		self.timeString = self.timeString[1:]
		qp.setPen(QColor(255, 255, 255))
		qp.setFont(QFont('Decorative', int(self.timeHeight*3/4)))
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

	def redPoint(self,pointValue):
		self.redScore += pointValue
		self.update()

	def redPenalty(self):
		self.redPenalties += 1
		self.update()

	def bluePoint(self,pointValue):
		self.blueScore	+= pointValue
		self.update()

	def bluePenalty(self):
		self.bluePenalties += 1
		self.update()

	def startMatch(self):
		self.currentSection = 1
		self.startRound()

	def startRound(self):
		if self.timerRunning == False:
			self.timerThread = Timer.TimerThread(self.sectionDurations[self.currentSection-1])
			# Connect to emitted signals
			self.timerThread.timerTicked.connect(self.timerTicked)
			self.timerThread.timerDone.connect(self.timerDone)
			# Start the thread
			self.timerThread.start()
		self.timerRunning = True

	def pauseRound(self):
		if self.timerRunning == True:
			self.timerThread.terminate()
		self.timerRunning = False

	def resumeRound(self):
		self.timerThread = Timer.TimerThread(self.timeLeft)
		# Connect to emitted signals
		self.timerThread.timerTicked.connect(self.timerTicked)
		self.timerThread.timerDone.connect(self.timerDone)
		# Start the thread
		if self.timerRunning == False:
			self.timerThread.start()
		self.timerRunning = True

	def resetRound(self):
		self.redScore = 0
		self.blueScore = 0
		self.redPenalties = 0
		self.bluePenalties = 0
		self.currentSection = 1
		self.timeLeft = self.roundLength
		if self.timerRunning == True:
			self.timerThread.terminate()
		self.update()
		self.timerRunning = False

	def resizeEvent(self, event):
		#print("resize")
		self.width = self.frameGeometry().width()
		self.height = self.frameGeometry().height()
		self.update()
		QMainWindow.resizeEvent(self, event)

	def timerTicked(self,newTime):
		self.timeLeft = newTime
		self.update()

	def timerDone(self):
		#self.timerThread.terminate()
		self.timerRunning = False
		self.timeLeft = 0
		self.update()
		time.sleep(1)
		print("Current section: %i"%(self.currentSection))
		print("Total Sections: %i"%(self.sections))
		if self.currentSection < self.sections:
			self.currentSection += 1
			# TODO:Wait for manual trigger for start of next section?
			self.startRound()

def main():
	app = QApplication(sys.argv)
	form = MainWindow()
	form.show()
	app.exec_()

if __name__ == '__main__':
	main()
