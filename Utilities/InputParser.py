def ExtractListWithIntValues(relativeFileLocation, delimiter):
    inputAsListOfStrings = ExtractListWithStringValues(relativeFileLocation, delimiter)
    return [int(x) for x in inputAsListOfStrings]

def ExtractListWithStringValues(relativeFileLocation, delimiter):
    inputFile = open(relativeFileLocation, "r")
    inputAsString = inputFile.readline()
    return inputAsString.split(delimiter) if delimiter != "" else list(inputAsString)

def Extract2DArrayWithIntValues(relativeFileLocation, delimiter):
    inputFile = open(relativeFileLocation, "r")
    inputLines = inputFile.readlines()
    returnValue = []
    for inputLine in inputLines:
        lineAsListOfStrings = inputLine.split(delimiter) if delimiter != "" else list(inputLine)
        returnValue.append([int(x) for x in lineAsListOfStrings])
    return returnValue