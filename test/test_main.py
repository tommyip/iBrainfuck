"""
Pytest test module
"""

from .main import parser  # , Lexier, Interpreter


def test_parser():
    assert parser("test.bf") == "+++++++++[>++++++++++<-]>+++++++."
