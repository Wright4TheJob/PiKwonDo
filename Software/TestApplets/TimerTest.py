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
import sys

from PyQt5.QtWidgets import (QWidget, QTreeView, QMessageBox, QHBoxLayout,
                             QFileDialog, QLabel, QSlider, QCheckBox,
                             QLineEdit, QVBoxLayout, QApplication, QPushButton,
                             QTableWidget, QTableWidgetItem,QSizePolicy,
                             QGridLayout,QGroupBox, QMainWindow,QAction)
from PyQt5.QtCore import Qt, QTimer, QCoreApplication, QThread
from PyQt5 import QtCore, QtGui
from scipy import stats
from sympy import *
import numpy as np
import os
import cmath
import math
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import rcParams
import matplotlib.mlab as mlab
import csv

class App(QWidget):
    
    def __init__(self):
        super().__init__()
        self.title = 'Testing Timer Board'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 200
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        grid_layout = QGridLayout()

        self.labels = []
        self.statuses = []
        for i in range(0,5):
            label = QLabel("Button %i"%(i+1),self)
            label.setAlignment(Qt.AlignCenter)
            grid_layout.addWidget(label,0,i)
            status = QLabel("",self)
            status.setStyleSheet("background: red")
            grid_layout.addWidget(status,1,i)
            self.statuses.append(status)

        self.setLayout(grid_layout)
        self.show()

# TODO: Do I even want this? Periodic scanning would make this not work
class ButtonHandler(threading.Thread):
    '''Detects desired signal from GPIO pin and emits signal after debounce'''
    def __init__(self, pin, func, edge='both', bouncetime=100, glitchtime=5):
        super().__init__(daemon=True)

        self.edge = edge
        self.func = func
        self.pin = pin
        self.glitchtime = float(glitchtime)/1000
        self.lastpinval = GPIO.input(self.pin)
        self.glitchLock = threading.Lock()

        if (self.edge == 'rising'):
            gpioEdge = GPIO.RISING
        elif (self.edge == 'falling'):
            gpioEdge = GPIO.FALLING

        GPIO.add_event_detect(pin, gpioEdge,callback=self)

    def __call__(self, *args):
        if not self.glitchLock.acquire(blocking=False):
            return

        glitchTimer = threading.Timer(self.glitchtime, self.glitchDone, args=args)
        glitchTimer.start()

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
    bit_changed = pyqtSignal(float,object)

    def __init__(self):
        name = os.uname()
        if name[0] == "RPi":#TODO:Check sys names on python
            import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
            self.hasGPIO = True
        else:
            # disable GPIO pinging
            self.hasGPIO = False
        # specify pin connections (load, clock, data pin array)
        self.bitsToScan = 13
        self.scanPeriod = 5 # ms
        # cluster clock, step, and data pins
        self.j0_load_pin = -1
        self.j0_clk_pin = -1
        self.j0_dat_pin = -1

        self.j0_load_pin = -1
        self.j0_clk_pin = -1
        self.j0_dat_pin = -1

        self.j0_load_pin = -1
        self.j0_clk_pin = -1
        self.j0_dat_pin = -1

        # timer
        self.t_load_pin = -1
        self.t_clk_pin = -1
        self.t_dat_pin = -1

        self.load_pins = [self.j0_load_pin, self.j0_load_pin, self.j0_load_pin, self.t_load_pin]
        self.clock_pins = [self.j0_clk_pin, self.j0_clk_pin, self.j0_clk_pin, self.t_clk_pin]
        self.data_pins = [self.j0_dat_pin, self.j0_dat_pin, self.j0_dat_pin, self.t_dat_pin]

        [GPIO.setup(pin, GPIO.OUT) for pin in self.load_pins]
        [GPIO.setup(pin, GPIO.OUT) for pin in self.clock_pins]
        [GPIO.setup(pin, GPIO.IN) for pin in self.data_pins]

        self.periodicActionThread = PeriodicActionThread()
        periodicActionThread.init(self.step,self.scanPeriod)

        self.oldBits = []

    @property
    def pinChangeSignals(self):
        return self.pinChangeSignalArray

    def microsecond(self):
        time.sleep(0.001)

    def pulseGPIOPin(self,pin):
        GPIO.set(pin,HIGH)
        self.microsecond()
        GPIO.set(pin,LOW)

    def readBits(self):
        '''reads one bit from each controller'''
        result = []
        for pin in self.dataPins:
            result.append(GPIO.read(pin))
        return result

    def scanBits(self):
        '''reads all data from controllers'''
        result = []
        # send load signal
        self.pulseGPIOPin(self.loadPin)
        # Read bits from all controllers
        for i in range(0,self.bitsToScan):
            self.microsecond() # Wait for signals to stabilize
            result.append(self.readBits()) # Read a single bit from each of controllers
            self.pulseGPIOPin(self.shiftPin) # Shift data to next bit

        return zip(*result)

    def compareBits(self,olds,news):
        '''Subtracts 2D list to determine changes to bit state'''
        n = len(olds)
        m = len(olds[0])
        delta = [[0] * m for i in range(n)]
        for i in range(0,n):
            for j in range(0,m):
                delta[i][j] = news[i][j] - olds[i][j]
        return delta

    def is_nonzero(self,delta):
        '''Returns True if any element of 2D list is nonzero, otherwise False'''
        nonzero = False
        for row in delta:
            for element in row:
                if element != 0:
                    nonzero = True
        return nonzero

    def step(self):
        '''cycles bit scanning and detects changes'''
        newBits = self.scanBits()
        if len(self.oldBits) != 0:
            changes = self.compareBits(self.oldBits,newBits)
            changed = self.is_nonzero(changes)
            if changed:
                time = -1 # TODO: Get current system time, or from start of match/round
                self.bit_changed.emit(time,changes)
        self.oldBits = newBits

class BitDecoder():
    def __init__(self,piKwonDo):
        self.main_process = piKwonDo
        a = 13
        b = 4
        for i in range(0,a):
            for j in range(0,b):
                pass
        #[pin1,pin2,pin3...]
        #[bit1,bit1,bit1...]
        #[bit2,bit2,bit2...]
        #[bit3,bit3,bit3...]
        # where each element is a touple of rising and falling signals
        # or rising is 1, falling is -1, and
        self.pinChangeSignalArray = [[1,0,-1],[0,0,0]]

        connect(lambda: self.main_process.redPoint(1))

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

    # TODO: Replace this with more general interpretation method
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
