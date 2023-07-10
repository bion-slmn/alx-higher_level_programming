#!/usr/bin/python3
'''empty class BaseGeometry.'''


class BaseGeometry:
    '''This is an empty class'''

    def area(self):
        '''This raises an exception'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''validates if value is an int
        Args:
            name(string): name of basegeo
            value(int): must be an int
        '''
        if type(value) != int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
