#!/usr/bin/python3

def replace_in_list(my_list, idx, element):

    """
    # Write a function that replaces an element of
    # a list at a specific position (like in C).
    # VARIABLE(" "):
    # my_list(list) Replace element
    # If idx is negative, the function should not modify anything,
    #           and returns the original list
    # If idx is out of range (> of number of element in my_list),
    #           the function should not modify anything, and returns the
    """
    if idx < 0 or idx >= len(my_list):
        return my_list

    my_list[idx] = element

    return my_list
