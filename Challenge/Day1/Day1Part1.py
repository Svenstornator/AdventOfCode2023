import Utilities.InputParser as Parser

def GetFirstValueFromInputLine(inputLine):
    return next(character for character in inputLine if character.isnumeric())

def GetResultFromInputLine(inputLine):
    return int(GetFirstValueFromInputLine(inputLine) + GetFirstValueFromInputLine(reversed(inputLine)))

def Solve(fileLocation):
    inputData = Parser.ExtractListOfStringsFromLinesOfStrings(fileLocation)
    return sum([GetResultFromInputLine(inputLine) for inputLine in inputData])