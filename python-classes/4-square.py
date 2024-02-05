#!/usr/bin/python3
"""
create class square
"""


class Square:
    def __init__(self, size=0):
        self.size = size

    def size(self):
        return (self.__size)

    def size(self, value):
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return (self.__size * self.__size)
