#!/usr/bin/python3
'''define a class square'''


class Square:
    '''The square is defined by:
    Private instance attribute: size
    Instantiation with optional size'''
    def __init__(self, size=0):
        '''Initialize a new Square.

        Args:
            size (:obj:`int`, optional): is the size of a square
        '''
        self.__size = size

    @property
    def size(self):
        '''Retrive the size value

        Return:
            the size private instance)'''
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        '''calculates the area of a square

        Args:
            size (int): the size of the square

        Return:
            int: the area of the square'''
        return self.__size ** 2

    def __eq__(self, other):
        '''adding equal sign operator'''
        if self.area() == other.area():
            return True
        else:
            return False

    def __ne__(self, other):
        ''' not equal functionality'''
        if self.area() != other.area():
            return True
        else:
            return False

    def __gt__(self, other):
        '''greater that functionality'''
        if self.area() > other.area():
            return True
        else:
            return False

    def __lt__(self, other):
        '''less than functionality'''
        if self.area() < other.area():
            return True
        else:
            return False

    def __ge__(self, other):
        '''greater than or equal to functionality'''
        if self.area() >= other.area():
            return True
        else:
            return False

    def __le__(self, other):
        '''less than  or equal tofunctionality'''
        if self.area() <= other.area():
            return True
        else:
            return False
