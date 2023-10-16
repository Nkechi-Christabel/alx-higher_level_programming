#!/usr/bin/python3
""" """

import unittest
from models.square import Square

class TestSquareMethods(unittest.TestCase):
    def test_init(self):
        # Test initialization with valid arguments
        square = Square(4, 1, 2, 10)
        self.assertEqual(square.size, 4)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 2)
        self.assertEqual(square.id, 10)

        # Test initialization with missing optional arguments
        square2 = Square(4)
        self.assertEqual(square2.size, 4)
        self.assertEqual(square2.x, 0)  # Default value
        self.assertEqual(square2.y, 0)  # Default value

    def test_str(self):
        square = Square(4, 1, 2, 10)
        expected_output = "[Square] (10) 1/2 - 4"
        self.assertEqual(str(square), expected_output)

    def test_size_property(self):
        # Test valid size
        square = Square(4)
        square.size = 6
        self.assertEqual(square.size, 6)

        # Test invalid size (not an integer)
        with self.assertRaises(TypeError):
            square.size = "invalid"

        # Test invalid size (less than or equal to 0)
        with self.assertRaises(ValueError):
            square.size = 0

    def test_update(self):
        square = Square(4, 1, 2, 10)
        square.update(20, 6, 3, 4)
        self.assertEqual(square.id, 20)
        self.assertEqual(square.size, 6)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)

    def test_to_dictionary(self):
        square = Square(4, 1, 2, 10)
        expected_dict = {'id': 10, 'size': 4, 'x': 1, 'y': 2}
        self.assertEqual(square.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
