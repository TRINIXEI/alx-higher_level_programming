#!/usr/bin/python3
# 3-say_my_name.py
"""Definition of a function name-printing."""


def say_my_name(first_name, last_name=""):
    """Printing a name.

    Arguments:
        first_name (str): The first_name to be printed.
        last_name (str): The last_name to be printed.
    Raise:
        TypeError: If either of first_name Or last_name aren't  string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if last_name:  # if last_name isn't empty
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {} ".format(first_name))
