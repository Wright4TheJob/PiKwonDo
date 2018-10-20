import unittest
import PiKwonDo as pkd
import Timer
from PyQt5.QtWidgets import QApplication
import sys
import time
import threading
#class KnownValues(unittest.TestCase):
    #self.fighterValues = ((0,1),(1,4))

    #def test_square_known_values(self):
    #	'''Square Integers should return known values with known inputs'''
    #	for integer, knownValue in self.fighterValues:
    #		result = PiKwonDo.MainWindow.penaltyDetected(integer)
    #		self.assertEqual(knownValue,result)

    #def test_parabola_results(self):
    #	'''parabola should return known results'''
    #	result = MainProgram.valueOfParabola([0,0,0],1)
    #	self.assertEqual(0,result)

class BadInput(unittest.TestCase):
    badFighterValues = (-1,2,10)

    def test_unknown_fighter_code_penalty(self):
        '''penalty function should fail with bad fighter input'''
        for badValue in self.badFighterValues:
            main = pkd.PiKwonDo(create_gui = False)
            with self.assertRaises(pkd.UnknownFighterError):
                main.penaltyDetected(badValue)

    def test_unknown_fighter_code_point(self):
        '''point function should fail with invalid fighter input'''
        for badValue in self.badFighterValues:
            main = pkd.PiKwonDo(create_gui = False)
            with self.assertRaises(pkd.UnknownFighterError):
                main.pointDetected(badValue,1)

class TickingTimer(unittest.TestCase):
    def test_known_duration(self):
        print('test_known_duration')
        test_timer = Timer.TimerThread(0.1,interval = 0.01)
        test_timer.start()

    def test_return_time(self):
        print('test_return_time')
        time_before = time.monotonic()
        test_timer = Timer.TimerThread(0.1,interval = 0.01)
        def on_tick():
            runtime = test_timer.current_time()
            time_after = time.monotonic()
            self.assertLessEqual(runtime,time_after-time_before)
        test_timer.tick = on_tick
        test_timer.start()
        test_timer.wait_until_done()

    def test_calls_done(self):
        print('test_calls_done')
        is_done = threading.Event()
        timer = Timer.TimerThread(0.1,interval = 0.01)
        def on_tick():
            self.assertFalse(is_done.is_set())
        def on_done():
            is_done.set()
        timer.tick = on_tick
        timer.done = on_done
        timer.start()
        timer.wait_until_done()
        self.assertTrue(is_done.wait(timeout=1))

if __name__ == '__main__':
    unittest.main()
