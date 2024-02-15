#!/usr/bin/python3
"""
    Function that appends a string to a text file (UTF8)
    and returns the number of characters written
"""


def append_write(filename="", text=""):
    """
        Function that appends a string to a text file (UTF8)
        and returns the number of characters written
    """
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(text)
        return len(text)
