#! /usr/bin/python3

import argparse


def parser(filename: str) -> str:

    with open(filename, 'r') as file:
        source_code = "".join(_ for _ in file.read() if _ in "><+-.,[]")

    # TODO: Error checking

    return source_code


def lexier(source: str) -> list:
    blocks = []
    current_block = ""
    for op in source:
        if op not in ["[", "]"]:
            current_block += op
        elif op == "[":
            if current_block != "":
                blocks.append(current_block)
            current_block = "["
        else:
            blocks.append(current_block + "]")
            current_block = ""
        print(op, blocks, current_block)
    if current_block != "":
        blocks.append(current_block)
    return blocks


def interpreter(code_block: list):
    pass


def main():
    # Get filename from command line arguments
    parser = argparse.ArgumentParser(description="A Python implementation for the Brainfuck language.")
    parser.add_argument("file", help="The source code of your brainfuck program.")
    args = parser.parse_args()

if __name__ == '__main__':
    main()
