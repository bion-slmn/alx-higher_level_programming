#!/usr/bin/python3
'''This module creates a class Square'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''class square inherits from Rectngle class'''
    def __init__(self, size, x=0, y=0, id=None):
        '''it initialises the attributes and call the init of parent class'''
        super().__init__(size, size, x, y, id)

    @property
    def width(self):
        return super().width

    @width.setter
    def width(self, new_value):
        '''settiing the value of width'''
        super(Square, type(self)).width.fset(self, new_value)

    @property
    def height(self):
        return super().height

    @height.setter
    def height(self, value):
        '''setting the height value'''
        super(Square, type(self)).height.fset(self, value)

    @property
    def x(self):
        '''getting th x value'''
        return super().x

    @x.setter
    def x(self, value):
        '''seting the x value'''
        super(Square, type(self)).x.fset(self, value)

    @property
    def y(self):
        '''getting th x value'''
        return super().y

    @y.setter
    def y(self, value):
        '''seting the x value'''
        super(Square, type(self)).y.fset(self, value)

    @property
    def size(self):
        '''get the value size'''
        return self.width

    @size.setter
    def size(self, value):
        '''setting the width and height to the same value'''
        self.width = value
        self.height = value

    def __str__(self):
        '''overloading the str method to return an informal statement'''
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'

    def update(self, *args, **kwargs):
        '''update the square class with both args and kwargs'''
        attr = [self.id, self.size, self.x, self.y]

        if args:
            for index in range(len(args)):
                if index <= len(attr) - 1:
                    attr[index] = args[index]
                else:
                    break

            if attr[0] is None:
                attr[0] = self.__init__(self.size, self.x, self.y)
            self.id, self.size, self.x, self.y = attr

        else:
            for key, value in kwargs.items():
                if key == 'size':
                    self.size = value
                if 'x' == key:
                    self.x = value
                if 'y' == key:
                    self.y = value
                if 'id' == key:
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    self.id = value
                else:
                    continue

    def to_dictionary(self):
        '''retutn the dictionary reprentation of square'''
        return {'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y}
