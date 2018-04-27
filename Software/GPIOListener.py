#!/bin/env/python
# David Wright
# Copyright 2017
# Written for Python 3.5.2
from PyQt5.QtCore import QThread
import PyQt5.QtCore as QtCore
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

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

	def decodeBinary(self, bitList):
		if len(bitList) != 3:
			print("Unknown number of bits sent to decodeBinary: %i"%(len(bitList)))

		value = 4*int(bitList[0]) + 2 * int(bitList[1]) + bitList[2]
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

	def gpioRead(self, pin):
		result = -1
		rawValue = GPIO.input(pin)
		if  rawValue == GPIO.HIGH:
			result = 1
		elif rawValue == GPIO.LOW:
			result = 0

		return result

	def judge0Signal(channel):
		buttonBits = [gpioRead(pin) for pin in judge0Pins]
		(self.thisPerson, self.thisValue)  = decodeJudgeSignal(decodeBinary(buttonBits))# Read from GPIO to decode signal
		thisJudge = 0
		self.thisTime = datetime.datetime.now()
		self.judgeTrigger(thisJudge)

	def judge1Signal(self):
		buttonBits = [gpioRead(pin) for pin in judge1Pins]
		(self.thisPerson, self.thisValue)  = decodeJudgeSignal(decodeBinary(buttonBits))# Read from GPIO to decode signal

		thisJudge = 1
		self.thisTime = datetime.datetime.now()
		self.judgeTrigger(thisJudge)

	def judge2Signal(self):
		buttonBits = [gpioRead(pin) for pin in judge2Pins]
		(self.thisPerson, self.thisValue)  = decodeJudgeSignal(decodeBinary(buttonBits))# Read from GPIO to decode signal
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

	def startRoundPushed(self):
		self.startRoundDetected.emit()

	def pauseRoundPushed(self):
		self.pauseRoundDetected.emit()

	def resetRoundPushed(self):
		self.resetRoundDetected.emit()

	def penaltyPushed(self):
		personCode = -1
		if gpioRead(redPenaltyPin) == 1 and gpioRead(bluePenaltyPin) == 0:
			personCode = 0
		elif gpioRead(redPenaltyPin) == 0 and gpioRead(bluePenaltyPin) == 1:
			personCode = 1
		else:
			print("Unknown combination of penalty pin presses:")
			print("Red Pin: %i" %(gpioRead(redPenaltyPin)))
			print("Blue Pin: %i" %(gpioRead(bluePenaltyPin)))
		self.penaltyDetected.emit(personCode)

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

		#GPIO.setwarnings(False) # Ignore warning for now
		GPIO.setmode(GPIO.BCM) # Use physical pin numbering
		# Falling edge detection on all pins for judge boxes
		# Judge 0 input pins
		judge0pins = [2,3,4]
		GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.add_event_detect(2,GPIO.FALLING,callback=judge0Signal)
		GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.add_event_detect(3,GPIO.FALLING,callback=judge0Signal)
		GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.add_event_detect(4,GPIO.FALLING,callback=judge0Signal)

		# Judge 1 input pins
		judge1Pins = [17,27,22]
		GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.add_event_detect(17,GPIO.FALLING,callback=judge1Signal)
		GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.add_event_detect(27,GPIO.FALLING,callback=judge1Signal)
		GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.add_event_detect(22,GPIO.FALLING,callback=judge1Signal)

		# Judge 2 input pins
		judge2Pins = [10,9,11]
		GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.add_event_detect(10,GPIO.FALLING,callback=judge2Signal)
		GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.add_event_detect(9,GPIO.FALLING,callback=judge2Signal)
		GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.add_event_detect(11,GPIO.FALLING,callback=judge2Signal)

		# Timer input pins
		timerPins = [5,6,13,19,26]
		startPin = timerPins[0]
		pausePin = timerPins[1]
		resetPin = timerPins[2]
		redPenaltyPin = timerPins[3]
		bluePenaltyPin = timerPins[4]
		GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		GPIO.add_event_detect(5,GPIO.RISING,callback=startRoundPushed)
		GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		GPIO.add_event_detect(6,GPIO.RISING,callback=pauseRoundPushed)
		GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		GPIO.add_event_detect(13,GPIO.RISING,callback=resetRoundPushed)
		GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		GPIO.add_event_detect(19,GPIO.RISING,callback=redPenaltyPushed)
		GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		GPIO.add_event_detect(26,GPIO.RISING,callback=bluePenaltyPushed)


	def __del__(self):
		#GPIO.cleanup() # Clean up
		self.wait()
