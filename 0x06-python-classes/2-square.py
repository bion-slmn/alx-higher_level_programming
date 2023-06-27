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
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
