#!/bin/env/python
# David Wright
# Copyright 2018
# Written for Python 3.5.6
"""Create signals and threads to be used throughout the program."""


import threading
import queue


class Signal():
    '''a signal object to pass messages between classes using python queue'''
    def __init__(self):
        super().__init__()
        self.listeners = []

    def on_signal(self, func, thread):
        """Add a diad of function and thread to self.listeners"""

        self.listeners += [func, thread]

    def emit(self, *args):
        """Call all target functions on target threads from self.listeners"""
        for [func, thread] in self.listeners:
            thread.signal_queue.put(lambda: func(*args))


class SignalThread(threading.Thread):
    """Create queue and associated thread"""
    def __init__(self):
        super().__init__()
        self.signal_queue = queue.Queue()

    def run(self):
        while True:
            func = self.signal_queue.get()
            func()
