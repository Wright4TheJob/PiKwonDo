#!/bin/env/python
# David Wright
# Copyright 2017
# Written for Python 3.5.2
from PyQt5.QtCore import QThread
import PyQt5.QtCore as QtCore

# Timer.py
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import datetime
import time
import traceback, sys

class TimerThread(QThread):

	timerTicked = pyqtSignal(int)
	timerDone = pyqtSignal()
	def __init__(self, duration):
		QThread.__init__(self)
		self.timeLeft = int(duration)

	def __del__(self):
		self.wait()

	def run(self):
		time.sleep(1)
		while self.timeLeft > 0:
			self.timeLeft = self.timeLeft - 1
			self.timerTicked.emit(self.timeLeft)
			time.sleep(1)
		self.timerDone.emit()
