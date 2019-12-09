import unittest
from Day01.AppDay01 import Day01
from Utils.CustomFileReader import readFileLinebyLineInt


class TestDay1(unittest.TestCase):

    def testDay01Part1(self):
        data = readFileLinebyLineInt('../Day01/changes.txt')
        expected = 510
        self.assertEqual(Day01.day1part1(data), expected, "Failed test Day 1 Part 1 Test 1")

        data = [1, -2, 3, +1]
        expected = 3
        self.assertEqual(Day01.day1part1(data), expected, "Failed test Day 1 Part 1 Test 2")

        data = [1, 1, 1]
        expected = 3
        self.assertEqual(Day01.day1part1(data), expected, "Failed test Day 1 Part 1 Test 3")

        data = [1, 1, -2]
        expected = 0
        self.assertEqual(Day01.day1part1(data), expected, "Failed test Day 1 Part 1 Test 4")

        data = [-1, -2, -3]
        expected = -6
        self.assertEqual(Day01.day1part1(data), expected, "Failed test Day 1 Part 1 Test 5")

    def testDay01Part2(self):
        data = readFileLinebyLineInt('../Day01/changes.txt')
        expected = 69074
        self.assertEqual(Day01.day1part2(data), expected, "Failed test Day 1 Part 2 Test 1")

        data = [1, -2, 3, 1]
        expected = 2
        self.assertEqual(Day01.day1part2(data), expected, "Failed test Day 1 Part 2 Test 2")

        data = [1, -1]
        expected = 1
        self.assertEqual(Day01.day1part2(data), expected, "Failed test Day 1 Part 2 Test 3")

        data = [3, 3, 4, -2, -4]
        expected = 10
        self.assertEqual(Day01.day1part2(data), expected, "Failed test Day 1 Part 2 Test 4")

        data = [-6, 3, 8, 5, -6]
        expected = 5
        self.assertEqual(Day01.day1part2(data), expected, "Failed test Day 1 Part 2 Test 5")

        data = [7, 7, -2, -7, -4]
        expected = 14
        self.assertEqual(Day01.day1part2(data), expected, "Failed test Day 1 Part 2 Test 6")


if __name__ == '__main__':
    unittest.main()
