#!/usr/bin/python3
'''Myint classs ia a rebel class of int'''


class MyInt(int):
    '''it inherits from int classs '''
    def __eq__(self, other):
        '''it return tthey arent equal'''
        return not super().__eq__(other)

    def __ne__(self, other):
        '''return they are equal'''
        return not super().__ne__(other)
