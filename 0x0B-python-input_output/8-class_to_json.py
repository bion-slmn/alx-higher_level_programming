#!/usr/bin/python3
'''this module converts class to json format'''


def class_to_json(obj):
    '''Return the dictionary represntation of a simple data structure.'''
    return obj.__dict__
