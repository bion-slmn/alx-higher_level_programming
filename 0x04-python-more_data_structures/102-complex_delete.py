#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value in a_dictionary.values():
        list1 = a_dictionary.items()
        keys_toremove = []
        for x, y in list1:
            if value == y:
                keys_toremove .append(x)

        for key in keys_toremove:
            a_dictionary.pop(key)

    return a_dictionary
