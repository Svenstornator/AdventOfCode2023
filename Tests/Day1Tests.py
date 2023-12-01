from Challenge.Day1 import Day1Part1

TESTDATALOCATION = "../Tests/TestData/Day1Part1TestData"

def test_GetDataAsAListOfStrings():
    assert Day1Part1.GetInputDataAsListOfStrings(TESTDATALOCATION) == ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]

def test_FindFirstCalibrationOnFirstLine():
    inputData = Day1Part1.GetInputDataAsListOfStrings(TESTDATALOCATION)
    assert Day1Part1.GetFirstValueFromInputLine(inputData[0]) == 1

def test_FindLastCalibrationOnFirstLine():
    inputData = Day1Part1.GetInputDataAsListOfStrings(TESTDATALOCATION)
    assert Day1Part1.GetLastValueFromInputLine(inputData[0]) == 2

def test_GetResultFromFirstLine():
    inputData = Day1Part1.GetInputDataAsListOfStrings(TESTDATALOCATION)
    assert Day1Part1.GetResultFromInputLine(inputData[0]) == 12