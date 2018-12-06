#!/bin/env/python
# David Wright
# Copyright 2017
# Written for Python 3.5.2
"""A set of timers for round control and evaluation."""
# Timer.py
# import datetime
import time
# import traceback
# import sys
import threading


class TimerThread():
    """Simple egg timer that emits a signal each second until done."""

    def __init__(self, duration, interval=1):
        """Establish duration, end time, and break off new thread."""
        self._start_time = time.monotonic()
        self.end_time = self._start_time + duration
        # print("Starting timer with %i seconds" % (duration))
        self.interval = interval
        self.is_done = threading.Event()

    def start(self):
        """Start the first tick of the timer."""
        self._tick()

    def tick(self):
        """Emit output on timer tick."""

    def done(self):
        """Emit output when timer finishes."""

    def _tick(self):
        """Perform actions to make timer tick."""
        remaining = self.end_time - time.monotonic()
        next_interval = min(remaining, self.interval)
        next_fn = self._tick if remaining > self.interval else self._done
        timer = threading.Timer(next_interval, next_fn)
        timer.start()
        self.tick()

    def _done(self):
        """Perform actions to close timer thread."""
        self.is_done.set()
        self.done()

    def current_time(self):
        """Calculate current timer time remaining."""
        return time.monotonic() - self._start_time

    def wait_until_done(self, timeout=None):
        """Idle the thread when not in use."""
        self.is_done.wait(timeout=timeout)

    def terminate(self):
        """Clean up thread upon close."""
