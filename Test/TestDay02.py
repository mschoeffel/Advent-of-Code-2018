import unittest
from Day02.AppDay02 import Day02
from Utils.CustomFileReader import readFileLinebyLineString


class TestDay2(unittest.TestCase):

    def testDay02Part1(self):
        data = readFileLinebyLineString('../Day02/data.txt')
        expected = 6000
        self.assertEqual(Day02.day2part1(data), expected, "Failed test Day 2 Part 1 Test 1")

        data = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]
        expected = 12
        self.assertEqual(Day02.day2part1(data), expected, "Failed test Day 2 Part 1 Test 2")

    def testDay02Part2(self):
        data = readFileLinebyLineString('../Day02/data.txt')
        expected = "pbykrmjmizwhxlqnasfgtycdv"
        self.assertEqual(Day02.day2part2(data), expected, "Failed test Day 2 Part 2 Test 1")

        data = ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]
        expected = "fgij"
        self.assertEqual(Day02.day2part2(data), expected, "Failed test Day 2 Part 2 Test 2")


if __name__ == '__main__':
    unittest.main()
