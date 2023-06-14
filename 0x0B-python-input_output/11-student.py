#!/usr/bin/python3
"""second iteration of the student class"""


class Student:
    """the class of the student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """makes the class into a json using only attrs"""
        variables = vars(self)
        my_dictionary = {}

        if isinstance(attrs, list):
            for attribute in attrs:
                if not isinstance(attribute, str):
                    return variables

                if attribute in variables:
                    my_dictionary[attribute] = variables[attribute]
            return my_dictionary
        return variables

    def reload_from_json(self, json):
        """makes student equal to the json"""
        for variable in json:
            vars(self)[variable] = json[variable]
