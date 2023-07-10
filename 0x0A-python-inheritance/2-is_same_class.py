#!/usr/bin/python3
'''This function  returns True if the object is exactly an
    instance of the specified class ; otherwise False'''


def is_same_class(obj, a_class):
    '''is_same_class return true or false if
    `obj is of instance a_class
    '''
    if type(obj) is a_class:
        return True
    return False
