#!/usr/bin/python3

# max_integer - inds the biggest integer of a list.
# If the list is empty, return None

def max_integer(my_list=[]):

    length = len(my_list)
    first = my_list[0]

    if length == 0:
        return None

    else:
        for x in my_list:
            if first < x:
                first = x

    return first
