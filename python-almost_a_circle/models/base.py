#!/usr/bin/python3
'''
Model Documentation
'''

import json
import turtle


class Base:
    '''
    class Documentation
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''
        Method Documentation
        '''
        __class__.__nb_objects += 1
        if id is not None:
            self.id = id
        else:
            self.id = __class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        Method Documentation.
        '''
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        Method Documentation
        '''
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list = [obj.to_dictionary() for obj in list_objs]
                jsonfile.write(Base.to_json_string(list))

    @staticmethod
    def from_json_string(json_string):
        '''
        Method Documentation
        '''
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''
        Method Documentation
        '''
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as jsonfile:
                JsonString = jsonfile.read()
                new_dict = cls.from_json_string(JsonString)
                new_list = []
                for o in new_dict:
                    obj = cls.create(**o)
                    new_list.append(obj)
                return new_list
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        '''
        Method Documentation
        '''
        screen = turtle.Screen()
        screen.setup(width=800, height=600)

        t = turtle.Turtle()

        for rect in list_rectangles:
            t.penup()
            t.goto(rect.x, rect.y)
            t.pendown()
            t.forward(rect.width)
            t.left(90)
            t.forward(rect.height)
            t.left(90)
            t.forward(rect.width)
            t.left(90)
            t.forward(rect.height)
            t.left(90)

        for square in list_squares:
            t.penup()
            t.goto(square.x, square.y)
            t.pendown()
            for _ in range(4):
                t.forward(square.width)
                t.left(90)

        screen.mainloop()
