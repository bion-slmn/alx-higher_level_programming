#!/usr/bin/python3
'''This function returns a lists of attributes'''


def lookup(obj):
    '''returns list of attributes for the object

    Args:
        obj(an object): an object of any class
    '''
    return dir(obj)
