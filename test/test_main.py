"""
Pytest test module
"""

from ..main import parser, lexier


def test_parser():
    # Test source code from file
    assert parser("test/test.bf") == "+++++++++[>++++++++++<-]>+++++++."

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
