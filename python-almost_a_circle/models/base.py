#!/usr/bin/python3
"""modul for create a Base class"""
import json


class Base:
    """Base class mother of all other clss of this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Manage the id attribute for all classes

        Args:
            id: id of the instance. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file
        list_objs is a list of instances who inherits of Base
        filename is <class name>.json"""
        filename = cls.__name__ + ".json"
        listOf = []
        if list_objs is not None:
            for object in list_objs:
                listOf.append(cls.to_dictionary(object))
        with open(filename, 'w') as jsonFileSaved:
            jsonFileSaved.write(cls.to_json_string(listOf))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(3, 4)
        elif cls.__name__ == "Square":
            dummy = cls(3)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances from a json file"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as jsonFileSaved:
                listOfInstance = Base.from_json_string(jsonFileSaved.read())
                return [cls.create(**instance) for instance in listOfInstance]
        except IOError:
            return []
