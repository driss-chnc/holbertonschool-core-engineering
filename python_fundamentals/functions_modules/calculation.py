#!/usr/bin/env python3

try:
    from .variable_load_5 import a
except ImportError:
    from importlib import import_module

    a = import_module("variable_load_5").a


if __name__ == "__main__":
    print(a)
