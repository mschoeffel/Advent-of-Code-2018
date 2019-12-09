from Utils.CustomFileReader import readFileLinebyLineInt


class Day01:

    @staticmethod
    def day1part1(data):
        result = 0
        for item in data:
            result += item
        return result

    @staticmethod
    def day1part2(data):
        frequency = 0
        visited = []
        while True:
            for item in data:
                frequency += item
                if visited.__contains__(frequency):
                    return frequency
                else:
                    visited.append(frequency)

    @staticmethod
    def main():
        print("Day 1: Result part one: " + str(Day01.day1part1(readFileLinebyLineInt('./changes.txt'))))
        print("Day 1: Result part two: " + str(Day01.day1part2(readFileLinebyLineInt('./changes.txt'))))


if __name__ == '__main__':
    Day01.main()
