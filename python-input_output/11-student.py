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

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance based on a dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
