"""
Pytest test module
"""

from ..main import lexier, parser, interpreter


def test_lexier(capfd):
    # Test normal source code from file
    assert lexier("tests/bf_source_normal.bf") == "+++++++++[>++++++++++<-]>+++++++."

    # Test input from string
    assert lexier("+++++++++ comments [ > ++++++++++ <- ] > +++++++.  end", False) == \
        "+++++++++[>++++++++++<-]>+++++++."

    # Test blank source code from file
    assert lexier("tests/bf_source_no_code.bf") == ""

    # Test unknown filename
    lexier("tests/unknown.bf") is False
    _, err = capfd.readouterr()
    assert err == "[-] iBrainfuck cannot open source code with filename tests/unknown.bf\n"

    # Test unmatch brackets
    lexier("+++++++++[>+++++[+++++<-]>+++++++.", False) is False
    _, err = capfd.readouterr()
    assert err == "[-] Syntax Error: unmatched brackets\n"


def test_parser(capfd):
    # Test default
    assert parser("+++++++++[>++++++++++<-]>+++++++.") == ["+++++++++", [">++++++++++<-"], ">+++++++."]

    # Test hello world
    hw = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."
    assert parser(hw) == ["++++++++", [">++++", [">++>+++>+++>+<<<<-"], ">+>+>->>+", ["<"], "<-"],
                          ">>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."]

    # Test loop at the end
    assert parser("+++++++++[>++++++++++<-][+++]") == ["+++++++++", [">++++++++++<-"], ["+++"]]

    # Test loop at the start
    assert parser("[+++].>[++<-]") == [["+++"], ".>", ["++<-"]]

    # Test blank source code
    assert parser("") == []

    # Test 2 dimensional loop
    assert parser("+++++[>+++[>+>-<<]<-]") == ['+++++', ['>+++', ['>+>-<<'], '<-']]


def test_interpreter(capfd):
    # Test normal
    interpreter(["+++++++++", [">++++++++++<-"], ">+++++++."], 10)
    output, _ = capfd.readouterr()
    assert output == "a"

    interpreter(["++++++++", [">++++", [">++>+++>+++>+<<<<-"], ">+>+>->>+", ["<"], "<-"],
                ">>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."], 20)
    output, _ = capfd.readouterr()
    assert output == "Hello World!\n"
