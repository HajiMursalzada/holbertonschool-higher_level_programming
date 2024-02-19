import unittest
import io
import os
import json

from contextlib import redirect_stdout

from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.rect = Rectangle(5, 10, 15, 20, 25)
        self.test_cases = [
            {"params": (1, 2), "expected": (1, 2, 0, 0)},
            {"params": (1, 2, 3), "expected": (1, 2, 3, 0)},
            {"params": (1, 2, 3, 4), "expected": (1, 2, 3, 4)},
        ]

    def test_attributes(self):
        self.assertEqual(self.rect.width, 5)
        self.assertEqual(self.rect.height, 10)
        self.assertEqual(self.rect.x, 15)
        self.assertEqual(self.rect.y, 20)
        self.assertEqual(self.rect.id, 25)

    def test_area(self):
        self.assertEqual(self.rect.area(), 50)

    def test_to_dictionary(self):
        expected = {"x": 15, "y": 20, "id": 25, "height": 10, "width": 5}
        self.assertEqual(self.rect.to_dictionary(), expected)

    def test_update(self):
        self.rect.update(30, 35, 40, 45, 50)
        self.assertEqual(self.rect.width, 35)
        self.assertEqual(self.rect.height, 40)
        self.assertEqual(self.rect.x, 45)
        self.assertEqual(self.rect.y, 50)
        self.assertEqual(self.rect.id, 30)

    def test_invalid_width(self):
        with self.assertRaises(TypeError):
            self.rect.width = "invalid"

    def test_invalid_height(self):
        with self.assertRaises(TypeError):
            self.rect.height = "invalid"

    def test_invalid_x(self):
        with self.assertRaises(TypeError):
            self.rect.x = "invalid"

    def test_invalid_y(self):
        with self.assertRaises(TypeError):
            self.rect.y = "invalid"

    def test_rectangle_initialization(self):
        for test_case in self.test_cases:
            rect = Rectangle(*test_case["params"])
            self.assertEqual((rect.width, rect.height, rect.x, rect.y), test_case["expected"])

    def test_invalid_initialization(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_str(self):
        self.assertEqual(str(self.rect), "[Rectangle] (25) 15/20 - 5/10")

    def test_display_without_x_y(self):
        self.rect.x = 0
        self.rect.y = 0
        expected_output = "\n".join(["#"*5 for _ in range(10)]) + "\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            self.rect.display()
            self.assertEqual(buf.getvalue(), expected_output)

    def test_display_without_y(self):
        self.rect.x = 15
        self.rect.y = 0
        expected_output = "\n".join([" "*15 + "#"*5 for _ in range(10)]) + "\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            self.rect.display()
            self.assertEqual(buf.getvalue(), expected_output)

    def test_display(self):
        expected_output = "\n"*20 + "\n".join([" "*15 + "#"*5 for _ in range(10)]) + "\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            self.rect.display()
            self.assertEqual(buf.getvalue(), expected_output)

    def test_create(self):
        rect_dict = {'id': 89, 'width': 10, 'height': 20, 'x': 2, 'y': 3}
        rect = Rectangle.create(**rect_dict)
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_empty(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", mode="r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file(self):
        rect = Rectangle(1, 2)
        Rectangle.save_to_file([rect])
        with open("Rectangle.json", "r") as file:
            content = json.load(file)
            self.assertEqual(content, [rect.to_dictionary()])

    def test_load_from_file_no_file(self):
        rectangles = Rectangle.load_from_file()
        self.assertEqual(rectangles, [])

    def test_load_from_file(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([rect])
        rectangles = Rectangle.load_from_file()
        self.assertEqual(len(rectangles), 1)
        self.assertEqual(rectangles[0].to_dictionary(), rect.to_dictionary())

    def tearDown(self):
        """This method is called after each test"""

        try:
            os.remove("Rectangle.json")
        except:
            pass

if __name__ == '__main__':
    unittest.main()
