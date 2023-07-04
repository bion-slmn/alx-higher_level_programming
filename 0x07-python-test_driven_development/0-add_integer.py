#!/usr/bin/python3
''' this fuction is about addition'''


def add_integer(a, b=98):
    '''adds two intergers with on having a default value 98

    args:
        a (float or int): first argument
        b (float or int): second arguments

    Return:
        the sum of the two numbers
    '''
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
