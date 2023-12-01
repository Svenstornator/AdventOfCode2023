def ExtractList(relativeFileLocation, delimiter):
    inputFile = open(relativeFileLocation, "r")
    inputAsString = inputFile.readline()
    inputAsListOfStrings = inputAsString.split(delimiter) if delimiter != "" else list(inputAsString)
    return [int(x) for x in inputAsListOfStrings]