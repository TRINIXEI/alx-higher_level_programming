#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    """
    # This adds first two Items of the 2 Given Tuples:
    # Variables:
    # tuple_a (tuple): The first tuple:
    # tuple_b (tuple): The first tuple:
    # A tuple that sum the first two items in the given tuple:
    """
    a = tuple_a or (0, 0)
    b = tuple_b or (0, 0)
    if len(tuple_a) == 1:
        a = (tuple_a[0], 0)
    if len(tuple_b) == 1:
        b = (tuple_b[0], 0)
    set_tuple = (a[0] + b[0], a[1] + b[1])
    return set_tuple
