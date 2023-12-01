import Utilities.InputParser

def test_GetListWithoutDelimiter():
    assert Utilities.InputParser.ExtractListWithIntValues("TestData/nodelimiterlist.txt", "") == [1, 2, 3, 4, 5, 6]

def test_GetListWithCommaDelimiter():
    assert Utilities.InputParser.ExtractListWithIntValues("TestData/commaseparatedlist.txt", ",") == [1, 2, 3, 4, 5, 6, 7]

def test_GetListWithSpaceDelimiter():
    assert Utilities.InputParser.ExtractListWithIntValues("TestData/spacedelimiter.txt", " ") == [1, 2, 3, 4]

def test_GetListWithSpaceDelimiterAsStrings():
    assert Utilities.InputParser.ExtractListWithStringValues("TestData/spacedelimiter.txt", " ") == ["1", "2", "3", "4"]

def test_GetListWithCommaDelimiterAsStrings():
    assert Utilities.InputParser.ExtractListWithStringValues("TestData/commaseparatedlist.txt", ",") == ["1", "2", "3", "4", "5", "6", "7"]

def test_GetListWithNoDelimiterAsStrings():
    assert Utilities.InputParser.ExtractListWithStringValues("TestData/nodelimiterlist.txt", "") == ["1", "2", "3", "4", "5", "6"]

def test_Get2dIntArrayWithSpaceDelimiter():
    assert Utilities.InputParser.Extract2DArrayWithIntValues("TestData/2darrayspacedelimiter", " ") == [[1,2,3,4],[5,6,7,8]]