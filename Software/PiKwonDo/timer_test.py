#! /bin/env/python3
# David Wright
# Copyright 2017
# Written for Python 3.5.6
"""Test the timer board and GPIO timing."""
import sys
import queue
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel
from PyQt5.QtCore import Qt
import gpio_scanner


class App(QWidget):
    """Create GUI visualization of timer board button status."""

    def __init__(self):
        """Start python application."""
        super().__init__()
        self.title = 'Testing Timer Board'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 200
        self.button_statuses = None
        self.init_ui()
        self.start_gpio_scan()
        self.dropbox = queue.Queue()
        gpio_scanner.PeriodicActionThread(self.read_queue, 1000)

    def init_ui(self):
        """Create GUI elements."""
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        grid_layout = QGridLayout()

        self.labels = []
        self.statuses = []
        for i in range(0, 5):
            label = QLabel("Button %i" % (i+1), self)
            label.setAlignment(Qt.AlignCenter)
            grid_layout.addWidget(label, 0, i)
            status = QLabel("", self)
            status.setStyleSheet("background: red")
            grid_layout.addWidget(status, 1, i)
            self.statuses.append(status)

        self.setLayout(grid_layout)
        self.show()

    def start_gpio_scan(self):
        """Begin hardware scanner routine."""
        self.scanner = gpio_scanner.HardwareControllerScanner()

    def read_queue(self):
        """Read the latest value from queue and react."""
        try:
            data = self.dropbox.get(block=False)
            self.button_statuses = [x[0] for x in data]
            self.update_ui()
        except queue.Empty:
            # print('Queue is empty, not redrawing')
            pass

    def update_ui(self):
        """Redraw the UI elements based on button status."""
        for label, value in zip(self.statuses, self.button_statuses):
            self.set_label_color(label, value)


def set_label_color(label, value):
    """Select label background color based on button status."""
    if value == 1:
        label.setStyleSheet('background: green')
    else:
        label.setStyleSheet('background: red')


if __name__ == '__main__':
    APP = QApplication(sys.argv)
    ex = App()
    sys.exit(APP.exec_())
