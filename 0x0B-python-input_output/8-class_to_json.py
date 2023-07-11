#!/usr/bin/python
'''this module converts class to json format'''


def class_to_json(obj):
    '''converts call tojson format'''
    return obj.__dict__
