def ExtractListWithIntValues(relativeFileLocation, delimiter):
    inputAsListOfStrings = ExtractListWithStringValues(relativeFileLocation, delimiter)
    return [int(x) for x in inputAsListOfStrings]

def ExtractListWithStringValues(relativeFileLocation, delimiter):
    inputFile = open(relativeFileLocation, "r")
    inputAsString = inputFile.readline()
    return __SplitLineWithDelimiter(inputAsString, delimiter)

def Extract2DArrayWithIntValues(relativeFileLocation, delimiter):
    inputLines = ExtractListOfStringsFromLinesOfStrings(relativeFileLocation)
    returnValue = []
    for inputLine in inputLines:
        lineAsListOfStrings = __SplitLineWithDelimiter(inputLine, delimiter)
        returnValue.append([int(x) for x in lineAsListOfStrings])
    return returnValue

def ExtractListOfStringsFromLinesOfStrings(relativeFileLocation):
    inputFile = open(relativeFileLocation, "r")
    inputLines = inputFile.readlines()
    return [line.strip() for line in inputLines]

def __SplitLineWithDelimiter(string, delimiter):
    return string.split(delimiter) if delimiter != "" else list(string)