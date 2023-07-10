#!/usr/bin/python3
'''Rectangle class inherits from the basegeomety'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''inherits from baseGeometry'''
    def __init__(self, width, height):
        ''' intialize height and  width
        Args:
            height(int): must be positive ints
            width(int): must be positive'''
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        '''calculates the area of the rectangle'''
        return self.__height * self.__width

    def __str__(self):
        '''prints the elaborate infor on the rectangle'''
        return f'[Rectangle] {self.__width}/{self.__height}'
