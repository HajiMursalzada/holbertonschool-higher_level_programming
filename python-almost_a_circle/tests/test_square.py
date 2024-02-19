#!/usr/bin/python3
"""Square test module"""


import unittest
from models.square import Square
import os

class TestBase(unittest.TestCase):
    def test_square_positive_num(self):
        square = Square(1, 2, 3, 4)
        self.assertEquals(square.size, 1)

        square = Square(1, 2, 3)
        self.assertEquals(square.y, 3)

        square = Square(1, 2)
        self.assertEquals(square.x, 2)

    def test_square_string(self):
        with self.assertRaises(TypeError):
            Square(1, 2, "3")
        with self.assertRaises(TypeError):
            Square(1, "2")
        with self.assertRaises(TypeError):
            Square("1")

    def test_value_error(self):
        with self.assertRaises(ValueError):
            Square(1, 2, -3)
        with self.assertRaises(ValueError):
            Square(0)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(-1)

    def test_str(self):
        square = Square(1, id=1)
        self.assertEqual(str(square), "[Square] (1) 0/0 - 1")

    def test_to_dictionary(self):
        square = Square(10, 2, 1, 1)
        self.assertEqual(
                square.to_dictionary(), {'id': 1, 'x': 2, 'size': 10, 'y': 1})

    def test_update(self):
        square = Square(5)
        square.update(size=7)
        self.assertEqual(square.size, 7)

    def test_create(self):
        square = Square.create(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 })
        self.assertEqual(square.id, 89)
    
    def test_save_to_file(self):
        try:
            os.remove("Square.json")
        except:
            pass
        
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")


        try:
            os.remove("Square.json")
        except:
            pass

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")


        try:
            os.remove("Square.json")
        except:
            pass

        Square.save_to_file([Square(1, id=1)])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), '[{"id": 1, "x": 0, "size": 1, "y": 0}]')

    def test_load_from_file(self):
        try:
            os.remove("Square.json")
        except:
            pass
        self.assertEqual(Square.load_from_file(), [])
