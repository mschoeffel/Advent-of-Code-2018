import unittest
from Test.TestDay01 import TestDay1
from Test.TestDay02 import TestDay2


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestDay1('testDay01Part1'))
    suite.addTest(TestDay1('testDay01Part2'))
    suite.addTest(TestDay2('testDay02Part1'))
    suite.addTest(TestDay2('testDay02Part2'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
