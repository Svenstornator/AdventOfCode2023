from Challenge.Day1 import Day1Part1
import Utilities.InputParser

TESTDATALOCATION = "../Tests/TestData/Day1Part1TestData"

def test_FindFirstCalibrationOnFirstLine():
    inputData = Utilities.InputParser.ExtractListOfStringsFromLinesOfStrings(TESTDATALOCATION)
    assert Day1Part1.GetFirstValueFromInputLine(inputData[0]) == 1

def test_FindLastCalibrationOnFirstLine():
    inputData = Utilities.InputParser.ExtractListOfStringsFromLinesOfStrings(TESTDATALOCATION)
    assert Day1Part1.GetLastValueFromInputLine(inputData[0]) == 2

def test_GetResultFromFirstLine():
    inputData = Utilities.InputParser.ExtractListOfStringsFromLinesOfStrings(TESTDATALOCATION)
    assert Day1Part1.GetResultFromInputLine(inputData[0]) == 12

def test_Solve():
    assert Day1Part1.Solve(TESTDATALOCATION) == 142

