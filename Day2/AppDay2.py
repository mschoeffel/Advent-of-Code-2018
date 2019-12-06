from Utils.CustomFileReader import readFileLinebyLineString


class Day2:

    @staticmethod
    def calcDiffOfIds(id1, id2):
        id1letters = [char for char in id1]
        id2letters = [char for char in id2]
        index = 0
        diff = 0
        for letter in id1letters:
            if letter != id2letters[index]:
                diff += 1
            index += 1
        return diff

    @staticmethod
    def eliminateDiff(id1, id2):
        id1letters = [char for char in id1]
        id2letters = [char for char in id2]
        index = 0
        cleaned = ""
        for letter in id1letters:
            if letter == id2letters[index]:
                cleaned = cleaned + letter
            index += 1
        return cleaned

    @staticmethod
    def day2part1(data):
        double = 0
        triple = 0

        for item in data:
            list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for letter in [char for char in item]:
                list[ord(letter) - 97] += 1
            doublecheck = True
            triplecheck = True
            for lettercount in list:
                if lettercount == 2 and doublecheck:
                    double += 1
                    doublecheck = False
                if lettercount == 3 and triplecheck:
                    triple += 1
                    triplecheck = False
        return double * triple

    @staticmethod
    def day2part2(data):
        mindiff = 0
        id = ""
        iddiff = ""

        for item in data:
            for comp in data:
                if comp == item:
                    break
                else:
                    difftemp = Day2.calcDiffOfIds(item, comp)
                    if difftemp < mindiff or mindiff == 0:
                        mindiff = difftemp
                        id = item
                        iddiff = comp
        return Day2.eliminateDiff(id, iddiff)

    @staticmethod
    def main():
        print("Result part one: " + str(Day2.day2part1(readFileLinebyLineString('./data.txt'))))
        print("Result part two: " + str(Day2.day2part2(readFileLinebyLineString('./data.txt'))))


if __name__ == '__main__':
    Day2.main()
