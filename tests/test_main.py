"""
Pytest test module
"""

from ..main import parser, lexier


def test_parser():
    # Test normal source code from file
    assert parser("tests/bf_source_normal.bf") == \
        "+++++++++[>++++++++++<-]>+++++++."

    # Test blank source code from FileExistsError
    assert parser("tests/bf_source_no_code.bf") == ""

    # Test source code from string
    # assert parser("comments +++++++++[>++++++ loop here ++++<-]>+++++++.") == \
    #     "+++++++++[>++++++++++<-]>+++++++."


def test_lexier():
    # Test default
    assert lexier("+++++++++[>++++++++++<-]>+++++++.") == \
        ["+++++++++", "[>++++++++++<-]", ">+++++++."]

    # Test loop at the end
    assert lexier("+++++++++[>++++++++++<-][+++]") == \
        ["+++++++++", "[>++++++++++<-]", "[+++]"]

    # Test no code
    assert lexier("") == []
