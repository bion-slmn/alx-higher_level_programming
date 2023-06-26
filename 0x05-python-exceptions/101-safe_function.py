#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    '''executes a function safely.'''
    try:
        result = fct(*args)
        return result
    except Exception as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return None
