import unittest
from Validator import *


class testing(unittest.TestCase):
    validatorObj = Validator()

    def testOne(self):
        x, y, z = self.validatorObj.validateFunction("x^2")
        self.assertTrue(y, "x^2 is not a valid function")

    def testTwo(self):
        x, y, z = self.validatorObj.validateFunction("2x")
        self.assertTrue(y, "2x is not a valid function")

    def testThree(self):
        x, y, z = self.validatorObj.validateFunction("cos(x)+x^2")
        self.assertTrue(y, "cos(x)+x^2 is not a valid function")

    def testFour(self):
        x, y, z = self.validatorObj.validateFunction("x**2")
        self.assertTrue(y, "x**2 is not a valid function")

    def testFive(self):
        x, y = self.validatorObj.validateInputRange("-2", "2")
        self.assertTrue(x, "-2 is not less than 2")

    def testSix(self):
        x, y = self.validatorObj.validateInputRange("5", "2")
        self.assertTrue(x, "5 is not less than 2")

    def testSeven(self):
        x, y = self.validatorObj.validateInputRange("5+2", "7+9")
        self.assertTrue(x, "5+2 is not less than 7+9")

    def testEight(self):
        x, y = self.validatorObj.validateInputRange("5+2", "2+1")
        self.assertTrue(x, "5+2 is not less than 2+1")

    def testNine(self):
        x, y = self.validatorObj.validateInputRange("2*5", "5*5")
        self.assertTrue(x, "2*5 is not less than 5*5")

    def testTen(self):
        x, y = self.validatorObj.validateInputRange("3*4", "5*6")
        self.assertTrue(x, "3*4 is not less than 5*6")

if __name__ == "__main__":
    unittest.main()
