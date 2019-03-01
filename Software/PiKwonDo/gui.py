#!/bin/env/python
# David Wright
# Copyright 2018
# Written for Python 3.7.0
"""Classes for front-end display and screen-based input."""
# imports
import datetime
import threading

from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QRect, pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QAction
from PyQt5.QtGui import QPainter, QColor, QFont

import match


class FrontEndController():
    """Central QT window manager for all GUI elements."""

    def __init__(self, main):
        """Create main window objects."""
        app = QApplication([])
        self.main_window = MainWindow(main)
        form = self.main_window
        form.show()
        app.exec_()

    def update_ui(self):
        """Redraw all elements of GUI that may change during use."""
        # replace with queue-based data passing
        # self.main_window.redScore = self.redScore
        # self.main_window.blueScore = self.blueScore
        # self.main_window.redPenalties = self.redPenalties
        # self.main_window.bluePenalties = self.bluePenalties
        # self.main_window.currentSection = self.currentSection
        # self.main_window.time = self.timeLeft
        self.main_window.update()

    def show(self):
        """Show the window."""
        self.main_window.show()


class MainWindow(QMainWindow):
    """Window for primary ringside display."""

    # pylint: disable=too-many-instance-attributes
    # Testing this supression

    def __init__(self, pkd):
        """Create main window elements."""
        self.program_loaded = False
        super().__init__()
        self.main_process = pkd
        self.match = match.Match()
        self.time = 90
        self.penalty_bar_height = 50
        self.time_height = 100

        # GUI sizing parameters
        self.blue_penalty_text = ''
        self.red_penalty_text = ''
        self.height = None
        self.time_string = ''
        self.width = None
        self.centralwidget = None
        self.setup_ui(self)

        self.program_loaded = True

    def setup_ui(self, window):
        """Initialize the main GUI elements."""
        window.setObjectName("MainWindow")
        window.resize(1000, 800)
        # MainWindow.showFullScreen()

        self.centralwidget = QWidget(window)
        self.centralwidget.setObjectName("centralwidget")

        self.width = window.frameGeometry().width()
        self.height = window.frameGeometry().height()

        self.setWindowTitle('PiKwonDo')
        self.activateWindow()
        self.raise_()
        self.show()
        window.setCentralWidget(self.centralwidget)

        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu('&File')

        exit_action = QAction('&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(self.close)  # This is built in
        file_menu.addAction(exit_action)

        round_menu = menu_bar.addMenu('&Match')
        start_action = QAction('&Start Match', self)
        # bluePointAction.setStatusTip('Exit application')
        start_action.triggered.connect(self.main_process.start_match)
        # This is built in
        round_menu.addAction(start_action)

        pause_action = QAction('&Pause Match', self)
        # pauseAction.setStatusTip('Exit application')
        pause_action.triggered.connect(self.main_process.pause_round)
        # This is built in
        round_menu.addAction(pause_action)

        resume_action = QAction('&Resume Match', self)
        # bluePointAction.setStatusTip('Exit application')
        resume_action.triggered.connect(self.main_process.resume_round)
        # This is built in
        round_menu.addAction(resume_action)

        reset_action = QAction('&Reset Match', self)
        # bluePointAction.setStatusTip('Exit application')
        reset_action.triggered.connect(self.main_process.reset_round)
        round_menu.addAction(reset_action)

        red_menu = menu_bar.addMenu('&Red')

        red_point_action = QAction('&Point', self)
        red_point_action.setShortcut('r')
        # bluePointAction.setStatusTip('Exit application')
        red_point_action.triggered.connect(
            lambda: self.main_process.red_point(1))
        red_menu.addAction(red_point_action)

        red_penalty_action = QAction('&Penalty', self)
        # redPenaltyAction.setShortcut('')
        # bluePointAction.setStatusTip('Exit application')
        red_penalty_action.triggered.connect(self.main_process.red_penalty)
        red_menu.addAction(red_penalty_action)

        blue_menu = menu_bar.addMenu('&Blue')
        blue_point_action = QAction('&Point', self)
        blue_point_action.setShortcut('b')
        # bluePointAction.setStatusTip('Exit application')
        blue_point_action.triggered.connect(
            lambda: self.main_process.blue_point(1))
        blue_menu.addAction(blue_point_action)

        blue_penalty_action = QAction('&Penalty', self)
        # redPenaltyAction.setShortcut('')
        # bluePointAction.setStatusTip('Exit application')
        blue_penalty_action.triggered.connect(self.main_process.blue_penalty)
        blue_menu.addAction(blue_penalty_action)

        QtCore.QMetaObject.connectSlotsByName(window)

    def paint_event(self):
        """Draw all necessary elements when update is needed."""
        q_paint = QPainter()
        q_paint.begin(self)
        self.draw_background(q_paint)
        self.draw_scores(q_paint)
        self.draw_penalties(q_paint)
        self.draw_time(q_paint)
        q_paint.end()

    def draw_background(self, q_paint):
        """Draw the colored boxes of the screen background."""
        col = QColor(0, 0, 0, 1)
        col.setNamedColor('#d4d4d4')
        q_paint.setPen(Qt.NoPen)

        q_paint.setBrush(QColor(255, 0, 0))
        q_paint.drawRect(0, 0, self.width/2, self.height+1)

        q_paint.setBrush(QColor(0, 0, 255))
        q_paint.drawRect(self.width/2, 0, self.width/2+2, self.height+1)

        # Penalty bar
        q_paint.setBrush(QColor(0, 0, 0, 100))
        q_paint.drawRect(0, 0, self.width, self.penaltyBarHeight)

        # Time box
        q_paint.setBrush(QColor(0, 0, 0, 255))
        q_paint.drawRect(
            self.width/4, self.penaltyBarHeight, self.width/2,
            self.timeHeight)

    def draw_scores(self, q_paint):
        """Draw the current scores on the screen."""
        q_paint.setPen(QColor(255, 255, 255))
        q_paint.setFont(QFont('Decorative', self.width/4))
        q_paint.drawText(
            QRect(0, 0, self.width/2, self.height),
            Qt.AlignCenter, str(int(self.match.red_score)))
        q_paint.drawText(
            QRect(self.width/2, 0, self.width/2+2, self.height),
            Qt.AlignCenter, str(int(self.match.blue_score)))

    def draw_penalties(self, q_paint):
        """Draw the penalties scores on the screen."""
        offset = 10
        if self.match.red_penalties >= 10:
            self.red_penalty_text = "Disqualified"
        else:
            self.red_penalty_text = "Penalties: "
            for _ in range(0, self.match.red_penalties):
                self.red_penalty_text += "X"
        if self.match.blue_penalties >= 10:
            self.blue_penalty_text = "Disqualified"
        else:
            self.blue_penalty_text = "Penalties: "
            for _ in range(0, self.match.blue_penalties):
                self.blue_penalty_text += "X"

        q_paint.setPen(QColor(255, 255, 255))
        q_paint.setFont(QFont('Decorative', 20))
        q_paint.drawText(
            QRect(offset, 0, self.width/2, self.penaltyBarHeight),
            (Qt.AlignLeft | Qt.AlignVCenter), self.redPenaltyText)
        q_paint.drawText(
            QRect(self.width/2+offset, 0, self.width/2, self.penaltyBarHeight),
            (Qt.AlignLeft | Qt.AlignVCenter), self.bluePenaltyText)

    def draw_time(self, q_paint):
        """Draw the current scores on the screen."""
        self.time_string = str(datetime.timedelta(seconds=self.time))
        self.time_string = ':'.join(str(self.time_string).split(':')[1:])
        self.time_string = self.time_string[1:]
        q_paint.setPen(QColor(255, 255, 255))
        q_paint.setFont(QFont('Decorative', int(self.time_height*3/4)))
        q_paint.drawText(
            QRect(
                self.width/4, self.penalty_bar_height,
                self.width/2, self.time_height),
            Qt.AlignCenter, self.time_string)

    def resize_event(self, event):
        """Resize elements to scale appropriately with window."""
        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.update()
        QMainWindow.resizeEvent(self, event)


class LatestValueBoxIOQT():
    """A container which holds only the most recent object put in it.

    The container provides threadsafe object storage and retrieval. Object get
    and place functions are pure python. The container instance emits a qt
    signal when a new object is placed in the container.
    """

    qt_signal = pyqtSignal()

    def __init__(self, value=None):
        """Create threading lock and initialize values."""
        self.lock = threading.Lock()
        self._value = value
        self.pending = False

    def put(self, value):
        """Place an object in the container.

        :param value: Object to place in the container.

        """
        self.lock.acquire()
        self._value = value
        if not self.pending:
            self.qt_signal.emit()
            self.pending = True
        self.lock.release()

    def get(self):
        """Retrieve the latest object from the container.

        :returns: The object placed in the container.

        """
        self.lock.acquire()
        value = self._value
        self.pending = False
        self.lock.release()
        return value
