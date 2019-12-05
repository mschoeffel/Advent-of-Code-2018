import unittest
from Test.TestDay1 import TestDay1


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestDay1('testDay1Part1'))
    suite.addTest(TestDay1('testDay1Part2'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
