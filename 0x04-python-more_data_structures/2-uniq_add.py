#!/usr/bin/python3

# uniq_add - adds all unique integers in a list (only once for each integer).
# my_list - is a the list

def uniq_add(my_list=[]):
    newset = set(my_list)

    sum = 0
    for x in newset:
        sum += x
    return sum
