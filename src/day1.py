import math


def readFile(fileInput):
    f = open(fileInput, 'r')
    data = []
    for line in f.readlines():
        data.append(float(line))
    f.close()
    return data


def calculateFuelRequired(mass):
    return math.floor(mass/3) - 2


def calculateFuelRequiredRecursive(mass):
    fuelReqCurrent = calculateFuelRequired(mass)
    if fuelReqCurrent > 0:
        fuelReq = fuelReqCurrent + calculateFuelRequiredRecursive(fuelReqCurrent)
        return fuelReq
    else:
        return 0



def main():
    listOfMass = readFile("../resources/day1_input.txt")

    print("Part one: ")
    listOfFuelRequired = []
    for mass in listOfMass:
        listOfFuelRequired.append(calculateFuelRequired(mass))
    print(sum(listOfFuelRequired))

    print("Part two: ")
    listOfFuelRequiredRec = []
    for mass in listOfMass:
        listOfFuelRequiredRec.append(calculateFuelRequiredRecursive(mass))
    print(sum(listOfFuelRequiredRec))


if __name__ == '__main__':
    main()
