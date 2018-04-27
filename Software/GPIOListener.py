#! /bin/env/python3
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
import threading

class ButtonHandler(threading.Thread):
    def __init__(self, pin, func, edge='both', bouncetime=200):
        super().__init__(daemon=True)

        self.edge = edge
        self.func = func
        self.pin = pin
        self.bouncetime = float(bouncetime)/1000

        self.lastpinval = GPIO.input(self.pin)
        self.lock = threading.Lock()

    def __call__(self, *args):
        if not self.lock.acquire(blocking=False):
            return

        t = threading.Timer(self.bouncetime, self.read, args=args)
        t.start()

    def read(self, *args):
        pinval = GPIO.input(self.pin)

        if (
                ((pinval == 0 and self.lastpinval == 1) and
                 (self.edge in ['falling', 'both'])) or
                ((pinval == 1 and self.lastpinval == 0) and
                 (self.edge in ['rising', 'both']))
        ):
            self.func(*args)

        self.lastpinval = pinval
        self.lock.release()

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

		#GPIO.setwarnings(False) # Ignore warning for now
		GPIO.setmode(GPIO.BCM) # Use physical pin numbering
		# Falling edge detection on all pins for judge boxes
		# Judge 0 input pins
		self.judge0Pins = [2,3,4]
		GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.add_event_detect(2,GPIO.FALLING,callback=self.judge0Signal)
		GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.add_event_detect(3,GPIO.FALLING,callback=self.judge0Signal)
		GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.add_event_detect(4,GPIO.FALLING,callback=self.judge0Signal)

		# Judge 1 input pins
		self.judge1Pins = [17,27,22]
		GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.add_event_detect(17,GPIO.FALLING,callback=self.judge1Signal)
		GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.add_event_detect(27,GPIO.FALLING,callback=self.judge1Signal)
		GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.add_event_detect(22,GPIO.FALLING,callback=self.judge1Signal)

		# Judge 2 input pins
		self.judge2Pins = [10,9,11]
		GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.add_event_detect(10,GPIO.FALLING,callback=self.judge2Signal)
		GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.add_event_detect(9,GPIO.FALLING,callback=self.judge2Signal)
		GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.add_event_detect(11,GPIO.FALLING,callback=self.judge2Signal)

		# Timer input pins
		self.timerPins = [5,6,13,19,26]
		self.startPin = self.timerPins[0]
		self.pausePin = self.timerPins[1]
		self.resetPin = self.timerPins[2]
		self.redPenaltyPin = self.timerPins[3]
		self.bluePenaltyPin = self.timerPins[4]
		GPIO.setup(self.startPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		startHandler = ButtonHandler(self.startPin, self.startRoundPushed, edge='rising', bouncetime=100)
		startHandler.start()
		GPIO.add_event_detect(self.startPin,GPIO.RISING,callback=startHandler)

		GPIO.setup(self.pausePin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		pauseHandler = ButtonHandler(self.pausePin, self.pauseRoundPushed, edge='rising', bouncetime=100)
		pauseHandler.start()
		GPIO.add_event_detect(self.pausePin,GPIO.RISING,callback=pauseHandler)

		GPIO.setup(self.resetPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		resetHandler = ButtonHandler(self.resetPin, self.resetRoundPushed, edge='rising', bouncetime=100)
		resetHandler.start()
		GPIO.add_event_detect(self.resetPin,GPIO.RISING,callback=resetHandler)

		GPIO.setup(self.redPenaltyPin , GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		redPenaltyHandler = ButtonHandler(self.redPenaltyPin, self.penaltyPushed, edge='rising', bouncetime=100)
		redPenaltyHandler.start()
		GPIO.add_event_detect(self.redPenaltyPin ,GPIO.RISING,callback=redPenaltyHandler)

		GPIO.setup(self.bluePenaltyPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		bluePenaltyHandler = ButtonHandler(self.bluePenaltyPin, self.penaltyPushed, edge='rising', bouncetime=100)
		bluePenaltyHandler.start()
		GPIO.add_event_detect(self.bluePenaltyPin,GPIO.RISING,callback=redPenaltyHandler)

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

	def judge0Signal(self,callback):
		buttonBits = [self.gpioRead(pin) for pin in self.judge0Pins]
		(self.thisPerson, self.thisValue)  = decodeJudgeSignal(decodeBinary(buttonBits))# Read from GPIO to decode signal
		thisJudge = 0
		self.thisTime = datetime.datetime.now()
		self.judgeTrigger(thisJudge)

	def judge1Signal(self,callback):
		buttonBits = [self.gpioRead(pin) for pin in self.judge1Pins]
		(self.thisPerson, self.thisValue)  = decodeJudgeSignal(decodeBinary(buttonBits))# Read from GPIO to decode signal

		thisJudge = 1
		self.thisTime = datetime.datetime.now()
		self.judgeTrigger(thisJudge)

	def judge2Signal(self,callback):
		buttonBits = [self.gpioRead(pin) for pin in self.judge2Pins]
		(self.thisPerson, self.thisValue)  = decodeJudgeSignal(decodeBinary(buttonBits))# Read from GPIO to decode signal
		thisJudge = 2
		self.thisTime = datetime.datetime.now()
		self.judgeTrigger(thisJudge)

	def judgeTrigger(self,judge):
		print('Judge Trigger called with judge code %i' %(judge))
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

	def startRoundPushed(self,callback):
		self.startRoundDetected.emit()

	def pauseRoundPushed(self,callback):
		self.pauseRoundDetected.emit()

	def resetRoundPushed(self,callback):
		self.resetRoundDetected.emit()

	def penaltyPushed(self,callback):
		personCode = -1
		if self.gpioRead(self.redPenaltyPin) == 1 and self.gpioRead(self.bluePenaltyPin) == 0:
			personCode = 0
			print('Penalty for Red')
		elif self.gpioRead(self.redPenaltyPin) == 0 and self.gpioRead(self.bluePenaltyPin) == 1:
			personCode = 1
			print('Penalty for Blue')
		else:
			print("Unknown combination of penalty pin presses:")
			print("Red Pin: %i" %(self.gpioRead(self.redPenaltyPin)))
			print("Blue Pin: %i" %(self.gpioRead(self.bluePenaltyPin)))
		self.penaltyDetected.emit(personCode)

	def __del__(self):
		#GPIO.cleanup() # Clean up
		self.wait()
