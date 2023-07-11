#!/usr/bin/python3
import json
'''This module contains a function that converts an obj to
json string'''


def to_json_string(my_obj):
    '''converts python obj to json string
    Args:
        my_obj(object): python object to be converted
        json string
    '''
    return json.dumps(my_obj)
