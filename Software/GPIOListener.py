#!/bin/env/python
# David Wright
# Copyright 2017
# Written for Python 3.5.2
from PyQt5.QtCore import QThread
import PyQt5.QtCore as QtCore

# PointListener.py
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import datetime
import time
import traceback, sys

class GPIOListenerThread(QThread):

	pointDetected = pyqtSignal(int,int) # Person(Red = 0, Blue = 1), Points
	penaltyDetected = pyqtSignal(int) # Person(Red = 0, Blue = 1)
	roundControl = pyqtSignal(int)# Start/Resume = 0, pause = 1, rest = 2

	def __init__(self, judgeGapThreshhold):
		QThread.__init__(self)
		print("Starting gpio listener")
		self.maxGapTime = judgeGapThreshhold
		#self.lastTime = datetime.datetime.now()# - 1 minute to ensure first trigger counts
		self.lastTime = [0,0,0]
		self.lastValue = [0,0,0]

		self.lastPerson = 0
		self.lastValue = 0
		self.lastJudge = 0 # Judge codes are 0, 1, and 2
		self.thisTime = datetime.datetime.now()# - 1 minute to ensure first trigger counts
		self.thisPerson = 0
		self.thisValue = 0
		self.thisJudge = 0

	def signalDetect(self):
		print('Signal detected from GPIO')
		self.thisTime = datetime.datetime.now()
		thisJudge = 0
		self.thisValue = 1
		self.judgeTrigger(thisJudge)

	def judgeTrigger(self,judge):
		# TODO:Check to make sure it is not the same judge double-tapping
		# TODO:Check to make sure it does not double-log points for all three judges scoring
		# TODO:Include 3+1 butten combo for 4-point score. Or include four-point physical button
		# Two judges within x milliseconds
		# One point even if all three judges trigger
		# Two points if two judges trigger in rapid succession
		# (timeToLastSelfTrigger > gapBetweenPoints) AND (timeToOtherJudgeTrigger < judgeGapThreshhold) AND (thisValue == otherJudgeValue)
		thisTriggerTime = datetime.datetime.now()
		thisJudgeTimeDelta = thisTriggerTime - self.lastTime[judge]
		timeDelta = self.thisTime - self.lastTime
		if timeDelta.milliseconds < self.maxGapTime: # Log only trigger events within threshold
			if self.lastJudge != self.thisJudge: # Prevent double-tapping by the same judge (debounce)
				if self.lastPerson == self.thisPerson: # Only add scores if judeges trigger for the same competitor
					if self.lastValue == self.thisValue: # If the two judges trigger the same point value, use that value
						self.pointDetected.emit(self.thisPerson,self.thisValue)

		self.lastValue = self.thisValue
		self.lastPerson = self.thisPerson
		self.lastTime = self.thisTime
