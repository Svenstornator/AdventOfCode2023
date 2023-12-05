def ExtractListWithIntValues(relativeFileLocation, delimiter):
    """
    Takes an input of a single row of numbers separated by a delimiter and returns it as a list of integers
    :param relativeFileLocation: the name of the relative path to the file to read from as a string
    :param delimiter: the means by which the values are separated, such as commas, spaces or and empty string.
                Note: This will not accept a newline character as a delimiter as it expects everything on a single row
    :return: returns the numbers as a list of integers
    """
    inputAsListOfStrings = ExtractListWithStringValues(relativeFileLocation, delimiter)
    return [int(x) for x in inputAsListOfStrings]


def ExtractListWithStringValues(relativeFileLocation, delimiter):
    """
    Takes an input of a single row of strings (includes individual chars) separated by a delimiter
    and returns it as a list of strings (or chars)
    :param relativeFileLocation: the name of the relative path to the file to read from as a string
    :param delimiter: the means by which the values are separated, such as commas, spaces or an empty string.
                Note: This will not accept a newline character as a delimiter as it expects everything on a single row
    :return: returns the numbers as a list of strings or chars
    """
    inputFile = open(relativeFileLocation, "r")
    inputAsString = inputFile.readline()
    return __SplitLineWithDelimiter(inputAsString, delimiter)


def Extract2DArrayWithIntValues(relativeFileLocation, delimiter):
    """
    Takes an input of a multiple rows of number separated by a delimiter
    and returns it as a list of lists of ints
    :param relativeFileLocation: the name of the relative path to the file to read from as a string
    :param delimiter: the means by which the values are separated, such as commas, spaces or an empty string.
            Note: This will not accept newline characters, as newline characters separate the lists of lists
    :return: returns the numbers as a list of strings or chars
    """
    inputLines = ExtractListOfStringsFromLinesOfStrings(relativeFileLocation)
    returnValue = []
    for inputLine in inputLines:
        lineAsListOfStrings = __SplitLineWithDelimiter(inputLine, delimiter)
        returnValue.append([int(x) for x in lineAsListOfStrings])
    return returnValue

def Extract2DArrayWithCharValues(relativeFileLocation, delimiter):
    """
    Takes an input of a multiple rows of number separated by a delimiter
    and returns it as a list of lists of ints
    :param relativeFileLocation: the name of the relative path to the file to read from as a string
    :param delimiter: the means by which the values are separated, such as commas, spaces or an empty string.
            Note: This will not accept newline characters, as newline characters separate the lists of lists
    :return: returns the numbers as a list of strings or chars
    """
    inputLines = ExtractListOfStringsFromLinesOfStrings(relativeFileLocation)
    returnValue = []
    for inputLine in inputLines:
        lineAsListOfStrings = __SplitLineWithDelimiter(inputLine, delimiter)
        returnValue.append(lineAsListOfStrings)
    return returnValue


def ExtractListOfStringsFromLinesOfStrings(relativeFileLocation):
    """
    Takes an input of a multiple rows of strings and returns a list of those strings
    :param relativeFileLocation: the name of the relative path to the file to read from as a string
    :return: returns the numbers as a list of strings or chars
    """
    inputFile = open(relativeFileLocation, "r")
    inputLines = inputFile.readlines()
    return [line.strip() for line in inputLines]


def __SplitLineWithDelimiter(string, delimiter):
    return string.split(delimiter) if delimiter != "" else list(string)
