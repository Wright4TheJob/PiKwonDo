#!/bin/env/python
# David Wright
# Copyright 2017
# Written for Python 3.7

"""Primary game logic for PiKwonDo."""

# https://docs.python.org/3.7/library/queue.html

# Import
import time

import pkd_timer
# import GPIOListener
from gui import FrontEndController


class OutOfRangeError(ValueError):
    """Exeption raised when input or result is outside of specified bounds."""


class UnknownFighterError(ValueError):
    """Exeption raised when input or result is not a known fighter code."""

# Create match class
# Have game emit signal to indicate something changed
# Have GUI check game variables
# Program manager creates match and view controller instances, passes game to
# GUI, sets up hardware classes

# TODO: Blink timer LED when waiting for round to start? Require press of start
# button to begin each round, not just whole match


class PiKwonDo():
    """Primary game logic."""

    def __init__(self, create_gui=True):
        """Initialize variables and create game instance."""
        self.program_loaded = False
        # super(self.__class__, self).__init__()

        # Settings
        self.round_length = 90  # seconds
        self.time_left = self.round_length
        self.round_quantity = 2
        self.break_length = 30  # seconds
        self.max_gap_time = 1000  # ms
        # Initialize variables
        self.red_score = 0
        self.blue_score = 0
        self.red_penalties = 0
        self.blue_penalties = 0
        self.current_section = 1
        self.match_running = False
        self.timer_running = False
        self.section_durations = [self.round_length]
        for _ in range(0, self.round_quantity-1):
            self.section_durations.append(self.break_length)
            self.section_durations.append(self.round_length)
        self.sections = len(self.section_durations)

        self.timer_thread = None

        if create_gui is True:
            self.gui_controller = FrontEndController(self)

        self.program_loaded = True

    def point_detected(self, person, point_value):
        """Respond to a point detected for a player."""
        if person == 0:
            self.red_point(point_value)
        elif person == 1:
            self.blue_point(point_value)
        else:
            raise UnknownFighterError(
                'code %i is not recognized in pointDetected' % (person))

    def penalty_detected(self, person):
        """Respond to a penalty detected for a player."""
        if person == 0:
            self.red_penalty()
        elif person == 1:
            self.blue_penalty()
        else:
            raise UnknownFighterError(
                'fighter code %i is not recognized penaltyDetected' % (person))

    def red_point(self, point_value):
        """Assign points to red player."""
        self.red_score += point_value
        # self.updateUI()

    def red_penalty(self):
        """Assign penalty to red player, and add a point to blue."""
        self.red_penalties += 1
        self.blue_point(1)
        # self.updateUI()

    def blue_point(self, point_value):
        """Assign points to blue player."""
        self.blue_score += point_value
        # self.updateUI()

    def blue_penalty(self):
        """Assign penalty to blue player, and add a point to red."""
        self.blue_penalties += 1
        self.red_point(1)
        # self.updateUI()

    def start_match(self):
        """Begin match timer and round tracking."""
        if self.match_running is False:
            self.current_section = 1
            self.start_round()
        else:
            self.resume_round()

    def start_round(self):
        """Begin round timer and incremement round."""
        if self.timer_running is False:
            # Timer Thread
            self.timer_thread = pkd_timer.TimerThread(
                self.section_durations[self.current_section-1])
            # Connect to emitted signals
            # self.timerThread.timerTicked.connect(self.timerTicked)
            # self.timerThread.timerDone.connect(self.timerDone)
            # Start the thread
            self.timer_thread.start()
        self.match_running = True
        self.timer_running = True

    def pause_round(self):
        """Save current time on round timer and terminate timer thread."""
        if self.timer_running is True:
            self.timer_thread.terminate()
        self.timer_running = False

    def resume_round(self):
        """Initialize new timer with remaining time."""
        if self.timer_running is False:
            self.timer_thread = pkd_timer.TimerThread(self.time_left)
            # Connect to emitted signals
            # self.timerThread.timerTicked.connect(self.timerTicked)
            # self.timerThread.timerDone.connect(self.timerDone)
            self.timer_thread.start()
        self.timer_running = True

    def reset_round(self):
        """Set points, penalties, and time to zero."""
        self.red_score = 0
        self.blue_score = 0
        self.red_penalties = 0
        self.blue_penalties = 0
        self.current_section = 1
        self.time_left = self.round_length
        if self.timer_running is True:
            self.timer_thread.terminate()
        # self.updateUI()
        self.timer_running = False
        self.match_running = False

    def timer_ticked(self, new_time):
        """Save new time to match."""
        self.time_left = new_time
        # self.updateUI()

    def timer_done(self):
        """Respond to timer reading end, either end match or round."""
        # self.timerThread.terminate()
        self.timer_running = False
        self.time_left = 0
        # self.update()
        time.sleep(1)
        if self.current_section < self.sections:
            self.current_section += 1
            # TODO:Wait for manual trigger for start of next section?
            self.start_round()
        elif self.current_section == self.sections:
            self.match_running = False
        else:
            raise OutOfRangeError(
                'number is out of range (must be less than 10)')


class Match():
    """A particular match driven by the rules of TaeKwonDo."""

    def __init__(self):
        """Begin a new match."""
        print('Started new match!')
        self.red_score = 0
        self.blue_score = 0
        self.red_penalties = 0
        self.blue_penalties = 0
        self.current_section = 1


def main():
    """Inializes game."""
    PiKwonDo()


if __name__ == '__main__':
    main()
