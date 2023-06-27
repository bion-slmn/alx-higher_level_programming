#!/usr/bin/python3
'''define a class square'''


class Square:
    '''The square is defined by: 1.Private instance attribute: size
      and 2. Instantiation with optional size'''
    def __init__(self, size=0, position=(0, 0)):
        '''Initialize a new Square.

        Args:
            size (:obj:`int`, optional): is the size of a square
            position(:obj:'tuple', optiona) : is position to start print
        '''
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        '''retrive the position value

        Return:
            the positon value'''
        return self_position

    @position.setter
    def position(self, value):
        '''set the position value'''
        if (len(value) != 2
                or not all(isinstance(num, int) for num in value) or
                not isinstance(value, tuple) or
                not all(num >= 0 for num in value)):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        '''calculates the area of a square

        Args:
            size (int): the size of the square

        Return:
            int: the area of the square'''
        return self.__size ** 2

    def my_print(self):
        ''' that prints in stdout the square with the character #'''
        if self.__size == 0:
            print("")
        else:
            for x in range(self.__position[1]):
                print("")
            for x in range(self.__size):
                for q in range(self.__position[0]):
                    print(" ", end="")
                for y in range(self.__size):
                    print("#", end="")
                print("")
