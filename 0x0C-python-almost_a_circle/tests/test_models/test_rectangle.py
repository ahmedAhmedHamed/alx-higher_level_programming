#!/usr/bin/python3
"""this is the test file for the 'Rectangle' class"""
import unittest
from unittest.mock import patch
from io import StringIO
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """here are the unit tests for 'Rectangle'"""

    def test_rectangle_default_initialisation(self):
        """tests initialisation with default id"""
        rectangle = Rectangle(1, 2)
        self.assertEqual(rectangle.height, 2)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(rectangle.x, 0)
        self.assertEqual(rectangle.y, 0)
        self.assertTrue(isinstance(rectangle, Rectangle))

    def test_rectangle_full_initialisation(self):
        """tests initialisation with id"""
        rectangle = Rectangle(1, 2, 1, 7, 9)
        self.assertEqual(rectangle.height, 2)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(rectangle.x, 1)
        self.assertEqual(rectangle.y, 7)
        self.assertEqual(rectangle.id, 9)

    def test_rectangle_missing_width(self):
        """tests missing width arg"""
        with self.assertRaises(TypeError):
            Rectangle(height=1)

    def test_rectangle_missing_height(self):
        """tests missing height arg"""
        with self.assertRaises(TypeError):
            Rectangle(width=1)

    def test_rectangle_wrong_type_width(self):
        """tests using the wrong type (non-integer) for width"""
        with self.assertRaises(TypeError):
            Rectangle(None, 2)

    def test_rectangle_wrong_type_height(self):
        """tests using the wrong type (non-integer) for height"""
        with self.assertRaises(TypeError):
            Rectangle(1, str)

    def test_rectangle_wrong_type_x(self):
        """tests using the wrong type (non-integer) for x"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, [])

    def test_rectangle_wrong_type_y(self):
        """tests using the wrong type (non-integer) for y"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, {})

    def test_rectangle_wrong_value_height(self):
        """tests using the wrong value (<= 0) for height"""
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_rectangle_wrong_value_width(self):
        """tests using the wrong value (<= 0) for width"""
        with self.assertRaises(ValueError):
            Rectangle(0, 1)

    def test_rectangle_wrong_value_x(self):
        """tests using the wrong value (< 0) for x"""
        with self.assertRaises(ValueError):
            Rectangle(1, 1, -1)

    def test_rectangle_wrong_value_y(self):
        """tests using the wrong value (< 0) for y"""
        with self.assertRaises(ValueError):
            Rectangle(0, 1, 1, -2)

    def test_rectangle_area(self):
        """tests the area function for the rectangle"""
        rectangle = Rectangle(3, 2)
        self.assertEqual(6, rectangle.area())

    def test_rectangle_display(self):
        """tests the display function on stdout"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            Rectangle(1, 2, 1, 1).display()
            self.assertEqual(fake_out.getvalue(), "\n #\n #\n")

    def test_rectangle_print(self):
        """tests printing the rectangle using __str__"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(4, 6, 2, 1, 12)
            print(r1)
            self.assertEqual(fake_out.getvalue(),
                             "[Rectangle] (12) 2/1 - 4/6\n")

    def test_rectangle_str(self):
        """tests the returned value when using __str__"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")

    def test_rectangle_update_args(self):
        """tests using update with args"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(98, 19, 2, 3, 4)
        self.assertEqual(r1.id, 98)
        self.assertEqual(r1.width, 19)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

    def test_rectangle_update_kwargs(self):
        """tests using update with kwargs"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(y=1, width=2, x=3, id=89, height=30)
        self.assertEqual(r1.y, 1)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.height, 30)
        self.assertEqual(r1.width, 2)

    def test_rectangle_to_dictionary(self):
        """tests to dictionary function"""
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        dictionary = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(r1_dictionary, dictionary)
