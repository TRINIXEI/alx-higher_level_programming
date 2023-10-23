#!/usr/bin/python3

def safe_print_integer(value):
    """
    print integer
    """
    bol = False
    try:
        if isinstance(value, int):
            bol = True
            print("{:d}".format(value))
        else:
            bol = false
            print("{}".format(value))
    except TypeError:
        pass
    finally:
        return bol
