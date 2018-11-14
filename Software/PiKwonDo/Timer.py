#!/bin/env/python
# David Wright
# Copyright 2017
# Written for Python 3.5.2

# Timer.py
import datetime
import time
import traceback, sys
import threading

class TimerThread():

    def __init__(self, duration,interval = 1):
        self._start_time = time.monotonic()
        self.end_time = self._start_time + duration
        print("Starting timer with %i seconds"%(duration))
        self.interval = interval
        self.is_done = threading.Event()

    def start(self):
        self._tick()

    def tick(self):
        pass

    def done(self):
        pass

    def _tick(self):
        remaining = self.end_time - time.monotonic()
        nextInterval = min(remaining, self.interval)
        nextFn = self._tick if remaining > self.interval else self._done
        timer = threading.Timer(nextInterval, nextFn)
        timer.start()
        self.tick()

    def _done(self):
        self.is_done.set()
        self.done()

    def current_time(self):
        return time.monotonic() - self._start_time

    def wait_until_done(self,timeout=None):
        self.is_done.wait(timeout=timeout)
