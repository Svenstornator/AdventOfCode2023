from Challenge.Day1 import Day1Part1, Day1Part2, DataObjects
import Utilities.InputParser as Parser

PART1TESTLOCATION = "Day1Part1TestData"
PART2TESTLOCATION = "Day1Part2TestData"

# Part One Tests
def test_FindFirstCalibrationOnFirstLine():
    inputData = Parser.ExtractListOfStringsFromLinesOfStrings(PART1TESTLOCATION)
    assert Day1Part1.GetFirstValueFromInputLine(inputData[0]) == '1'

def test_FindLastCalibrationOnFirstLine():
    inputData = Parser.ExtractListOfStringsFromLinesOfStrings(PART1TESTLOCATION)
    assert Day1Part1.GetFirstValueFromInputLine(reversed(inputData[0])) == '2'

def test_GetResultFromFirstLine():
    inputData = Parser.ExtractListOfStringsFromLinesOfStrings(PART1TESTLOCATION)
    assert Day1Part1.GetResultFromInputLine(inputData[0]) == 12

def test_SolvePartOne():
    assert Day1Part1.Solve(PART1TESTLOCATION) == 142


# Part Two Tests
def test_NumberCalibrationsFromLine():
    inputLine = Parser.ExtractListOfStringsFromLinesOfStrings(PART2TESTLOCATION)[0]  # two1nine
    calibrations = Day1Part2.FindAllCalibrationNumbersFromLine(inputLine)
    assert calibrations[0].index == 3
    assert calibrations[0].value == 1
    assert len(calibrations) == 1


def test_StringCalibrationsFromLine():
    inputLine = Parser.ExtractListOfStringsFromLinesOfStrings(PART2TESTLOCATION)[0]  # two1nine
    calibrations = Day1Part2.FindAllCalibrationStringsFromLine(inputLine)
    assert calibrations[0].index == 0
    assert calibrations[0].value == 2
    assert calibrations[1].index == 4
    assert calibrations[1].value == 9
    assert len(calibrations) == 2


def test_AllCalibrationsFromLine():
    inputLine = Parser.ExtractListOfStringsFromLinesOfStrings(PART2TESTLOCATION)[0]  # two1nine
    calibrations = Day1Part2.FindAllCalibrationsFromLine(inputLine)
    assert calibrations[0].index == 0
    assert calibrations[0].value == 2
    assert calibrations[1].index == 4
    assert calibrations[1].value == 9
    assert calibrations[2].index == 3
    assert calibrations[2].value == 1
    assert len(calibrations) == 3


def test_MinFindsFirstCalibrationFromLine():
    inputLine = Parser.ExtractListOfStringsFromLinesOfStrings(PART2TESTLOCATION)[0]  # two1nine
    calibration = min(Day1Part2.FindAllCalibrationStringsFromLine(inputLine))
    assert calibration.index == 0
    assert calibration.value == 2


def test_MaxFindsLastCalibrationFromLine():
    inputLine = Parser.ExtractListOfStringsFromLinesOfStrings(PART2TESTLOCATION)[0]  # two1nine
    calibration = max(Day1Part2.FindAllCalibrationStringsFromLine(inputLine))
    assert calibration.index == 4
    assert calibration.value == 9

def test_SolveDayTwo():
    assert Day1Part2.Solve(PART2TESTLOCATION) == 281