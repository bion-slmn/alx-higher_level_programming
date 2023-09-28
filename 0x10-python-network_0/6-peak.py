#!/usr/bin/python3
''' this module defines a function to find a peak in unsorted
list'''


def find_peak(list_of_integers):
    '''This function find a peak in in usorted list

    list_of_ integers (list): contain a list of unsorted array
    '''

    # if the liist is empty return none
    if list_of_integers == []:
        return None
    if list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]

    # otherwise  iterate thru the list
    for index in range(1, len(list_of_integers) - 1):
        left = index - 1
        right = index + 1
        item = list_of_integers[index]
        if item >= list_of_integers[left] and item >= list_of_integers[right]:
            return item

    # check if a number is geater or equal to the numbeer in ifront and behind
    # and return that no else continue to
