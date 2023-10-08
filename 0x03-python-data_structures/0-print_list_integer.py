#!/usr/bin/python3

def print_list_integer(my_list=[]):

    """
    # Write a function that prints all integers of a list.
    # Format: one integer per line. See example
    # VARIABLE(" "):
    # my_list(list)  Print a list of integers
    # You are not allowed to cast integers into strings
    # You have to use str.format() to print integers
    """
    for integers in my_list:
        print("{:d}".format(integers))
