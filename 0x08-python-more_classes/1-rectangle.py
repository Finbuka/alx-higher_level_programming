#!/usr/bin/python3
""" A Rectangle module"""


class Rectangle:
    """Reprsents a Rectangle
    private instance attribute : width, height
        - property def width(self)
        - property setter def width(self)
        - property def height(self)
        - property setter def height(self)
    """

    def __init__(self, width=0, height=0):
        """Initializes the object/instance"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width"""
        if type(value) is not int:
            raise TypeError
        elif value < 0:
            raise ValueError
        self.__width = value

    @property
    def height(self):
        """Retrieves the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height"""
        if type(value) is not int:
            raise TypeError
        elif value < 0:
            raise ValueError
        self.__height = value
