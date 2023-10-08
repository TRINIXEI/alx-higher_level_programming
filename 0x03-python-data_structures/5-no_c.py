#!/usr/bin/python3

def no_c(my_string):

    """
    # Write a function that removes all characters c and C from a string.
    # VARIABLE(" "):
    # no_c(str) Can you C me now?
    # The function should return the new string
    """
    str_2 = []
    for list_alph in my_string:
        if list_alph not in 'cC':
            str_2.append(list_alph)
    return ''.join(str_2)
