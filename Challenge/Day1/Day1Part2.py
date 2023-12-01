import Utilities.InputParser

def GetFirstValueFromInputLine(inputLine):
    for character in inputLine:
        if character.isnumeric():
            return int(character)

def GetLastValueFromInputLine(inputLine):
    for character in reversed(inputLine):
        if character.isnumeric():
            return int(character)

def GetResultFromInputLine(inputLine):
    firstValue = GetFirstValueFromInputLine(inputLine)
    secondValue = GetLastValueFromInputLine(inputLine)
    return int(str(firstValue) + str(secondValue))

def Solve(fileLocation):
    inputData = Utilities.InputParser.ExtractListOfStringsFromLinesOfStrings(fileLocation)
    result = 0
    for inputLine in inputData:
        result = result + GetResultFromInputLine(inputLine)
    return result