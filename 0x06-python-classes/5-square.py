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
        self.size = size

    @property
    def size(self):
        """Get Size Value"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set Size Value"""
        if not (isinstance(value, int)):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate the square of size"""
        return self.__size ** 2

    def my_print(self):
        """Print square using #"""
        if (self.__size == 0):
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
