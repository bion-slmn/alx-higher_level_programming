#!/usr/bin/python3
# replace_in_list -  replaces an element of a list at a specific position
# my_list: is the list
# idx: is the index of the element
# element: is the new element to  replace

def replace_in_list(my_list, idx, element):
    length = len(my_list)

    if idx < 0 or idx > length:
        return (my_list)
    else:
        my_list[idx] = element
        return (my_list)
