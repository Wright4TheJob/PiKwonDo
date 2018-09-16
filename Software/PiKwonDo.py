#!/bin/env/python
# David Wright
# Copyright 2017
# Written for Python 3.6.3


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
import GPIOListener
from GUI import MainWindow

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class OutOfRangeError(ValueError):
    '''exeption raised when input or result is outside of specified bounds'''

class UnknownFighterError(ValueError):
    '''exeption raised when input or result is not a known fighter code'''

# Create game class
# Have game emit signal to indicate something changed
# Have GUI check game variables
# Program manager creates game and GUI instances, passes game to GUI, sets up hardware classes

class PiKwonDo():
    def __init__(self):
        self.programLoaded = False
        super(self.__class__, self).__init__()

        # Settings
        self.roundLength = 90 # seconds
        self.timeLeft = self.roundLength
        self.roundQuantity = 2
        self.breakLength = 30 # seconds
        self.maxGapTime = 200 #ms
        # Initialize variables
        self.redScore = 0
        self.blueScore = 0
        self.redPenalties = 0
        self.bluePenalties = 0
        self.currentSection = 1
        self.matchRunning = False
        self.timerRunning = False
        self.sectionDurations = [self.roundLength]
        for i in range(0,self.roundQuantity-1):
        	self.sectionDurations.append(self.breakLength)
        	self.sectionDurations.append(self.roundLength)
        self.sections = len(self.sectionDurations)

        self.threadpool = QThreadPool()

        """
        # Point Listener Thread
        self.gpioListenerThread = GPIOListener.GPIOListenerThread(self.maxGapTime)
        # Connect to emitted signals
        self.gpioListenerThread.pointDetected.connect(self.pointDetected)
        self.gpioListenerThread.penaltyDetected.connect(self.penaltyDetected)
        self.gpioListenerThread.startRoundDetected.connect(self.startMatch)
        self.gpioListenerThread.pauseRoundDetected.connect(self.pauseRound)
        self.gpioListenerThread.resetRoundDetected.connect(self.resetRound)
        # Start the thread
        self.gpioListenerThread.start()
        """
        self.mainWindow = MainWindow(self)

        self.programLoaded = True

    def pointDetected(self,person,pointValue):
        if person == 0:
            self.redPoint(pointValue)
        elif person == 1:
            self.bluePoint(pointValue)
        else:
            raise UnknownFighterError('fighter code %i is not recognized in pointDetected'%(person))

    def penaltyDetected(self,person):
        if person == 0:
            self.redPenalty()
        elif person == 1:
            self.bluePenalty()
        else:
            raise UnknownFighterError('fighter code %i is not recognized penaltyDetected'%(person))

    def redPoint(self,pointValue):
        self.redScore += pointValue
        self.updateUI()

    def redPenalty(self):
        self.redPenalties += 1
        self.bluePoint(1)
        self.updateUI()

    def bluePoint(self,pointValue):
        self.blueScore	+= pointValue
        self.updateUI()

    def bluePenalty(self):
        self.bluePenalties += 1
        self.redPoint(1)
        self.updateUI()

    def startMatch(self):
        if self.matchRunning == False:
            self.currentSection = 1
            self.startRound()
        else:
            self.resumeRound()

    def startRound(self):
        if self.timerRunning == False:
            # Timer Thread
            self.timerThread = Timer.TimerThread(self.sectionDurations[self.currentSection-1])
            # Connect to emitted signals
            self.timerThread.timerTicked.connect(self.timerTicked)
            self.timerThread.timerDone.connect(self.timerDone)
            # Start the thread
            self.timerThread.start()
        self.matchRunning = True
        self.timerRunning = True

    def pauseRound(self):
        if self.timerRunning == True:
            self.timerThread.terminate()
        self.timerRunning = False

    def resumeRound(self):
        if self.timerRunning == False:
            self.timerThread = Timer.TimerThread(self.timeLeft)
            # Connect to emitted signals
            self.timerThread.timerTicked.connect(self.timerTicked)
            self.timerThread.timerDone.connect(self.timerDone)
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
        self.updateUI()
        self.timerRunning = False
        self.matchRunning = False

    def timerTicked(self,newTime):
        self.timeLeft = newTime
        self.updateUI()

    def timerDone(self):
        #self.timerThread.terminate()
        self.timerRunning = False
        self.timeLeft = 0
        #self.update()
        time.sleep(1)
        if self.currentSection < self.sections:
            self.currentSection += 1
            # TODO:Wait for manual trigger for start of next section?
            self.startRound()
        elif self.currentSection == self.sections:
            self.matchRunning = False
        else:
            raise OutOfRangeError('number is out of range (must be less than 10)')

    def updateUI(self):
        self.mainWindow.redScore = self.redScore
        self.mainWindow.blueScore = self.blueScore
        self.mainWindow.redPenalties = self.redPenalties
        self.mainWindow.bluePenalties = self.bluePenalties
        self.mainWindow.currentSection = self.currentSection
        self.mainWindow.time = self.timeLeft
        self.mainWindow.update()

    def show(self):
        self.mainWindow.show()

def main():
    app = QApplication(sys.argv)
    form = PiKwonDo()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
