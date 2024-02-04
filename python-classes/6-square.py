#!/usr/bin/python3
"""This file contains Square class inside."""


class Square():
    """Documentation for Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """Init block of Square Class"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """size function that returns private size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Size function for set value for size of square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """position property that retrieve position"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets value for position."""
        if not (isinstance(value, tuple)
           and len(value) == 2
           and isinstance(value[0], int)
           and isinstance(value[1], int)
           and value[0] >= 0
           and value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Area mothod that calculates area of square"""
        return self.__size ** 2

    def my_print(self):
        """Prints area using # sign"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()

            for i in range(self.size):
                for j in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
