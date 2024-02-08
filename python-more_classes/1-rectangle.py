#!/usr/bin/python3
"""
    Empty class named Rectangle
"""


class Rectangle:
    """define Rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle."""
        self.height = height
        self.width = width

    def width(self):
        """return width"""
        return self.__width

    def width(self, value):
        """check error"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def height(self):
        """return height"""
        return self.__height

    def height(self, value):
        """check error"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.height = value
