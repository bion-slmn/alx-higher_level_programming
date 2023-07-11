#!/usr/bin/python3
'''Thia module writes to json file'''
import json


def load_from_json_file(filename):
    '''convert json to python obj '''
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
