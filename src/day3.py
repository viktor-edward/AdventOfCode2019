def readFile(fileInput):
    f = open(fileInput, 'r')
    data = []
    for line in f.readlines():
        data.append(line.rstrip('\n').split(','))
    f.close()
    return data[0], data[1]


def generateNextCoordinate(currentCoordinate, direction, steps):
    if direction == "U":
        return currentCoordinate[0], currentCoordinate[1] + steps
    elif direction == "D":
        return currentCoordinate[0], currentCoordinate[1] - steps
    elif direction == "L":
        return currentCoordinate[0] - steps, currentCoordinate[1]
    elif direction == "R":
        return currentCoordinate[0] + steps, currentCoordinate[1]
    else:
        print("Error: incorrect direction " + direction)


def generatePath(visitedCoords, currentCoordinate, direction, steps):
    curX = currentCoordinate[0]
    curY = currentCoordinate[1]
    for i in range(steps):
        newX = curX
        newY = curY
        if direction == "U":
            newY += 1
        elif direction == "D":
            newY -= 1
        elif direction == "L":
            newX -= 1
        elif direction == "R":
            newX += 1
        visitedCoords.add((newX, newY))
        curX = newX
        curY = newY


def generateVisitedCoords(path):
    visitedCoords = set()
    currentCoordinate = (0, 0)
    for step in path:
        direction = step[0]
        steps = abs(int(step[1:]))
        nextCoordinate = generateNextCoordinate(currentCoordinate, direction, steps)
        visitedCoords.add(generatePath(visitedCoords, currentCoordinate, direction, steps))
        currentCoordinate = nextCoordinate
    return visitedCoords


def stepsToNextCoordinate(currentCoordinate, coordinate, direction, steps):
    curX = currentCoordinate[0]
    curY = currentCoordinate[1]
    coordinateFound = False
    i = 0
    for i in range(steps):
        newX = curX
        newY = curY
        if direction == "U":
            newY += 1
        elif direction == "D":
            newY -= 1
        elif direction == "L":
            newX -= 1
        elif direction == "R":
            newX += 1
        curX = newX
        curY = newY
        if newX == coordinate[0] and newY == coordinate[1]:
            coordinateFound = True
            break
    return i+1, coordinateFound


def stepsToCoordinate(path, coordinate):
    stepsToCoordinate = 0
    coordinateFound = False
    currentCoordinate = (0, 0)
    for step in path:
        direction = step[0]
        steps = abs(int(step[1:]))
        nextCoordinate = generateNextCoordinate(currentCoordinate, direction, steps)
        stepsToAdd, coordinateFound = stepsToNextCoordinate(currentCoordinate, coordinate, direction, steps)
        stepsToCoordinate += stepsToAdd
        currentCoordinate = nextCoordinate
        if coordinateFound:
            break
    return stepsToCoordinate


def manhattanDistance(coordinate):
    return str(abs(coordinate[0]) + abs(coordinate[1]))


def main():
    path1, path2 = readFile("../resources/day3_input.txt")
    visitedCoords1 = generateVisitedCoords(path1)
    visitedCoords2 = generateVisitedCoords(path2)

    intersection = visitedCoords1.intersection(visitedCoords2)

    for p in intersection:
        if p is not None:
            print("Coordinate: " + str(p))
            print(manhattanDistance(p))
            stepp1 = stepsToCoordinate(path1, p)
            stepp2 = stepsToCoordinate(path2, p)
            print("Steps to Coordinate for path 1: " + str(stepp1))
            print("Steps to Coordinate for path 2: " + str(stepp2))
            print("Total steps: " + str(stepp1 + stepp2))
            print()


if __name__ == '__main__':
    main()
