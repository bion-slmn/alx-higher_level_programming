#!/usr/bin/python3
'''This module contains a function that converts an obj tojson string'''
import json


def to_json_string(my_obj):
    '''converts python obj to json string'''
    return json.dumps(my_obj)
