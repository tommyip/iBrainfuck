from ..utils import extract_loops, in_nD_list


def test_extract_loops():
    # Test default
    assert extract_loops(["++>-[++<-]+-[[+]-][++->[--<+]]"]) == \
        ["++>-", ["++<-"], "+-", [["+"], "-"], ["++->", ["--<+"]]]

    # Test nested loops
    assert extract_loops(["[[++[>+++<-]]]."]) == [[["++", [">+++<-"]]], "."]

    # Test blank
    assert extract_loops([]) == []


def test_find_in_nD_list():
    # Test true
    assert in_nD_list(["++--,.", ["++>-", [">++"]], [["+"], [["-", "+-[]"]]]], "]") is True

    # Test false
    assert in_nD_list(["++--,.", ["++>-", [">++"]], [["+"], [["-"]]]], "]") is False

    # Test no loop
    assert in_nD_list(["++--++>>>..,,...++---"], "]") is False

    # Test corner case
    assert in_nD_list([[[[[[[["]"]]]]]]]], "]") is True

    # Test blank
    assert in_nD_list([], "+") is False
