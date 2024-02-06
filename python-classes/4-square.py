#!/usr/bin/python3
"""square modul"""


class Square:
    """class that defines a square"""
    def __init__(self, size=0):
        """init a new square"""
        self.size = size

    @property
    def size(self):
        """retrieve size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """ def if size is an >0 int in private attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ define the area of a square entrer in argument"""
        return (self.__size ** 2)
