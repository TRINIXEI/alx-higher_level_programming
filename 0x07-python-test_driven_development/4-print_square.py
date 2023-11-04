#!/usr/bin/python3
# 4-print_square.py
"""Defination of a function square printing."""


def print_square(size):
    """Printing a square the # char.

    Argumnets:
        size (int): height/width of the_square.
    Rais:
        TypeError: if size is not_integer.
        ValueError: if size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
