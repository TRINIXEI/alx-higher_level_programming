#!/usr/bin/python3
"""Class Square validate size to integer"""


class Square:
    """Square class with private instance.
    validate square
    """

    def __init__(self, size=0):
        """Define private variable
        size: must be an int
        """

        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
