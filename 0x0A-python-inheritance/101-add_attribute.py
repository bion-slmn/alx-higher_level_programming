#!/usr/bin/python3
''' this function adds attribute to an objest'''


def add_attribute(obj, name, value):
    '''it add name attribute to the object
    Args:
        obj(object): an objectt of a classs
        name(name): name of the attribute
        value: is the data of the attribute
    '''

    if obj is None or not hasattr(obj, '__dict__') or name is None or\
            value is None:
        raise TypeError("can't add new attribute")
    obj.name = value
