import Utilities.InputParser

def test_GetListWithoutDelimiter():
    assert Utilities.InputParser.ExtractListWithIntValues("TestData/nodelimiterlist.txt", "") == [1, 2, 3, 4, 5, 6]

def test_GetListWithCommaDelimiter():
    assert Utilities.InputParser.ExtractListWithIntValues("TestData/commaseparatedlist.txt", ",") == [1, 2, 3, 4, 5, 6, 7]

def test_GetListWithSpaceDelimiter():
    assert Utilities.InputParser.ExtractListWithIntValues("TestData/spacedelimiter.txt", " ") == [1, 2, 3, 4]

def test_GetListWithSpaceDelimiterAsChars():
    assert Utilities.InputParser.ExtractListWithStringValues("TestData/spacedelimiter.txt", " ") == ["1", "2", "3", "4"]

def test_GetListWithCommaDelimiterAsStrings():
    assert Utilities.InputParser.ExtractListWithStringValues("TestData/commaseparatedlist.txt", ",") == ["1", "2", "3", "4", "5", "6", "7"]

def test_GetListWithNoDelimiterAsStrings():
    assert Utilities.InputParser.ExtractListWithStringValues("TestData/nodelimiterlist.txt", "") == ["1", "2", "3", "4", "5", "6"]

def test_GetListWithSpaceDelimiterAsStrings():
    assert Utilities.InputParser.ExtractListWithStringValues("TestData/listofstringswithspacedelimiter", " ") == ["hello", "world", "how", "are", "you"]

def test_Get2dIntArrayWithSpaceDelimiter():
    assert Utilities.InputParser.Extract2DArrayWithIntValues("TestData/2darrayspacedelimiter", " ") == [[1,2,3,4],[5,6,7,8]]

def test_Get2dIntArrayWithCommaDelimiter():
    assert Utilities.InputParser.Extract2DArrayWithIntValues("TestData/2darraycommadelimiter", ",") == [[1,2,3],[4,5,6]]

def test_Get2dIntArrayWithNoDelimiter():
    assert Utilities.InputParser.Extract2DArrayWithIntValues("TestData/2darraynodelimitertrailingline","") == [[1,2,3,4,5],[6,7,8,9,0]]

def test_GetListOfStringsWithNewlineDelimiter():
    assert Utilities.InputParser.ExtractListOfStringsFromLinesOfStrings("TestData/listofstringswithnewlinedelimiter") == ["goodnight", "world", "sleep", "well"]