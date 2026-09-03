#!/usr/bin/env python3

alphabet = "abcdefghijklmnopqrstuvwxyz"
result = ""

for lettre in alphabet:
    if lettre != "q" and lettre != "e":
        result += lettre

print(result)
