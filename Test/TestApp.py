import unittest
from Test.TestDay1 import TestDay1
from Test.TestDay2 import TestDay2


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestDay1('testDay1Part1'))
    suite.addTest(TestDay1('testDay1Part2'))
    suite.addTest(TestDay2('testDay2Part1'))
    suite.addTest(TestDay2('testDay2Part2'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
