#!/usr/bin/python3
"""
    Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inheriths from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """init method"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str method"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.width = width
        self.height = width

    def update(self, *args, **kwargs):
        """ learning *args """
        if (len(args) != 0):
            counter = 0
            atrs = ['id', 'width', 'x', 'y']
            for arg in args:
                setattr(self, atrs[counter], arg)
                counter += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns dictionary"""
        tmpdic = {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
        return tmpdic
