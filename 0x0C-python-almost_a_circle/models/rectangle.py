#!/usr/bin/python3
'''This module defines a class rectangle that inherits base'''
from models.base import Base


class Rectangle(Base):
    '''this class inherits Base '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''this is the constructor to intialise instance variables'''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''getter method for width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''sets the width as a private'''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        '''gets the private value height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''sets the private value height'''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        '''gets the private value x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''sets the private value x'''
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        '''gets the private value y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''sets the private value y'''
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        '''calculate the area of the the rectangle'''
        return (self.__width * self.__height)

    def display(self):
        ''' display the rectangle with # symbol'''

        for x in range(self.__y):
            print()
        for h in range(self.__height):
            for y in range(self.__x):
                print(' ', end="")
            for w in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        '''prints an informal message about the class'''
        return f'[Rectangle] ({self.id}) {self.__x}/{self.__y} - '\
            f'{self.__width}/{self.__height}'

    def update(self, *args, **kwargs):
        '''updates the arguments with non keyword arguments'''
        attr = [self.id, self.width, self.height, self.x, self.y]

        if args:
            for index in range(len(args)):
                if index <= len(attr) - 1:
                    attr[index] = args[index]
                else:
                    break
            self.id, self.width, self.height, self.x, self.y = attr

        else:
            for key, value in kwargs.items():
                if key == 'id':
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                if key == 'width':
                    self.width = value
                if key == 'height':
                    self.height = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value
                else:
                    continue

    def to_dictionary(self):
        '''return a dictionary representation of Recatangle'''
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x,
                'y': self.y}
