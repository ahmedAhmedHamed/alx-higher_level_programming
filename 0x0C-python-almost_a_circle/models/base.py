#!/usr/bin/python3
"""module for 'Base' class"""
import json


class Base:
    """
    This class will be the “base” of all other classes in this project.
     The goal of it is to manage id attribute in all your
     future classes and to avoid duplicating the same code
     (by extension, same bugs)
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """transforms the list_dictionaries to a json"""
        if list_dictionaries is None or list_dictionaries == []:
            return '"[]"'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves the list_objs array to a file as a json"""
        new_list_objs = list_objs[:]
        if list_objs is None:
            new_list_objs = []
            list_type = list_objs.__class__.__name__
        else:
            list_type = list_objs[0].__class__.__name__

        for counter, obj in enumerate(list_objs):
            new_list_objs[counter] = obj.to_dictionary()

        obj_json = Base.to_json_string(new_list_objs)

        with open(str(list_type) + ".json", "w", encoding="utf-8") as file:
            file.write(obj_json)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Square':
            dummy_class = cls(3)
        if cls.__name__ == 'Rectangle':
            dummy_class = cls(3, 3)

        dummy_class.update(**dictionary)
        return dummy_class

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """saves to csv"""
        pass
    @classmethod
    def load_from_file_csv(cls):
        """loads from csv"""
        pass

    @classmethod
    def load_from_file(cls):
        class_name = cls.__name__
        with open(class_name + ".json", "r", encoding="utf-8") as file:
            all_lines = ""
            for line in file:
                all_lines += line.rstrip()
            if all_lines == "":
                return []
            dict_array = cls.from_json_string(all_lines)
            class_array = []
            for dict_instance in dict_array:
                class_array.append(cls.create(**dict_instance))
            return class_array
