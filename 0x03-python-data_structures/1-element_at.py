#!/usr/bin/python3
"""element_at - retrieves an element from a list
    my_list : is the list passed
    idx: is the index of the element"""


def element_at(my_list, idx):
    length = len(my_list)

    if idx >= 0 or idx <= length - 1:
        return (my_list[idx])
    else:
        return None
