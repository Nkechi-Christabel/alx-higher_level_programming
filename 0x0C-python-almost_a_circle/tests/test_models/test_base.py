#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from unittest.mock import patch

class TestBaseMethods(unittest.TestCase):
    def test_to_json_string(self):
        # Test with an empty list
        empty_list = []
        self.assertEqual(Base.to_json_string(empty_list), '[]')

        # Test with a list of dictionaries
        data = [{"id": 1, "name": "Object 1"}, {"id": 2, "name": "Object 2"}]
        self.assertEqual(Base.to_json_string(data), '[{"id": 1, "name": "Object 1"}, {"id": 2, "name": "Object 2"}]')

    def test_from_json_string(self):
        # Test with an empty JSON string
        empty_json = '[]'
        self.assertEqual(Base.from_json_string(empty_json), [])

        # Test with a JSON string containing data
        json_data = '[{"id": 1, "name": "Object 1"}, {"id": 2, "name": "Object 2"}]'
        expected_data = [{"id": 1, "name": "Object 1"}, {"id": 2, "name": "Object 2"}]
        self.assertEqual(Base.from_json_string(json_data), expected_data)

    def test_save_to_file(self):
        # Create a test instance and save it to a file
        obj = Base(1)
        Base.save_to_file([obj])
        
        # Read the contents of the saved file and check if it matches the expected JSON
        with open('Base.json', 'r') as f:
            file_contents = f.read()
        expected_json = '[{"id": 1}]'
        self.assertEqual(file_contents, expected_json)

    def test_load_from_file(self):
        # Create a test instance and save it to a file
        obj = Base(1)
        Base.save_to_file([obj])
        
        # Load data from the saved file and check if it matches the expected object
        loaded_objects = Base.load_from_file()
        expected_objects = [obj]
        self.assertEqual(loaded_objects, expected_objects)

    def test_create(self):
        # Test with a dictionary for a Rectangle
        rect_dict = {"id": 1, "width": 4, "height": 5, "x": 2, "y": 3}
        created_rect = Base.create(**rect_dict)
        self.assertEqual(created_rect.id, 1)
        self.assertEqual(created_rect.width, 4)
        self.assertEqual(created_rect.height, 5)
        self.assertEqual(created_rect.x, 2)
        self.assertEqual(created_rect.y, 3)

        # Test with a dictionary for a Square
        square_dict = {"id": 2, "size": 3, "x": 1, "y": 2}
        created_square = Base.create(**square_dict)
        self.assertEqual(created_square.id, 2)
        self.assertEqual(created_square.size, 3)
        self.assertEqual(created_square.x, 1)
        self.assertEqual(created_square.y, 2)

        # Test with an empty dictionary
        empty_dict = {}
        created_instance = Base.create(**empty_dict)
        self.assertEqual(created_instance.id, 3)  # Incremented ID for the empty dictionary

        # Test with a dictionary containing unexpected keys
        unexpected_keys_dict = {"id": 4, "length": 6}
        created_instance = Base.create(**unexpected_keys_dict)
        self.assertEqual(created_instance.id, 4)

    def test_save_and_load_to_file_csv(self):
        # Test with a list of Rectangle instances
        rect1 = Rectangle(1, 2, 3, 4, 5)
        rect2 = Rectangle(6, 7, 8, 9, 10)
        Base.save_to_file_csv([rect1, rect2])
        loaded_rectangles = Base.load_from_file_csv()
        self.assertEqual(loaded_rectangles, [rect1, rect2])

        # Test with a list of Square instances
        square1 = Square(11, 12, 13, 14)
        square2 = Square(15, 16, 17, 18)
        Base.save_to_file_csv([square1, square2])
        loaded_squares = Base.load_from_file_csv()
        self.assertEqual(loaded_squares, [square1, square2])

        # Test with an empty list
        Base.save_to_file_csv([])
        loaded_empty_list = Base.load_from_file_csv()
        self.assertEqual(loaded_empty_list, [])

    @patch('turtle.Screen', autospec=True)
    @patch('turtle.Turtle', autospec=True)
    def test_draw(self, mock_turtle, mock_screen):
        # Test the draw method
        Base.draw([], [])
        mock_screen.assert_called_with()
        mock_turtle.assert_called_with()

if __name__ == '__main__':
    unittest.main()
