#!/usr/bin/python3
"""this is the test file for the 'Base' class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """here are the unit tests for 'Base'"""

    def test_base_id_default_multiple(self):
        """checks the default id setting for base"""
        base = Base()
        self.assertEqual(base.id, 1)
        base = Base()
        self.assertEqual(base.id, 2)
        base = Base()
        self.assertEqual(base.id, 3)
        base = Base()
        self.assertEqual(base.id, 4)

    def test_base_id_setting_positive(self):
        """checks setting base id with a positive int"""
        base = Base(2)
        self.assertEqual(base.id, 2)
        base = Base(40)
        self.assertEqual(base.id, 40)
        base = Base(999999999)
        self.assertEqual(base.id, 999999999)

    def test_base_id_setting_negative(self):
        """checks setting base id with a negative int"""
        base = Base(2)
        self.assertEqual(base.id, 2)
        base = Base(-40)
        self.assertEqual(base.id, -40)
        base = Base(-999999999)
        self.assertEqual(base.id, -999999999)

    def test_base_id_infinity(self):
        """checks setting base id with infinity"""
        base = Base(23e23)
        self.assertEqual(base.id, 23e23)

    def test_base_id_setting_string(self):
        """checks setting base id with string"""
        base = Base("hello")
        self.assertEqual(base.id, "hello")

    def test_base_id_setting_array(self):
        """checks setting base id with array"""
        base = Base([2, 3, 4])
        self.assertEqual(base.id, [2, 3, 4])

    def test_base_is_base(self):
        """checks if base is instance of Base"""
        base = Base(1)
        self.assertEqual(type(base), Base)
        self.assertTrue(isinstance(base, Base))

    def test_dictionary_to_json_string_none(self):
        """tests using to json string with none arg"""
        self.assertEqual(Base.to_json_string(None), '"[]"')

    def test_dictionary_to_json_string_empty(self):
        """tests using to json string with empty arr arg"""
        self.assertEqual(Base.to_json_string([]), '"[]"')

    def test_dictionary_to_json_string_correct(self):
        """tests using to json string with dict arg"""
        json_dictionary = Base.to_json_string(
            [{'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}])
        self.assertEqual(
            json_dictionary,
            '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]')

