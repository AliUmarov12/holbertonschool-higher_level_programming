#!/usr/bin/python3
"""Defines a Rectangle class with width and height."""


class Rectangle:
    """Class that defines a rectangle by width and height."""

    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """klsfnd"""
        return self.__width * self.__height

    def perimeter(self):
        """lksdn"""
        if self.__width == 0 or self.__height:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """jkfdjfn"""
        if self.__width == 0 or self.__height == 0:
            return ''
        lines = ['#' * self.__width for i in range(self.__height)]
        return '\n'.join(lines)
