#!/bin/env/python
# David Wright
# Copyright 2017
# Written for Python 3.5.2
from PyQt5.QtCore import QThread
import PyQt5.QtCore as QtCore
#import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

# PointListener.py
#from PyQt5.QtGui import *
#from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import datetime
import time
import traceback, sys

class GPIOListenerThread(QThread):

	pointDetected = pyqtSignal(int,int) # Person(Red = 0, Blue = 1), Points
	penaltyDetected = pyqtSignal(int) # Person(Red = 0, Blue = 1)
	startRoundDetected = pyqtSignal()
	pauseRoundDetected = pyqtSignal()
	resetRoundDetected = pyqtSignal()

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
		self.thisPerson = 0 # Red is 0, blue is 1
		self.thisValue = 0
		self.thisJudge = 0

		GPIO.setwarnings(False) # Ignore warning for now
		GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
		GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge

	def decodeBinary(self, mostsigBit, middlesigBit, leastsigBit):
		value = 4*int(mostsigBit) + 2 * int(middlesigBit) + leastsigBit
		return value

	def decodeJudgeSignal(self,input):
			if input > 7:
				print("Unexpected input to DecodeJudgeSignal: %i"%(input))
			if input > 3:
				person = 1
				points = input - 3
			else:
				person = 0
				points = input + 1
		return (person,points)

	def judge0Signal(self):
		bit1 = 1 # GPIO.read...
		bit2 = 0
		bit3 = 1
		(self.thisPerson, self.thisValue)  = decodeJudgeSignal(decodeBinary(bit1,bit2,bit3))# Read from GPIO to decode signal
		thisJudge = 0
		self.thisTime = datetime.datetime.now()
		self.judgeTrigger(thisJudge)

	def judge1Signal(self):
		bit1 = 1 # GPIO.read...
		bit2 = 0
		bit3 = 1
		(self.thisPerson, self.thisValue)  = decodeJudgeSignal(decodeBinary(bit1,bit2,bit3))# Read from GPIO to decode signal
		thisJudge = 1
		self.thisTime = datetime.datetime.now()
		self.judgeTrigger(thisJudge)

	def judge2Signal(self):
		bit1 = 1 # GPIO.read...
		bit2 = 0
		bit3 = 1
		(self.thisPerson, self.thisValue)  = decodeJudgeSignal(decodeBinary(bit1,bit2,bit3))# Read from GPIO to decode signal
		thisJudge = 2
		self.thisTime = datetime.datetime.now()
		self.judgeTrigger(thisJudge)

	def signalDetect(self):
		print('Signal detected from GPIO')
		thisJudge = 0
		self.thisValue = 2

	def judgeTrigger(self,judge):
		# TODO:Check to make sure it does not double-log points for all three judges scoring
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

	def __del__(self):
		GPIO.cleanup() # Clean up
		self.wait()
