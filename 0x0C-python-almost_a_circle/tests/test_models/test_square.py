#!/usr/bin/python3
"""this is the test file for the 'Square' class"""
import unittest
from unittest.mock import patch
from io import StringIO
from models.square import Square


class TestBase(unittest.TestCase):
    """here are the unit tests for 'Square'"""

    def test_square_initialisation(self):
        square = Square(5, 1, 2, 3)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 2)
        self.assertEqual(square.id, 3)
        self.assertEqual(square.size, 25)

    def test_square_size(self):
        square = Square(5, 1, 2, 3)
        self.assertEqual(square.size, 25)

    def test_square_update_args(self):
        square = Square(5, 1, 2, 3)
        square.update(1, 2, 3, 4)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.width, 2)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)

    def test_square_update_args_ignore_kwargs(self):
        """update method should ignore kwargs if args exist"""
        square = Square(5, 1, 2, 3)
        square.update(1, 2, 3, 4, x=77, size=7, id=89, y=1)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.width, 2)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)

    def test_square_update_kwargs(self):
        """update method should ignore kwargs if args exist"""
        square = Square(5, 1, 2, 3)
        square.update(x=77, size=7, id=89, y=1)
        self.assertEqual(square.id, 89)
        self.assertEqual(square.width, 7)
        self.assertEqual(square.x, 77)
        self.assertEqual(square.y, 1)
    def test_square_print(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s1 = Square(5, id=1)
            print(s1)
            self.assertEqual(fake_out.getvalue(), "[Square] (1) 0/0 - 5\n")

    def test_square_str(self):
        s1 = Square(5, id=2)
        self.assertEqual(s1.__str__(), "[Square] (2) 0/0 - 5")

    def test_square_to_dictionary(self):
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        dictionary = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(s1_dictionary, dictionary)
