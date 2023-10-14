#!/usr/bin/python3
"""This module(base.py) defines a class Base."""

import json
import csv

class Base:
    """
    The Base class represents the base of a geometric shape.

    Attributes:
        __nb_objects (int): A private class attribute that keeps
        track of the number of instances created.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new instance of the Base class.

        Args:
            id (int, optional): An identifier for the instance. If not
            provided, a unique ID is assigned.

        Attributes:
            id (int): The identifier for the instance.
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries to be converted
            to JSON.

        Returns:
            str: JSON string representation of the list of dictionaries.
        """
        return json.dumps(list_dictionaries) if list_dictionaries else '[]'

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of a list of instances to a file.

        Args:
            list_objs (list): A list of instances to be saved to a JSON file.

        Notes:
            If list_objs is None, an empty list is saved.

        The filename will be "<Class name>.json" (e.g., "Rectangle.json").
        """
        filename = filename = cls.__name__ + ".json"
        json_str = (cls.to_json_string([obj.to_dictionary() for obj in
                    list_objs]) if list_objs else '[]')
        with open(filename, "w", encoding="utf-8") as f:
            return f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """
        Return a list from a JSON string representation.

        Args:
            json_string (str): A string representing a list of dictionaries.

        Returns:
            list: A list represented by the JSON string.

        Notes:
            If json_string is None or empty, an empty list is returned.
        """
        return json.loads(json_string) if json_string else '[]'

    @classmethod
    def create(cls, **dictionary):
        """
        Create and return an instance with all attributes set based on a
        dictionary.

        Args:
            **dictionary: A dictionary containing attribute values for the
            instance.

        Returns:
            cls: An instance of the class with attributes set based on the
            dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(2, 2)
        elif cls.__name__ == "Square":
            dummy = cls(2)
        else:
            dummy = cls()

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Return a list of instances loaded from a JSON file.

        Returns:
            list: A list of instances loaded from a JSON file.

        Notes:
            The filename is based on the class name, e.g., "Rectangle.json".
            If the file doesn't exist, an empty list is returned.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                dictionaries = cls.from_json_string(json_string)
                return [cls.create(**d) for d in dictionaries]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serialize and save a list of instances to a CSV file.

        Args:
            list_objs (list): A list of instances to be saved in CSV format.
        """
        filename = cls.__name__ + ".csv"

        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)

            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.width, obj.height, obj.x,
                                    obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserialize and load a list of instances from a CSV file.

        Returns:
            list: A list of instances loaded from the CSV file.
        """
        filename = cls.__name__ + ".csv"

        instances = []
        try:
            with open(filename, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    row = [int(value) for value in row]
                    if cls.__name__ == "Rectangle":
                        instances.append(cls.create(id=row[0], width=row[1],
                                         height=row[2], x=row[3], y=row[4]))
                    elif cls.__name__ == "Square":
                        instances.append(cls.create(id=row[0], size=row[1],
                                         x=row[2], y=row[3]))
        except FileNotFoundError:
            pass

        return instances
