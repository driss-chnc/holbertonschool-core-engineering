SEARCH
=======
# Python fundamentals: control flow

## Description

This directory contains introductory Python exercises focused on control flow:

- conditional statements with `if`, `elif`, and `else`;
- `for` loops and nested loops;
- ranges and formatted output;
- hexadecimal conversion;
- classification of positive, negative, and zero values.

## Requirements

- Python 3.8 or later

## Usage

Run any exercise from this directory with `python3`:

```bash
python3 positive_or_negative.py
python3 last_digit.py
python3 print_alphabt.py
python3 print_comb2.py
python3 print_comb3.py
python3 print_hexa.py
```

The two number-classification scripts generate random values, so their output changes on each run. The other scripts produce deterministic output.

## Exercises

| File | Description |
| --- | --- |
| `positive_or_negative.py` | Generates an integer from `-10` to `10` and displays whether it is positive, negative, or zero. |
| `last_digit.py` | Generates an integer from `-10000` to `10000` and classifies its last digit. |
| `print_alphabt.py` | Prints the lowercase alphabet except for `q` and `e`. |
| `print_comb2.py` | Prints all two-digit numbers from `00` to `99`, separated by commas. |
| `print_comb3.py` | Prints combinations of two different digits in ascending order. |
| `print_hexa.py` | Prints each number from `0` to `98` with its hexadecimal representation. |

## Concepts practiced

- Testing conditions and comparison operators
- Iterating with `range()`
- Nesting loops
- Formatting numbers with format specifications such as `{:02d}`
- Converting integers with `hex()`

