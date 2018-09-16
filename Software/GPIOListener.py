#! /bin/env/python3
# David Wright
# Copyright 2017
# Written for Python 3.5.2
from PyQt5.QtCore import QThread
import PyQt5.QtCore as QtCore
import os

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

class PeriodicActionThread(threading.Thread):

    def __init__(self,function,period):
        self.function = function
        self.timer = threading.Timer(period,self.step)
        self.timer.start()
        self.lock = threading.Lock()

    def step(self):
        self.timer.start()
        if self.lock.acquire(blocking=False):
            self.function()
            self.lock.release()

class HardwareControllerScanner():
    pinChanged = pyqtSignal(int,int,bool)

    def __init__(self):
        name = os.uname()
        if name[0] == "RPi":#TODO:Check sys names on python
            import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
            self.hasGPIO = True
        else:
            # disable GPIO pinging
            self.hasGPIO = False
        # specify pin connections (load, clock, data pin array)
        self.bitsToScan = 10
        self.scanPeriod = 5 # ms
        GPIO.setup(self.judge0Pins[0], GPIO.IN)
        self.periodicActionThread = PeriodicActionThread()
        periodicActionThread.init(self.step,self.scanPeriod)

        self.oldBits = []

    def pinChangeSignals(self):
        return self.pinChangeSignalArray

    def microsecond(self):
        time.sleep(0.001)

    def pulseGPIOPin(self,pin):
        GPIO.set(pin,HIGH)
        self.microsecond()
        GPIO.set(pin,LOW)

    def readBits(self):
        result = []
        for pin in self.dataPins:
            result.append(GPIO.read(pin))
        return result

    def scanBits(self):
        result = []
        # send load signal
        self.pulseGPIOPin(self.loadPin)
        for i in range(0,bitCount-1):
            self.microsecond()
            result.append(self.readBits())
            self.pulseGPIOPin(self.shiftPin)

        return zip(*result)

    def compareBits(self,olds,news):
        for i in range(0,len(olds)):
            oldList = olds[i]
            for j in range(0,len(oldList)):
                change = news[i][j] - olds[i][j]
                if change == -1:
                    self.pinChanged.emit(i,j,False)
                elif change == 1:
                    self.pinChanged.emit(i,j,True)

    def step(self):
        newBits = self.scanBits()
        if len(self.oldBits) != 0:
            self.compareBits(self.oldBits,newBits)
        self.oldBits = newBits

class BitDecoder():
    for i in range():
        for j in range():

    #[pin1,pin2,pin3...]
    #[bit1,bit1,bit1...]
    #[bit2,bit2,bit2...]
    #[bit3,bit3,bit3...]
    # where each element is a touple of rising and falling signals
    self.pinChangeSignalArray = [[[signal.rising,signal.falling]]]

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


        # Compare results to last values, check for differences
        # If different, send

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
