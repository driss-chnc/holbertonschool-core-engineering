#!/usr/bin/env python3

"""Read a text file and print its content."""


def read_file(filename=""):
    """Read a text file and print its content."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
