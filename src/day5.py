def readFile(fileInput: str) -> list:
    f = open(fileInput, 'r')
    data = f.read().split(',')
    f.close()
    data = [int(i) for i in data]
    return data


def getOpCodesAndParameters(opCode: int) -> tuple:
    opCodeStr = str(opCode)
    instr = int(opCodeStr[-2:])
    para1, para2, para3 = 0, 0, 0
    if len(opCodeStr) == 5:
        para1 = int(opCodeStr[2])
        para2 = int(opCodeStr[1])
        para3 = int(opCodeStr[0])
    elif len(opCodeStr) == 4:
        para1 = int(opCodeStr[1])
        para2 = int(opCodeStr[0])
    elif len(opCodeStr) == 3:
        para1 = int(opCodeStr[0])
    return instr, para1, para2, para3


def updateOpcodes(listOfOpcodes: list, inputCode: int) -> list:
    opcodesLength = len(listOfOpcodes)
    output = []
    i = 0
    while i < opcodesLength:
        currentOpcode, par1, par2, par3 = getOpCodesAndParameters(listOfOpcodes[i])
        if not (currentOpcode in (1, 2, 3, 4, 5, 6, 7, 8)):
            break

        if par1 == 0:
            pos1 = listOfOpcodes[i + 1]
        else:
            pos1 = i + 1
        if currentOpcode == 1 or currentOpcode == 2:
            if par2 == 0:
                pos2 = listOfOpcodes[i + 2]
            else:
                pos2 = i + 2

            if par3 == 0:
                toBeUpdated = listOfOpcodes[i + 3]
            else:
                toBeUpdated = i+3

            if currentOpcode == 1:
                listOfOpcodes[toBeUpdated] = listOfOpcodes[pos1] + listOfOpcodes[pos2]
            else:
                listOfOpcodes[toBeUpdated] = listOfOpcodes[pos1] * listOfOpcodes[pos2]
            i += 4
        elif currentOpcode == 3:
            listOfOpcodes[pos1] = inputCode
            i += 2
        elif currentOpcode == 4:
            output.append(listOfOpcodes[pos1])
            i += 2
        elif currentOpcode == 5:
            if listOfOpcodes[pos1] != 0:
                if par2 == 0:
                    pos2 = listOfOpcodes[i + 2]
                else:
                    pos2 = i + 2
                i = listOfOpcodes[pos2]
            else:
                i += 3
        elif currentOpcode == 6:
            if listOfOpcodes[pos1] == 0:
                if par2 == 0:
                    pos2 = listOfOpcodes[i + 2]
                else:
                    pos2 = i + 2
                i = listOfOpcodes[pos2]
            else:
                i += 3
        elif currentOpcode == 7:
            if par3 == 0:
                pos3 = listOfOpcodes[i + 3]
            else:
                pos3 = i + 3
            if par2 == 0:
                pos2 = listOfOpcodes[i + 2]
            else:
                pos2 = i + 2
            if listOfOpcodes[pos1] < listOfOpcodes[pos2]:
                listOfOpcodes[pos3] = 1
            else:
                listOfOpcodes[pos3] = 0
            i += 4
        elif currentOpcode == 8:
            if par3 == 0:
                pos3 = listOfOpcodes[i + 3]
            else:
                pos3 = i + 3
            if par2 == 0:
                pos2 = listOfOpcodes[i + 2]
            else:
                pos2 = i + 2
            if listOfOpcodes[pos1] == listOfOpcodes[pos2]:
                listOfOpcodes[pos3] = 1
            else:
                listOfOpcodes[pos3] = 0
            i += 4
    return output


def main():
    listOfOpcodesOriginal = readFile("../resources/day5_input.txt")
    listOfOpcodes = listOfOpcodesOriginal.copy()

    inputCode = 1
    print("Part 1:")
    output = updateOpcodes(listOfOpcodes, inputCode)
    print(output)

    inputCode = 5
    listOfOpcodes = listOfOpcodesOriginal.copy()

    #listOfOpcodes = [3,21,1007,21,8,20,1005,20,22,107,8,21,20,1006,20,31, 1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104, 999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

    #PROBABLY ERROR IN CODE, STRING ABOVE HAS NOT PASSED TEST FOR INPUT CODE = 8 and <8!

    print("Part 2:")
    output = updateOpcodes(listOfOpcodes, inputCode)
    print(output)


if __name__ == '__main__':
    main()
