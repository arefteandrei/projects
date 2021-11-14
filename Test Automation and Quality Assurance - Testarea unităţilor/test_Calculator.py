import unittest
from Calculator import Calculator

class testDivisionFromNumbers(unittest.TestCase):

    def test_result(self):
        calc = Calculator()
        result = calc.divisionFromNumbers(12, 4)
        expected = 3
        self.assertEqual(result, expected), "The result is not 3"

    def test_isZero(self):
        calc = Calculator()
        self.assertRaises(ZeroDivisionError, calc.divisionFromNumbers, 12, 0)

    def test_isString(self):
        calc = Calculator()
        self.assertRaises(TypeError, calc.divisionFromNumbers, 12, "c")

def suite():

    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(testDivisionFromNumbers))
    return test_suite


mySuite = suite()


runner = unittest.TextTestRunner()
runner.run(mySuite)