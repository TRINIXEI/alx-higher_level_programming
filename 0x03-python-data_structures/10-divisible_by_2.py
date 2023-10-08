#!/usr/bin/python3


def divisible_by_2(my_list=[]):

    """
    # This searches for multiples of 2:
    # Variables:
    # my_list(list): The first tuple..
    # Lists of Bool stating the possibility of division
    # of the number with 2 at same position in the List:
    """
    lists = []
    for num in my_list:
        if num % 2 == 0:
            lists.append(True)
        else:
            lists.append(False)
    return lists
