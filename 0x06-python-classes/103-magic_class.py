#!/usr/bin/python3
'''"Define a MagicClass matching exactly a bytecode provided'''
import math


class MagicClass:
    """Represent a circle."""
    def __init__(self, radius=0):
        '''intilize a circle

        Args:
            radius (int or float):  The radius of the new MagicClass.'''
        self.__radius = 0

        if (type(radius) is not int) and (type(radius) is not float):
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self, radius):
        '''the area of the circle'''
        return ((self.__radius ** 2) * (math.pi))

    def circumference(self, radius):
        '''circumfrance of a circlie'''
        return (2 * math.pi * self.__radius)
