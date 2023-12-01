def ExtractListWithIntValues(relativeFileLocation, delimiter):
    inputAsListOfStrings = ExtractListWithStringValues(relativeFileLocation, delimiter)
    return [int(x) for x in inputAsListOfStrings]

def ExtractListWithStringValues(relativeFileLocation, delimiter):
    inputFile = open(relativeFileLocation, "r")
    inputAsString = inputFile.readline()
    return inputAsString.split(delimiter) if delimiter != "" else list(inputAsString)
