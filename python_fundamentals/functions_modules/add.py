#!/usr/bin/env python3

from add_0 import add  # type: ignore[import-not-found]


if __name__ == "__main__":
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
