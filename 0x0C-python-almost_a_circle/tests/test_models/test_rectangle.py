#!/usr/bin/python3
"""
Test cases for the Rectangle class in models.rectangle module.
"""
import unittest
from models.rectangle import Rectangle

class TestRectangleMethods(unittest.TestCase):
    """
    A class to test methods and behaviors of the Rectangle class.
    """
        def test_init(self):
        """
        Test the initialization of a Rectangle.

        Case 1: Test initialization with valid arguments.
        """
        rect = Rectangle(4, 5, 1, 2, 10)
        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 2)
        self.assertEqual(rect.id, 10)

        """
        Case 2: Test initialization with missing optional arguments.
        """
        rect2 = Rectangle(4, 5)
        self.assertEqual(rect2.width, 4)
        self.assertEqual(rect2.height, 5)
        self.assertEqual(rect2.x, 0)  # Default value
        self.assertEqual(rect2.y, 0)  # Default value

    def test_width_property(self):
        """
        Test the width property of a Rectangle.

        Case 1: Test valid width.
        """
        rect = Rectangle(4, 5)
        rect.width = 6
        self.assertEqual(rect.width, 6)

        """
        Case 2: Test invalid width (not an integer).
        """
        with self.assertRaises(TypeError):
            rect.width = "invalid"

        """
        Case 3: Test invalid width (less than or equal to 0).
        """
        with self.assertRaises(ValueError):
            rect.width = 0

    def test_height_property(self):
        """
        Test the height property of a Rectangle.

        Case 1: Test valid height.
        """
        rect = Rectangle(4, 5)
        rect.height = 7
        self.assertEqual(rect.height, 7)

        """
        Case 2: Test invalid height (not an integer).
        """
        with self.assertRaises(TypeError):
            rect.height = "invalid"

        """
        Case 3: Test invalid height (less than or equal to 0).
        """
        with self.assertRaises(ValueError):
            rect.height = 0

    def test_x_property(self):
        """
        Test the x property of a Rectangle.

        Case 1: Test valid x.
        """
        rect = Rectangle(4, 5)
        rect.x = 2
        self.assertEqual(rect.x, 2)

        """
        Case 2: Test invalid x (not an integer).
        """
        with self.assertRaises(TypeError):
            rect.x = "invalid"

        """
        Case 3: Test invalid x (less than 0).
        """
        with self.assertRaises(ValueError):
            rect.x = -1

    def test_y_property(self):
        """
        Test the y property of a Rectangle.

        Case 1: Test valid y.
        """
        rect = Rectangle(4, 5)
        rect.y = 3
        self.assertEqual(rect.y, 3)

        """
        Case 2: Test invalid y (not an integer).
        """
        with self.assertRaises(TypeError):
            rect.y = "invalid"

        """
        Case 3: Test invalid y (less than 0).
        """
        with self.assertRaises(ValueError):
            rect.y = -1

    def test_area(self):
        """
        Test the area method of a Rectangle.
        """
        rect = Rectangle(4, 5)
        self.assertEqual(rect.area(), 20)

    def test_display(self):
        """
        Test the display method of a Rectangle.
        """
        rect = Rectangle(3, 2)
        expected_output = "###\n" \
                          "###\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            rect.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str(self):
        """
        Test the string representation of a Rectangle.
        """
        rect = Rectangle(4, 5, 1, 2, 10)
        expected_output = "[Rectangle] (10) 1/2 - 4/5"
        self.assertEqual(str(rect), expected_output)

    def test_update(self):
        """
        Test the update method of a Rectangle.
        """
        rect = Rectangle(4, 5, 1, 2, 10)
        rect.update(20, 6, 7, 3, 4)
        self.assertEqual(rect.id, 20)
        self.assertEqual(rect.width, 6)
        self.assertEqual(rect.height, 7)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_to_dictionary(self):
        """
        Test the to_dictionary method of a Rectangle.
        """
        rect = Rectangle(4, 5, 1, 2, 10)
        expected_dict = {'id': 10, 'width': 4, 'height': 5, 'x': 1, 'y': 2}
        self.assertEqual(rect.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
