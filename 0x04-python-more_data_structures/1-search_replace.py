#!/usr/bin/python3

# search_replace :replaces all occurrences of an element by another
# my_list is the initial list
# search is the element to replace in the list
# replace is the new element

def search_replace(my_list, search, replace):
    newList = my_list[:]
    for x in range(len(my_list)):
        if newList[x] == search:
            newList[x] = replace

    return newList
