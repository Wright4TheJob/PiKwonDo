import unittest
import PiKwonDo

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
			testMainWindow = PiKwonDo.MainWindow()
			self.assertRaises(PiKwonDo.UnknownFighterError,testMainWindow.penaltyDetected(badValue))

	def test_unknown_fighter_code_point(self):
		'''point function should fail with large input'''
		for badValue in self.badFighterValues:
			testMainWindow = PiKwonDo.MainWindow()
			self.assertRaises(PiKwonDo.UnknownFighterError,testMainWindow.pointDetected(badValue, 1))

if __name__ == '__main__':
	unittest.main()
