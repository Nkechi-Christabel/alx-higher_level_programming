#!/usr/bin/python3
"""
Test cases for the Square class in models.square module.
"""

import unittest
import io
import contextlib
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle

class TestSquareMethods(unittest.TestCase):
    """
    A class to test the Square Class
    """
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_inits(self):
        """Test initialization with valid arguments"""
        s0 = Square(1)
        self.assertEqual(s0.id, 1)
        s1 = Square(5, 3, 4)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 4)
        self.assertEqual(s1.id, 2)

        """Test initialization check for size attribute."""
        s1 = Square(8)
        self.assertEqual(s1.size, 8)
        s2 = Square(9, 8, 7, 2)
        self.assertEqual(s2.size, 9)
	
        """Test initialization with the wrong attributes."""
        with self.assertRaises(TypeError) as x:
            s = Square("Hello", 2)
        self.assertEqual("width must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            s = Square(2, "World")
        self.assertEqual("x must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            s = Square(1, 2, "Foo", 3)
        self.assertEqual("y must be an integer", str(x.exception))
        with self.assertRaises(ValueError) as x:
            s = Square(0, 2)
        self.assertEqual("width must be > 0", str(x.exception))
        with self.assertRaises(ValueError) as x:
            s = Square(-1)
        self.assertEqual("width must be > 0", str(x.exception))
        with self.assertRaises(ValueError) as x:
            s = Square(2, -3)
        self.assertEqual("x must be >= 0", str(x.exception))
        with self.assertRaises(ValueError) as x:
            s = Square(2, 5, -5, 6)
        self.assertEqual("y must be >= 0", str(x.exception))

        """Test initialization with missing optional arguments"""
        square2 = Square(4)
        self.assertEqual(square2.size, 4)
        self.assertEqual(square2.x, 0)  # Default value
        self.assertEqual(square2.y, 0)  # Default value

        """Test initialization check for missing arguments"""
        with self.assertRaises(TypeError) as x:
            s1 = Square()
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'size'", str(
                x.exception))

    def test_str(self):
        """Test the string representation of a Square."""
        s1 = Square(9, 4, 5, 6)
        self.assertEqual(str(s1), "[Square] (6) 4/5 - 9")

    def test_square_inheritance_and_instances(self):
        """Test the Square class for inheritance and instance relationships.
    
        This test case checks the Square class for its inheritance from Rectangle
        and verifies the relationships between instances and classes.
	"""
        s1 = Square(6)
        self.assertTrue(isinstance(s1, Rectangle))
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertFalse(isinstance(Square, Rectangle))
        self.assertTrue(isinstance(s1, Base))
        self.assertTrue(issubclass(Square, Base))
        self.assertFalse(isinstance(Square, Base))

    def test_square_inheritance_and_methods(self):
        """Test the Square class for inheritance and methods inherited from Rectangle.
    
        This test case checks the Square class for its inheritance from Rectangle
        and the behavior of methods inherited from Rectangle.
	"""
        s1 = Square(9)
        self.assertEqual(s1.area(), 81)
        s2 = Square(4, 1, 2, 5)
        s2.update(7)
        self.assertEqual(s2.id, 7)
        f = io.StringIO()
        s3 = Square(4)
        with contextlib.redirect_stdout(f):
            s3.display()
        s = f.getvalue()
        res = "####\n####\n####\n####\n"
        self.assertEqual(s, res)

    def test_update(self):
        """Test the update method of Square."""
        s1 = Square(5)
        s1.update(10)
        self.assertEqual(s1.id, 10)
        s1.update(x=12)
        self.assertEqual(s1.x, 12)
        s1.update(size=7, id=89, y=1)
        self.assertEqual(s1.size, 7)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.y, 1)
        s1.update()
        self.assertEqual(s1.size, 7)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.y, 1)

        """Test update method on Square with the wrong types."""
        s1 = Square(9)
        with self.assertRaises(TypeError) as x:
            s1.update(2, 3, 4, "hello")
        self.assertEqual("y must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            s1.update("hello", 8, 9)
        self.assertEqual("id must be an integer", str(x.exception))

    def test_to_dictionary(self):
        """Test for public method to_dictionary."""
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        s_dictionary = {'x': 2, 'y': 1, 'id': 1, 'size': 10}
        self.assertEqual(len(s1_dictionary), len(s_dictionary))
        self.assertEqual(type(s1_dictionary), dict)
        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        s2_dictionary = s2.to_dictionary()
        self.assertEqual(len(s1_dictionary), len(s2_dictionary))
        self.assertEqual(type(s2_dictionary), dict)
        self.assertFalse(s1 == s2)

        """Test for public method to_dictionary with wrong args."""
        s = "to_dictionary() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as x:
            s1 = Square(10, 2, 1, 9)
            s1_dictionary = s1.to_dictionary("Hi")
        self.assertEqual(s, str(x.exception))


if __name__ == '__main__':
    unittest.main()
