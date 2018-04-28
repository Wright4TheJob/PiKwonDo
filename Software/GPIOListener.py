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
	def __init__(self, pin, func, edge='both', bouncetime=100, glitchtime=5):
		super().__init__(daemon=True)

		self.edge = edge
		self.func = func
		self.pin = pin
		#self.bouncetime = float(bouncetime)/1000
		self.glitchtime = float(glitchtime)/1000

		self.lastpinval = GPIO.input(self.pin)
		self.glitchLock = threading.Lock()
		#self.bounceLock = threading.Lock()

		if (self.edge == 'rising'):
			gpioEdge = GPIO.RISING
		elif (self.edge == 'falling'):
			gpioEdge = GPIO.FALLING

		GPIO.add_event_detect(pin, gpioEdge,callback=self)

	def __call__(self, *args):
		#if not self.bounceLock.acquire(blocking=False):
		#	return
		if not self.glitchLock.acquire(blocking=False):
			return

		glitchTimer = threading.Timer(self.glitchtime, self.glitchDone, args=args)
		glitchTimer.start()

		#bounceTimer = threading.Timer(self.bouncetime, self.bounceDone, args=args)
		#bounceTimer.start()

	def glitchDone(self, *args):
		pinval = GPIO.input(self.pin)

		if (
				((pinval == 0 and self.lastpinval == 1) and
				 (self.edge in ['falling', 'both'])) or
				((pinval == 1 and self.lastpinval == 0) and
				 (self.edge in ['rising', 'both']))
		):
			self.func(*args)

		self.lastpinval = pinval
		self.glitchLock.release()

	#def bounceDone(self, *args):
		#self.bounceLock.release()

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

		self.lastTime = datetime.datetime.now()
		self.lastJudge = 0 # Judge codes are 0, 1, and 2
		self.lastValue = 0
		self.lastFighter = 0
		self.lastPointCounted = False
		self.thisTime = datetime.datetime.now()# - 1 minute to ensure first trigger counts
		self.thisJudge = 0
		self.thisValue = 0
		self.thisFighter = 0 # Red is 0, blue is 1

		#GPIO.setwarnings(False) # Ignore warning for now
		GPIO.setmode(GPIO.BCM) # Use physical pin numbering
		# Falling edge detection on all pins for judge boxes
		# Judge 0 input pins
		self.judge0Pins = [2,3,4]
		self.judge0TriggerPin = 16
		GPIO.setup(self.judge0Pins[0], GPIO.IN)
		GPIO.setup(self.judge0Pins[1], GPIO.IN)
		GPIO.setup(self.judge0Pins[2], GPIO.IN)
		GPIO.setup(self.judge0TriggerPin, GPIO.IN)
		j0Handler = ButtonHandler(self.judge0TriggerPin, self.judge0Signal, edge='falling')
		j0Handler.start()

		# Judge 1 input pins
		self.judge1Pins = [17,27,22]
		self.judge1TriggerPin = 20
		GPIO.setup(self.judge1Pins[0], GPIO.IN)
		GPIO.setup(self.judge1Pins[1], GPIO.IN)
		GPIO.setup(self.judge1Pins[2], GPIO.IN)
		GPIO.setup(self.judge1TriggerPin, GPIO.IN)
		j1Handler = ButtonHandler(self.judge1TriggerPin, self.judge1Signal, edge='falling')
		j1Handler.start()

		# Judge 2 input pins
		self.judge2Pins = [10,9,11]
		self.judge2TriggerPin = 21
		GPIO.setup(self.judge2Pins[0], GPIO.IN)
		GPIO.setup(self.judge2Pins[1], GPIO.IN)
		GPIO.setup(self.judge2Pins[2], GPIO.IN)
		GPIO.setup(self.judge2TriggerPin, GPIO.IN)
		j2Handler = ButtonHandler(self.judge2TriggerPin, self.judge2Signal, edge='falling')
		j2Handler.start()

		# Timer input pins
		self.timerPins = [5,6,13,19,26]
		self.startPin = self.timerPins[0]
		self.pausePin = self.timerPins[1]
		self.resetPin = self.timerPins[2]
		self.redPenaltyPin = self.timerPins[3]
		self.bluePenaltyPin = self.timerPins[4]
		GPIO.setup(self.startPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		startHandler = ButtonHandler(self.startPin, self.startRoundPushed, edge='rising')
		startHandler.start()

		GPIO.setup(self.pausePin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		pauseHandler = ButtonHandler(self.pausePin, self.pauseRoundPushed, edge='rising')
		pauseHandler.start()

		GPIO.setup(self.resetPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		resetHandler = ButtonHandler(self.resetPin, self.resetRoundPushed, edge='rising')
		resetHandler.start()

		GPIO.setup(self.redPenaltyPin , GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		redPenaltyHandler = ButtonHandler(self.redPenaltyPin, self.penaltyPushed, edge='rising')
		redPenaltyHandler.start()

		GPIO.setup(self.bluePenaltyPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		bluePenaltyHandler = ButtonHandler(self.bluePenaltyPin, self.penaltyPushed, edge='rising')
		bluePenaltyHandler.start()

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
		(self.thisFighter, self.thisValue)  = self.decodeJudgeSignal(decodeBinary(buttonBits))# Read from GPIO to decode signal
		self.thisJudge = 0
		self.thisTime = datetime.datetime.now()
		self.judgeTrigger()

	def judge1Signal(self,callback):
		buttonBits = [self.gpioRead(pin) for pin in self.judge1Pins]
		(self.thisFighter, self.thisValue)  = self.decodeJudgeSignal(decodeBinary(buttonBits))# Read from GPIO to decode signal
		self.thisJudge = 1
		self.thisTime = datetime.datetime.now()
		self.judgeTrigger()

	def judge2Signal(self,callback):
		buttonBits = [self.gpioRead(pin) for pin in self.judge2Pins]
		(self.thisFighter, self.thisValue)  = self.decodeJudgeSignal(decodeBinary(buttonBits))# Read from GPIO to decode signal
		self.thisJudge = 2
		self.thisTime = datetime.datetime.now()
		self.judgeTrigger()

	def judgeTrigger(self):
		print('Judge Trigger called:')
		print('Judge: %i'%(self.thisJudge))
		print('Fighter: %i'%(self.thisFighter))
		print('Points: %i'%(self.thisValue))
		timeDelta = self.thisTime - self.lastTime
		if timeDelta.milliseconds < self.maxGapTime: # Log only trigger events within threshold
			if self.lastJudge != self.thisJudge: # Prevent double-tapping by the same judge (debounce)
				if self.lastFighter == self.thisFighter: # Only add scores if judeges trigger for the same competitor
					if self.lastValue == self.thisValue: # If the two judges trigger the same point value, use that value
						if self.lastPointCounted == False:
							self.pointDetected.emit(self.thisPerson,self.thisValue)
							self.lastPointCounted == True
						elif self.lastPointCounted == True:
							self.lastPointCounted == False

		self.lastValue = self.thisValue
		self.lastFighter = self.thisFighter
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
