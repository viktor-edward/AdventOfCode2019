class planet():
    def __init__(self, name: str, orbits: '__main__.planet'):
        self.name = name
        self.orbits = orbits

    def getOrbitCount(self) -> int:
        if self.orbits is not None:
            return self.orbits.getOrbitCount() + 1
        else:
            return 0

    def getVisitedPlanets(self, visitedSofar: list) -> list:
        if self.orbits is not None:
            visitedSofar.append(self.name)
            return self.orbits.getVisitedPlanets(visitedSofar)
        else:
            return visitedSofar

    def getStepsToPlanet(self, planetName: str) -> int:
        if self.name != planetName and self.orbits is not None:
            return self.orbits.getStepsToPlanet(planetName) + 1
        else:
            return -1


def readFile(fileInput: str) -> list:
    f = open(fileInput, 'r')
    data = []
    for line in f.readlines():
        data.append(line.replace("\n", "").split(")"))
    f.close()
    return data


def generateOrbitsData(inputData):
    orbitDataList = []
    for orbit in inputData:
        planet1 = getPlanet(orbitDataList, orbit[0])
        planet2 = getPlanet(orbitDataList, orbit[1])
        planet2.orbits = planet1
    return orbitDataList


def getPlanet(orbitDataList: list, name: str) -> '__main__.planet':
    planetFound = planetExists(orbitDataList, name)
    if planetFound is None:
        newPlanet = planet(name, None)
        orbitDataList.append(newPlanet)
        return newPlanet
    else:
        return planetFound


def planetExists(orbitDataList: list, name: str) -> '__main__.planet':
    for p in orbitDataList:
        if p.name == name:
            return p
    return None


def getNumberOfOrbits(orbitDataList: list) -> int:
    orbits = 0
    for p in orbitDataList:
        orbits += p.getOrbitCount()
    return orbits


def getFirstCommonPlanet(planet1: '__main__.planet', planet2: '__main__.planet') -> str:
    planet1Visited = planet1.getVisitedPlanets([])
    planet2Visited = planet2.getVisitedPlanets([])
    for p in planet1Visited:
        if p in planet2Visited:
            return p


def getStepsBetweenPlanets(planet1: '__main__.planet', planet2: '__main__.planet') -> str:
    firstCommonPlanet = getFirstCommonPlanet(planet1, planet2)
    stepsToCommonPlanet1 = planet1.getStepsToPlanet(firstCommonPlanet)
    stepsToCommonPlanet2 = planet2.getStepsToPlanet(firstCommonPlanet)
    return stepsToCommonPlanet1 + stepsToCommonPlanet2


def main():
    inputData = readFile("../resources/day6_input.txt")
    orbitDataList = generateOrbitsData(inputData)
    print("Part 1: ")
    print(getNumberOfOrbits(orbitDataList))

    print("Part 2: ")
    planet1 = getPlanet(orbitDataList, "YOU")
    planet2 = getPlanet(orbitDataList, "SAN")
    print(getStepsBetweenPlanets(planet1, planet2))


if __name__ == '__main__':
    main()
