def readFile(fileInput):
    f = open(fileInput, 'r')
    data = f.read().split(',')
    f.close()
    data = [int(i) for i in data]
    return data


def updateOpcodes(listOfOpcodes):
    opcodesLength = len(listOfOpcodes)
    i = 0
    while i < opcodesLength:
        currentOpcode = listOfOpcodes[i]
        if not (currentOpcode == 1 or currentOpcode == 2):
            break
        toBeUpdated = listOfOpcodes[i + 3]
        pos1 = listOfOpcodes[i + 1]
        pos2 = listOfOpcodes[i + 2]
        if currentOpcode == 1:
            listOfOpcodes[toBeUpdated] = listOfOpcodes[pos1] + listOfOpcodes[pos2]
        elif currentOpcode == 2:
            listOfOpcodes[toBeUpdated] = listOfOpcodes[pos1] * listOfOpcodes[pos2]
        i += 4
    return listOfOpcodes

def main():
    listOfOpcodesOriginal = readFile("../resources/day2_input.txt")
    listOfOpcodes = listOfOpcodesOriginal.copy()

    print("Part 1:")
    listOfOpcodes[1] = 12
    listOfOpcodes[2] = 2
    updatedListOfOpcodes = updateOpcodes(listOfOpcodes)
    print(updatedListOfOpcodes[0])

    print("Part 2:")
    solutionFound = False
    solution = 19690720
    for i in range(100):
        for j in range(100):
            listOfOpcodes = listOfOpcodesOriginal.copy()
            listOfOpcodes[1] = i
            listOfOpcodes[2] = j
            updatedListOfOpcodes = updateOpcodes(listOfOpcodes)
            if updatedListOfOpcodes[0] == solution:
                print("Solution found: ")
                print("Noun: " + str(i))
                print("Verb: " + str(j))
                solutionFound = True
                break
        if solutionFound:
            break


if __name__ == '__main__':
    main()
