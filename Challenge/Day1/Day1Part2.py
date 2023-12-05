import Challenge.Day1.DataObjects as DataObjects
import Utilities.InputParser as Parser


def Solve(fileLocation):
    inputData = Parser.ExtractListOfStringsFromLinesOfStrings(fileLocation)
    endResult = 0
    for line in inputData:
        foundCalibrations = FindAllCalibrationsFromLine(line)
        endResult = endResult + int(str(min(foundCalibrations).value) + str(max(foundCalibrations).value))
    return endResult


def FindAllCalibrationsFromLine(line):
    foundCalibrations = FindAllCalibrationStringsFromLine(line)
    foundCalibrations.extend(FindAllCalibrationNumbersFromLine(line))
    return foundCalibrations


def FindAllCalibrationNumbersFromLine(line):
    return [DataObjects.Calibration(characterIndex, int(value)) for characterIndex, value in enumerate(list(line)) if value.isnumeric()]


def FindAllCalibrationStringsFromLine(line):
    validDigits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    return [DataObjects.Calibration(line.find(value), digitIndex+1) for digitIndex, value in enumerate(validDigits) if line.find(value) > -1]
