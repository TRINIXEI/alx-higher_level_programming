#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    print list using try/except
    """
    index = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            index += 1
        print()
    except IndexError:
        print()
    finally:
        return index
