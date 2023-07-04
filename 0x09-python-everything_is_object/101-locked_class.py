#!/usr/bin/python3
''' This module prevents the user from dynamically creating new instance
    attributes, except if the new instance attribute is called first_name
'''


class LockedClass(object):
    '''allows creation of first name only'''

    __slots__ = ['first_name']

    def __init__(self):
        ''' intialize first name to object'''

        self.first_name = None
