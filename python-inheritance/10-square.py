#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square that inherits from Rectangle"""

    def __init__(self, size):
        """Initialize square with validated size"""
        # size müsbət tam olmalıdır — Rectangle-in parent classı BaseGeometry yoxlayır
        self.integer_validator("size", size)
        self.__size = size

        # Rectangle konstruktorunu width və height eyni olaraq çağırırıq
        super().__init__(size, size)

    def area(self):
        """Return area of the square"""
        return self.__size * self.__size
