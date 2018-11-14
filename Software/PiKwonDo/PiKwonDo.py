#!/bin/env/python
# David Wright
# Copyright 2017
# Written for Python 3.7

# https://docs.python.org/3.7/library/queue.html

#Import
import sys
import datetime
import time
import os
import math
import csv
import Timer
import GPIOListener
from GUI import FrontEndController

class OutOfRangeError(ValueError):
    '''exeption raised when input or result is outside of specified bounds'''

class UnknownFighterError(ValueError):
    '''exeption raised when input or result is not a known fighter code'''

# Create match class
# Have game emit signal to indicate something changed
# Have GUI check game variables
# Program manager creates match and view controller instances, passes game to GUI, sets up hardware classes

# TODO: Blink timer LED when waiting for round to start? Require press of start button to begin each round, not just whole match

class PiKwonDo():
    def __init__(self,create_gui = True):
        self.programLoaded = False
        #super(self.__class__, self).__init__()

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

#        self.threadpool = QThreadPool()

        if create_gui == True:
            self.gui_controller = FrontEndController(self)

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
        #self.updateUI()

    def redPenalty(self):
        self.redPenalties += 1
        self.bluePoint(1)
        #self.updateUI()

    def bluePoint(self,pointValue):
        self.blueScore	+= pointValue
        #self.updateUI()

    def bluePenalty(self):
        self.bluePenalties += 1
        self.redPoint(1)
        #self.updateUI()

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
            #self.timerThread.timerTicked.connect(self.timerTicked)
            #self.timerThread.timerDone.connect(self.timerDone)
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
            #self.timerThread.timerTicked.connect(self.timerTicked)
            #self.timerThread.timerDone.connect(self.timerDone)
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
        #self.updateUI()
        self.timerRunning = False
        self.matchRunning = False

    def timerTicked(self,newTime):
        self.timeLeft = newTime
        #self.updateUI()

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

class Match():
    def __init__(self):
        print('Started new match!')
        self.redScore = 0
        self.blueScore = 0
        self.redPenalties = 0
        self.bluePenalties = 0
        self.currentSection = 1


def main():
    game_controller = PiKwonDo()

if __name__ == '__main__':
    main()
