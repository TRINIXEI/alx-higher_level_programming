#!/usr/bin/python3
"""Square Class defined with private instance size"""


class Square:
    """Square class.
    size: the private instance of the class
    area: is a method of the class Square
    """

    def __init__(self, size=0):
        """__init__
        initialize a private instance.
        validate size type and value of size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculate the square of size"""
        return self.__size ** 2
