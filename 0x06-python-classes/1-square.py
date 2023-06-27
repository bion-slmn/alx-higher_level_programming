#!/usr/bin/python3
'''Define a class square'''


class Square:
    '''defines a square by
    Private instance attribute: size
    Instantiation with size (no type/value verification)'''
    def __init__(self, size):
        '''Initialize a new Square.
            Args:
                size (int):size of a square
        '''
        self.__size = size
