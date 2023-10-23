#!/usr/bin/python3

def safe_print_division(a, b):
    """
    print result of division of two numbers
    """
    result = 0
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
