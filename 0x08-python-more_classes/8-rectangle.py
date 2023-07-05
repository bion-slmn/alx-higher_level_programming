#!/usr/bin/python3
'''This module creates a rectangle class'''


class Rectangle:
    '''creates a class rectangle with width
    abd height'''
    number_of_instances = 0
    print_symbol = str('#')

    def __init__(self, width=0, height=0):
        '''intialises width and height with default 0
        Args:
            width(int):the width of the rectangle
            height(int): the height of the rectangle
            self: the object instance
        '''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        '''sets the width'''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        '''returns the height '''
        return self.__height

    @height.setter
    def height(self, value):
        '''sets the height attribute'''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    def area(self):
        '''calculates the area of the rectangle'''
        return (self.__width * self.__height)

    def perimeter(self):
        '''calculates the perimeter of the rectangle'''
        if self.__height == 0 or self.__width == 0:
            return 0

        return 2 * (self.__height + self.__width)

    def __str__(self):
        '''prints the the rectangle with #'''
        if self.__height == 0 or self.__width == 0:
            return ""

        for x in range(self.__height):
            for _ in range(self.__width):
                print(str(self.print_symbol), end="")
            if x != self.__height - 1:
                print()

        return ""

    def __repr__(self):
        '''return a string representation of the rectangle
        to be able to recreate a new instance by eval'''
        return f"{type(self).__name__}({self.__width}, {self.__height})"

    def __del__(self):
        ''' delete an object'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''Returns the biggest rectangle based on the area'''
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')

        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        if Rectangle.area(rect_1) >= Rectangle.area(rect_2):
            return rect_1
        else:
            rect_2
