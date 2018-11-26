#!/bin/env/python
# David Wright
# Copyright 2018
# Written for Python 3.7.0

# imports
from PyQt5 import QtCore
from PyQt5.QtCore import QThreadPool, Qt, QTimer, QCoreApplication, QThread, QRect, pyqtSignal
from PyQt5.QtWidgets import (QWidget, QFileDialog, QApplication,QMainWindow,QAction)
from PyQt5.QtGui import QPainter, QColor, QFont
import datetime
import threading

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class FrontEndController():
    def __init__(self,main):
        app = QApplication([])
        self.main_window = MainWindow(main)
        form = self.main_window
        form.show()
        app.exec_()

    def updateUI(self):
        # replace with queue-based data passing
        self.main_window.redScore = self.redScore
        self.main_window.blueScore = self.blueScore
        self.main_window.redPenalties = self.redPenalties
        self.main_window.bluePenalties = self.bluePenalties
        self.main_window.currentSection = self.currentSection
        self.main_window.time = self.timeLeft
        self.main_window.update()

    def show(self):
        self.main_window.show()

class MainWindow(QMainWindow):
    def __init__(self,piKwonDo):
        self.programLoaded = False
        super(self.__class__, self).__init__()
        self.mainProcess = piKwonDo
        self.redScore = 0
        self.blueScore = 0
        self.redPenalties = 0
        self.bluePenalties = 0
        self.currentSection = 0
        self.time = 90
        self.penaltyBarHeight = 50
        self.timeHeight = 100

        self.current_match = None

        self.setupUI(self)

        self.programLoaded = True

    def setupUI(self, window):
        #Builds GUI
        window.setObjectName(_fromUtf8("MainWindow"))
        window.resize(1000, 800)
        #MainWindow.showFullScreen()

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.width = window.frameGeometry().width()
        self.height = window.frameGeometry().height()

        self.setWindowTitle('PiKwonDo')
        self.activateWindow()
        self.raise_()
        self.show()
        window.setCentralWidget(self.centralwidget)

        menuBar = self.menuBar()

        file_menu = menuBar.addMenu('&File')

        exit_action = QAction('&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(self.close) #This is built in
        file_menu.addAction(exit_action)

        round_menu = menuBar.addMenu('&Match')
        startAction = QAction('&Start Match', self)
        #bluePointAction.setStatusTip('Exit application')
        startAction.triggered.connect(self.mainProcess.startMatch) #This is built in
        round_menu.addAction(startAction)

        pauseAction = QAction('&Pause Match', self)
        #pauseAction.setStatusTip('Exit application')
        pauseAction.triggered.connect(self.mainProcess.pauseRound) #This is built in
        round_menu.addAction(pauseAction)

        resumeAction = QAction('&Resume Match', self)
        #bluePointAction.setStatusTip('Exit application')
        resumeAction.triggered.connect(self.mainProcess.resumeRound) #This is built in
        round_menu.addAction(resumeAction)

        resetAction = QAction('&Reset Match', self)
        #bluePointAction.setStatusTip('Exit application')
        resetAction.triggered.connect(self.mainProcess.resetRound)
        round_menu.addAction(resetAction)


        red_menu = menuBar.addMenu('&Red')

        redPointAction = QAction('&Point', self)
        redPointAction.setShortcut('r')
        #bluePointAction.setStatusTip('Exit application')
        redPointAction.triggered.connect(lambda: self.mainProcess.redPoint(1))
        red_menu.addAction(redPointAction)

        redPenaltyAction = QAction('&Penalty',self)
        #redPenaltyAction.setShortcut('')
        #bluePointAction.setStatusTip('Exit application')
        redPenaltyAction.triggered.connect(self.mainProcess.redPenalty)
        red_menu.addAction(redPenaltyAction)

        blue_menu = menuBar.addMenu('&Blue')
        bluePointAction = QAction('&Point', self)
        bluePointAction.setShortcut('b')
        #bluePointAction.setStatusTip('Exit application')
        bluePointAction.triggered.connect(lambda: self.mainProcess.bluePoint(1))
        blue_menu.addAction(bluePointAction)

        bluePenaltyAction = QAction('&Penalty',self)
        #redPenaltyAction.setShortcut('')
        #bluePointAction.setStatusTip('Exit application')
        bluePenaltyAction.triggered.connect(self.mainProcess.bluePenalty)
        blue_menu.addAction(bluePenaltyAction)

        QtCore.QMetaObject.connectSlotsByName(window)

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawBackground(qp)
        self.drawScores(e,qp)
        self.drawPenalties(e,qp)
        self.drawTime(e,qp)
        qp.end()

    def drawBackground(self, qp):
        col = QColor(0, 0, 0, 1)
        col.setNamedColor('#d4d4d4')
        qp.setPen(Qt.NoPen)

        qp.setBrush(QColor(255, 0, 0))
        qp.drawRect(0, 0, self.width/2, self.height+1)

        qp.setBrush(QColor(0, 0, 255))
        qp.drawRect(self.width/2, 0, self.width/2+2, self.height+1)

        # Penalty bar
        qp.setBrush(QColor(0, 0, 0,100))
        qp.drawRect(0, 0, self.width, self.penaltyBarHeight)

        # Time box
        qp.setBrush(QColor(0, 0, 0, 255))
        qp.drawRect(self.width/4, self.penaltyBarHeight, self.width/2, self.timeHeight)

    def drawScores(self, event, qp):
        qp.setPen(QColor(255, 255, 255))
        qp.setFont(QFont('Decorative', self.width/4))
        qp.drawText(QRect(0, 0, self.width/2, self.height), Qt.AlignCenter, str(int(self.redScore)))
        qp.drawText(QRect(self.width/2, 0, self.width/2+2, self.height), Qt.AlignCenter, str(int(self.blueScore)))

    def drawPenalties(self,event,qp):
        offset = 10
        if self.redPenalties >= 10:
            self.redPenaltyText = "Disqualified"
        else:
            self.redPenaltyText = "Penalties: "
            for i in range(0,self.redPenalties):
                self.redPenaltyText += "X"
        if self.bluePenalties >= 10:
            self.bluePenaltyText = "Disqualified"
        else:
            self.bluePenaltyText = "Penalties: "
            for i in range(0,self.bluePenalties):
                self.bluePenaltyText += "X"

        qp.setPen(QColor(255, 255, 255))
        qp.setFont(QFont('Decorative', 20))
        qp.drawText(QRect(offset, 0, self.width/2, self.penaltyBarHeight), (Qt.AlignLeft | Qt.AlignVCenter), self.redPenaltyText)
        qp.drawText(QRect(self.width/2+offset, 0, self.width/2, self.penaltyBarHeight), (Qt.AlignLeft | Qt.AlignVCenter), self.bluePenaltyText)

    def drawTime(self,event,qp):
        self.timeString = str(datetime.timedelta(seconds=self.time))
        self.timeString = ':'.join(str(self.timeString ).split(':')[1:])
        self.timeString = self.timeString[1:]
        qp.setPen(QColor(255, 255, 255))
        qp.setFont(QFont('Decorative', int(self.timeHeight*3/4)))
        qp.drawText(QRect(self.width/4, self.penaltyBarHeight, self.width/2, self.timeHeight), Qt.AlignCenter, self.timeString)

    #def load_data(self):
        #Write this function
    #    options = QFileDialog.Options()
    #    options |= QFileDialog.DontUseNativeDialog
    #    fileName, _ = QFileDialog.getOpenFileName(self,
    #        "QFileDialog.getOpenFileName()",
    #        "","All Files (*);;Text Files (*.txt)",
    #        options=options)
    #    if fileName:
    #        with open(fileName, 'r') as fin:
    #            print('Reading file')
    #        self.redrawInputTables()
    #        self.graph_canvas.plotTruss(self.initialNodeArray,self.initialBeamArray)

    def resizeEvent(self, event):
        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.update()
        QMainWindow.resizeEvent(self, event)

class LatestValueBoxIOQT():
    '''A container which holds only the most recent object put in it.

    The container provides threadsafe object storage and retrieval. Object get
    and place functions are pure python. The container instance emits a qt
    signal when a new object is placed in the container.
    '''
    qt_signal = pyqtSignal()

    def __init__(value=None):
        self.lock = threading.Lock()
        self._value = value
        self._pending = False

    def put(self, value):
        '''Place an object in the container.

        :param value: Object to place in the container.

        '''

        self.lock.acquire()
        self._value = value
        if not self._pending:
            self.qt_signal.emit()
            self._pending = True
        self.lock.release()

    def get(self):
        '''Retrieve the latest object from the container.

        :returns: The object placed in the container.

        '''

        self.lock.acquire()
        value = self._value
        self._pending = False
        self.lock.release()
        return value
