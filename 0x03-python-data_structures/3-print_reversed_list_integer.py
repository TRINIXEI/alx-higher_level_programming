#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):

    """
    # Write a function that prints all integers of a list, in reverse order.
    # VARIABLE(" "):
    # my_list(list) Print a list of integers... in reverse!
    # Format: one integer per line.
    # You have to use str.format() to print integers
    """
    if my_list:
        my_list.reverse()
        for rev in my_list:
            print("{:d}".format(rev))
