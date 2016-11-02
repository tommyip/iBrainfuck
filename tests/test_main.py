"""
Pytest test module
"""

from ..main import lexier, parser  # , interpreter


def test_lexier(capsys):
    # Test normal source code from file
    assert lexier("tests/bf_source_normal.bf") == "+++++++++[>++++++++++<-]>+++++++."

    # Test blank source code from file
    assert lexier("tests/bf_source_no_code.bf") == ""

    # Test unknown filename
    lexier("tests/unknown.bf") is False
    output, _ = capsys.readouterr()
    assert output == "[-] iBrainfuck cannot open source code with filename tests/unknown.bf\n"

    # Test source code from string
    # assert lexier("comments+++++++++[>++++++ loop ++++<-]>+++++++.") == \
    #     "+++++++++[>++++++++++<-]>+++++++."


def test_parser(capsys):
    # Test default
    assert parser("+++++++++[>++++++++++<-]>+++++++.") == ["+++++++++", [">++++++++++<-"], ">+++++++."]

    # Test loop at the end
    assert parser("+++++++++[>++++++++++<-][+++]") == ["+++++++++", [">++++++++++<-"], ["+++"]]

    # Test loop at the start
    assert parser("[+++].>[++<-]") == [["+++"], ".>", ["++<-"]]

    # Test blank source code
    assert parser("") == []

    # Test 2 dimensional loop
    assert parser("+++++[>+++[>+>-<<]<-]") == ['+++++', ['>+++', ['>+>-<<'], '<-']]

    # Test unmatch brackets
    parser("+++++++++[>+++++[+++++<-]>+++++++.") is False
    output, _ = capsys.readouterr()
    assert output == "[-] Syntax Error: unmatched brackets\n"


def test_interpreter():
    # Test normal
    # assert interpreter(["+++++++++", "[>++++++++++<-]", ">+++++++."], False) == "a"
    pass
