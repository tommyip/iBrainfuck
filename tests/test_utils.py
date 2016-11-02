from ..utils import extract_loops, in_nD_list


def test_extract_loops():
    assert extract_loops(["++>-[++<-]+-[[+]-][++->[--<+]]"]) == \
        ["++>-", ["++<-"], "+-", [["+"], "-"], ["++->", ["--<+"]]]

    assert extract_loops(["[[++[>+++<-]]]."]) == [[["++", [">+++<-"]]], "."]

    assert extract_loops([]) == []


def test_find_in_nD_list():
    assert in_nD_list(["++--,.", ["++>-", [">++"]], [["+"], [["-"]]]], "]") is False

    assert in_nD_list(["++--,.", ["++>-", [">++"]], [["+"], [["-", "+-[]"]]]], "]") is True

    assert in_nD_list(["++--++>>>..,,...++---"], "]") is False

    assert in_nD_list([[[[[[[["]"]]]]]]]], "]") is True

    assert in_nD_list([], "+") is False
