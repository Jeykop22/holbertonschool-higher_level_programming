#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle."""
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(line_1, line_2):
        """Return the Rectangle with the greater area."""
        if not isinstance(line_1, Rectangle):
            raise TypeError("line_1 must be an instance of Rectangle")
        if not isinstance(line_2, Rectangle):
            raise TypeError("line_2 must be an instance of Rectangle")
        if line_1.area() >= line_2.area():
            return (line_1)
        return (line_2)

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle with width and height equal to size."""
        return (cls(size, size))

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        line = []
        for i in range(self.__height):
            [line.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                line.append("\n")
        return ("".join(line))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        line = "Rectangle(" + str(self.__width)
        line += ", " + str(self.__height) + ")"
        return (line)

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
