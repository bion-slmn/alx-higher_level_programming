#!/usr/bin/python3
'''Thia module writes to json file'''
import json


def save_to_json_file(my_obj, filename):
    '''convert py object and save it in json file'''
    with open(filename, 'w', encoding='utf-8') as f:
        return json.dump(my_obj, f)
