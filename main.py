#! /usr/bin/python3

import argparse
import getch

from .utils import extract_loops

STACK_SIZE = 1000


def lexier(filename):
    """ Extract all brainfuck operators into a Python string

    >>> lexier("tests/bf_source_normal.bf")
    '+++++++++[>++++++++++<-]>+++++++.'

    # TODO: Error checking
    # TODO: Convert to polymorphic function to handle both file and string argument input
    # TODO: Handle comments in loop block (when pointer value = 0)
    """
    try:
        with open(filename) as file:
            return "".join(filter(
                lambda string: string in "><+-,.[]",
                file.read()
            ))

    except IOError:
        print("[-] iBrainfuck cannot open source code with filename", filename)

    return False


def parser(source):
    """ Indentify and group blocks to a list element

    >>> parser("+++++++++[>++++++++++<-]>+++++++.")
    ['+++++++++', ['>++++++++++<-'], '>+++++++.']

    >>> parser("+++++[>+++[>+>-<<]<-]")
    ['+++++', ['>+++', ['>+>-<<'], '<-']]
    """
    # Syntax checking: Check brackets balance
    if source.count("[") != source.count("]"):
        print("[-] Syntax Error: unmatched brackets")
        return False

    return extract_loops([source])


def interpreter(code_blocks, interactive=True):
    """ Run code generated from lexier

    >>> interpreter(["+++++++++", "[>++++++++++<-]", ">+++++++."], False)
    'a'
    """
    stack = [0 for _ in range(STACK_SIZE)]
    pointer = 0
    output = ""

    for block in code_blocks:
        is_loop = False
        counter = 0

        if block[0] == "[":
            is_loop = True
            counter_pointer = pointer
            counter = stack[counter_pointer]
            # String bracketsblog
            block = block[1:-1]

        while counter > 1 or not is_loop:
            if is_loop:
                counter = stack[counter_pointer]
            for op in block:
                if op == "+":
                    stack[pointer] += 1
                elif op == "-":
                    stack[pointer] -= 1
                elif op == ">":
                    pointer += 1
                elif op == "<":
                    pointer -= 1
                elif op == ".":
                    display = chr(stack[pointer])
                    if interactive:
                        print(display)
                    else:
                        output += display
                elif op == ",":
                    stack[pointer] == getch.getch()

            if not is_loop:
                break

    if not interactive:
        return output


def main():
    # Get filename from command line arguments
    parser = argparse.ArgumentParser(description="A Brainfuck interpreter")
    parser.add_argument("source", help="Brainfuck source code")
    args = parser.parse_args()
    print(args)

if __name__ == '__main__':
    main()
