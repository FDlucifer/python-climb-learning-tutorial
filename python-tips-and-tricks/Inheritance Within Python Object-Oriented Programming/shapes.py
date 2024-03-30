import json


class JSONMixin:
    def to_json(self):
        return json.dumps(self.__dict__)


class Circle(JSONMixin):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color


class Rectangle(JSONMixin):
    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self.color = color
