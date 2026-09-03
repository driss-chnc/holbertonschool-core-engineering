#!/usr/bin/env python3

for first in range(10):
    for second in range(first + 1, 10):
        if first < 8 or second < 9:
            print("{:02d}, ".format(first * 10 + second), end="")
        else:
            print("{:02d}".format(first * 10 + second))
