#!/usr/bin/python3

# new_in_list - replaces an element in a list at a specific position without
# modifying the original list
# my_list: is the list
# idx : is the index to replace
# element: is the new element to be added

def new_in_list(my_list, idx, element):
    length = len(my_list)
    newList = my_list[:]

    if idx < 0 or idx > length - 1:
        return (newList)
    else:
        newList[idx] = element
        return (newList)
