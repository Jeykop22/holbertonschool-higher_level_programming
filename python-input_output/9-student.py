#!/usr/bin/python3
"""
A simple class representing a Student and a method
to convert its attributes to a JSON-like dictionary.
"""


class Student:
    """
    Represents a Student with first name, last name, and age attributes.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a new instance of the Student class.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Converts the student object to a JSON-like dictionary.
        """
        return self.__dict__
