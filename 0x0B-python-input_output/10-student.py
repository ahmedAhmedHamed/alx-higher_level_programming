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



student_1 = Student("John", "Doe", 23)
student_2 = Student("Bob", "Dylan", 27)

j_student_1 = student_1.to_json()
j_student_2 = student_2.to_json(['first_name', 'age'])
j_student_3 = student_2.to_json(['middle_name', 'age'])

print(j_student_1)
print(j_student_2)
print(j_student_3)