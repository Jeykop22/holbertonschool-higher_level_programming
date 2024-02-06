#!/usr/bin/python3
"""modul for the first task, Write a function that adds 2 integers."""


def add_integer(a, b=98):
    """return int sum of a and b if they are int or float"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a + b)


if __name__ == '__main__':
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
