#!/usr/bin/python3
"""
    Empty class named Rectangle
"""


class Rectangle:
    """define Rectangle"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    def width(self):
        return self.__width
    
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def height(self):
        return self.__height

    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.height = value
