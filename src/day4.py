def verifyNumber(number):
    doubleCondition = False
    increasingCondition = True
    previous = str(number)[0]
    for n in str(number)[1:]:
        if int(n) < int(previous):
            increasingCondition = False
            break
        if n == previous:
            doubleCondition = True
        previous = n
    return doubleCondition and increasingCondition


def verifyNumberNewCondition(number):
    doubleCondition = False
    increasingCondition = True
    previous = str(number)[0]
    for n in str(number)[1:]:
        if int(n) < int(previous):
            increasingCondition = False
            break
        if n == previous and countCharactersInString(n, str(number)) == 2:
            doubleCondition = True
        previous = n
    return doubleCondition and increasingCondition


def countCharactersInString(charToCount, stringInput):
    numberOfChar = 0
    for c in stringInput:
        if c == charToCount:
            numberOfChar += 1
    return numberOfChar


def main():
    lowerLimit = 172851
    upperLimit = 675869

    sumOfVerifiedNumbers = 0
    for i in range(lowerLimit, upperLimit):
        if verifyNumber(i):
            sumOfVerifiedNumbers += 1
    print("Part 1:")
    print("Sum of numbers in the range that are ok:")
    print(sumOfVerifiedNumbers)

    sumOfVerifiedNumbers = 0
    for i in range(lowerLimit, upperLimit):
        if verifyNumberNewCondition(i):
            sumOfVerifiedNumbers += 1
    print()
    print("Part 2:")
    print("Sum of numbers in the range that are ok with new condition: ")
    print(sumOfVerifiedNumbers)


if __name__ == '__main__':
    main()
