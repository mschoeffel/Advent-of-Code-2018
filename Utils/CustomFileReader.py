def readFileLinebyLineInt(filename):
    data = []
    with open(filename) as fp:
        line = fp.readline()
        while line:
            data.append(int(line.strip()))
            line = fp.readline()
    return data


def readFileLinebyLineString(filename):
    data = []
    with open(filename) as fp:
        line = fp.readline()
        while line:
            data.append(line.strip())
            line = fp.readline()
    return data

