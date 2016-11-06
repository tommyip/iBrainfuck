#! /usr/bin/python3
"""
Name: iBrainfuck
Author: Tommy Ip <hkmp7tommy@gmail.com>
Github repo: https://gituhub.com/tommyip/iBrainfuck

iBrainfuck is a interpreter for the Brainfuck language written in Python 3

Testing are handled by Pytest, invoke them by running:

    ~$ py.test

in the project's root path. You have to install the pytest plugin `pytest-pythonpath` in order
for pytest to properly detect the directories. Unittest are in tests/ directory and doctest are
inline with source code.

Coming features include:
    - PyPy 3 support
    - Code Optimization
"""

import sys
import argparse
import getch
from utils import extract_loops


def lexier(filename):
    """ Extract all brainfuck operators into a Python string

    >>> lexier("tests/bf_source_normal.bf")
    '+++++++++[>++++++++++<-]>+++++++.'

    """
    # TODO: Error checking
    # TODO: Convert to polymorphic function to handle both file and string argument input
    # TODO: Handle comments in loop block (when pointer value = 0)

    try:
        with open(filename) as file:
            return "".join(filter(
                lambda string: string in "><+-,.[]",
                file.read()
            ))

    except IOError:
        print("[-] iBrainfuck cannot open source code with filename " + filename, file=sys.stderr)

    return False


def parser(source):
    """ Parse raw source code from lexier to a semi-AST like data structure

    >>> parser("+++++++++[>++++++++++<-]>+++++++.")
    ['+++++++++', ['>++++++++++<-'], '>+++++++.']

    >>> parser("+++++[>+++[>+>-<<]<-]")
    ['+++++', ['>+++', ['>+>-<<'], '<-']]

    """
    # TODO: Optimise source code

    # Syntax checking: Check brackets balance
    if source.count("[") != source.count("]"):
        print("[-] Syntax Error: unmatched brackets", file=sys.stderr)
        return False

    return extract_loops([source])


def interpreter(ast, size):
    """ Execute code generated from parser

    >>> interpreter(["+++++++++", [">++++++++++<-"], ">+++++++."], 10)
    a
    >>> interpreter(["++++++++", [">++++", [">++>+++>+++>+<<<<-"], ">+>+>->>+", ["<"], "<-"], \
        ">>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."], 20)
    Hello World!

    """
    stack = [0] * size
    pointer = 0

    for block in ast:
        stack, pointer = evaluate(stack, block, pointer)


def evaluate(stack, block, pointer):
    if isinstance(block, str):
        # Commands structure
        for op in block:
            if op == ">":
                pointer += 1
            elif op == "<":
                if pointer > 0:
                    pointer -= 1
            elif op == ",":
                stack[pointer] = ord(getch.getch())
            elif op == ".":
                print(chr(stack[pointer]), end="", flush=True)
            elif op == "+":
                stack[pointer] += 1
            elif op == "-":
                stack[pointer] -= 1
    else:
        # loop structure
        counter = stack[pointer]
        while counter > 0:
            for code in block:
                stack, pointer = evaluate(stack, code, pointer)
                counter = stack[pointer]
    return stack, pointer


def main():
    parser = argparse.ArgumentParser(description="iBrainfuck -> A brainfuck interpreter implementation in Python")
    parser.add_argument("source", help="Brainfuck source file [.bf]")
    parser.add_argument("-s", "--size", help="The size of the brainfuck array, default: 6000", type=int)
    args = parser.parse_args()

    stack_size = args.size if args.size else 6000



if __name__ == '__main__':
    main()
