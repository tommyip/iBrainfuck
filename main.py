#! /usr/bin/python3

import argparse


def parser(filename: str) -> str:
    with open(filename, 'r') as file:
        source_code = "".join(_ for _ in file.read() if _ in "><+-.,[]")

    return source_code


def lexier(source: str) -> list:
    pass


def interpreter(code_block: list):
    pass


def main():
    # Get filename from command line arguments
    parser = argparse.ArgumentParser(description="A Python implementation for the Brainfuck language.")
    parser.add_argument("file", help="The source code of your brainfuck program.")
    args = parser.parse_args()

if __name__ == '__main__':
    main()
