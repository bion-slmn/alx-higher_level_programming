#!/usr/bin/python3
'''class Square that inherits from Rectangle'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''it creates saquare from the parent Rectangle'''
    def __init__(self, size):
        '''it intialises the size of the square'''
        super().integer_validator('size', size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        '''calculates the area using the method in rectangle'''
        return self.__size ** 2

    def __str__(self):
        '''return the descreiptio of  square'''
        return f'[Square] {self.__size}/{self.__size}'
