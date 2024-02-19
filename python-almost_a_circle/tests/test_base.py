#!usr/bin/python3
'''
Unit tests
Module Documentation
'''


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    def test_id_none(self):
        b = Base()
        self.assertEqual(b.id, 2)

    def test_id_positive(self):
        b = Base(3)
        self.assertEqual(b.id, 3)

    def test_id_negative(self):
        b = Base(-3)
        self.assertEqual(b.id, -3)

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), '[]')
        self.assertEqual(Base.to_json_string([]), '[]')
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string('[]'), [])
        self.assertEqual(Base.from_json_string('[{ "id": 89}]'), [{"id": 89}])


if __name__ == '__main__':
    unittest.main()
