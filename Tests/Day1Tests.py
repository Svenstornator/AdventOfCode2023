from Challenge.Day1 import Day1Part1, Day1Part2
import Utilities.InputParser

PART1TESTLOCATION = "../Tests/TestData/Day1Part1TestData"
PART2TESTLOCATION = "../Tests/TestData/Day1Part2TestData"

# Part One Tests
def test_FindFirstCalibrationOnFirstLine():
    inputData = Utilities.InputParser.ExtractListOfStringsFromLinesOfStrings(PART1TESTLOCATION)
    assert Day1Part1.GetFirstValueFromInputLine(inputData[0]) == '1'

def test_FindLastCalibrationOnFirstLine():
    inputData = Utilities.InputParser.ExtractListOfStringsFromLinesOfStrings(PART1TESTLOCATION)
    assert Day1Part1.GetFirstValueFromInputLine(reversed(inputData[0])) == '2'

def test_GetResultFromFirstLine():
    inputData = Utilities.InputParser.ExtractListOfStringsFromLinesOfStrings(PART1TESTLOCATION)
    assert Day1Part1.GetResultFromInputLine(inputData[0]) == 12

def test_Solve():
    assert Day1Part1.Solve(PART1TESTLOCATION) == 142


# Part Two Tests