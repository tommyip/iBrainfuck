#! /usr/bin/python3
"""
Name: iBrainfuck
Author: Tommy Ip <hkmp7tommy@gmail.com>
Github repo: https://gituhub.com/tommyip/iBrainfuck

iBrainfuck is a Brainfuck interpreter written in Python 3.

Testing are handled by Pytest, invoke them by running:

    ~$ py.test

in the project's root path. You have to install the pytest plugin `pytest-pythonpath` in order
for pytest to properly detect the directories. Unittest are in tests/ directory and doctest
while inline with source code.
"""

import argparse
import getch
import sys


def lexier(source, isfile=True):
    """ Extract all brainfuck operators into a Python string

    >>> lexier("tests/bf_source_normal.bf")
    '+++++++++[>++++++++++<-]>+++++++.'
    """
    # TODO: Handle comments in loop block (when pointer value = 0)

    try:
        if isfile:
            with open(source) as f:
                source = f.read()

        source = "".join(filter(
            lambda char: char in "><+-,.[]",
            source
        ))

        # Error checking
        if source.count("[") != source.count("]"):
            print("[-] Syntax Error: unmatched brackets", file=sys.stderr)
            return False

        return source

    except IOError:
        print("[-] iBrainfuck cannot open source code with filename " + source, file=sys.stderr)
        return False


def parser(source):
    """ Parse raw source code to a semi-AST like data structure

    >>> parser("+++++++++[>++++++++++<-]>+++++++.")
    ['+++++++++', ['>++++++++++<-'], '>+++++++.']

    >>> parser("+++++[>+++[>+>-<<]<-]")
    ['+++++', ['>+++', ['>+>-<<'], '<-']]
    """
    # TODO: Optimise source code

    new_loops = []

    for loop in [source]:
        brackets = 0
        op_block = ""
        for op in loop:
            if op not in "[]":
                op_block += op

            else:
                if op == "[":
                    if not brackets:
                        # Non loop structure
                        if op_block != "":
                            new_loops.append(op_block)
                            op_block = ""
                    else:
                        op_block += "["
                    brackets += 1

                elif op == "]":
                    brackets -= 1
                    if not brackets:
                        # Loop structure
                        if "[" in op_block or "]" in op_block:
                            op_block = parser(op_block)
                        else:
                            op_block = [op_block]
                        new_loops.append(op_block)
                        op_block = ""
                    else:
                        op_block += "]"

        if op_block != "":
            new_loops.append(op_block)

    return new_loops


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
        stack, pointer = _evaluate(stack, block, pointer)


def _evaluate(stack, block, pointer):
    """ Recursively execute code blocks. """
    if isinstance(block, str):
        # Commands structure
        for op in block:
            if op == ">":
                pointer += 1
            elif op == "<":
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
                stack, pointer = _evaluate(stack, code, pointer)
                counter = stack[pointer]
    return stack, pointer


def main():
    argparser = argparse.ArgumentParser(description="iBrainfuck -> A brainfuck interpreter implementation in Python")
    argparser.add_argument("source", help="Brainfuck source file [.bf]")
    argparser.add_argument("-s", "--size", help="The size of the brainfuck array, default: 6000", type=int)
    args = argparser.parse_args()

    stack_size = args.size if args.size else 6000

    raw_source = lexier(args.source)
    if raw_source:
        ast = parser(raw_source)
        if ast:
            interpreter(ast, stack_size)

if __name__ == '__main__':
    main()
