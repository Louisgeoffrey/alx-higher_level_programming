#!/usr/bin/python3

"""Define a magicClass matching exactly a bytecode provided by Holberton"""

import math

class magicClass:
    """Represent a circle"""

    def __init__(self, radius=0):
        """Initialize a magicClass.

        Args:
            radius (float or int): The radius of the new magicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the magicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return the circumference of the magicClass."""
        return (2 * math.pi * self.__radius)
