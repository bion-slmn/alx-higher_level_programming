#!/usr/bin/python3
''' this function  returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False.'''


def is_kind_of_class(obj, a_class):
    ''' returns true is the obbject is an inherited from another class'''
    return isinstance(obj, a_class)
