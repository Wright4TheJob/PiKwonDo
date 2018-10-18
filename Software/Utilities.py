#!/bin/env/python
# David Wright
# Copyright 2018
# Written for Python 3.7.0

import threading
import queue

class Signal():
    '''a signal object to pass messages between classes using python queue'''
    def __init__(self):
        self.listeners = []

    def on_signal(func,thread):
        self.listeners += [func,thread]

    def emit(*args):
        for [fn,thread] in self.listeners:
            thread.signal_queue.put(lambda: func(*args))

class SignalThread(threading.Thread):
    def __init__(self):
        self.signal_queue = Queue()

    def run(self):
        while True:
            f = self.signal_queue.get()
            f()
