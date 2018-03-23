#!/bin/env/python
# David Wright
# Copyright 2017
# Written for Python 3.5.2

# Timer.py
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import datetime
import time
import traceback, sys

class TimerSignals(QObject):
	timerTicked = pyqtSignal(int) # Expects integer number of seconds to run timer
	timerDone = pyqtSignal()

class TimerWorker(QRunnable):
	def __init__(self, duration):
		super(TimerWorker, self).__init__()
		self.timeLeft = int(duration)
		self.signals = TimerSignals()

	@pyqtSlot()
	def run(self):
		time.sleep(1)
		while self.timeLeft > 0:
			self.timeLeft = self.timeLeft - 1
			self.signals.timerTicked.emit(self.timeLeft)
			time.sleep(1)
		self.signals.timerDone.emit()
