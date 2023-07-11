#!/usr/bin/python3
'''this module converts jsonstring to python'''
import json


def from_json_string(my_str):
    '''thefunction that converts json string to python'''
    return json.loads(my_str)
