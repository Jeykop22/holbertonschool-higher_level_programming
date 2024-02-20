#!/usr/bin/python3
"""create a base class"""


class Base:
    """define a base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor for base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
