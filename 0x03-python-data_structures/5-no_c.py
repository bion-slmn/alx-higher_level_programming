#!/usr/bin/python3
# no_c - removes all characters c and C from a string.
# my_string: is the string passed

def no_c(my_string):
    newString = []
    for x in my_string:
        if x != "c" and x != "C":
            newString.append(x)
    return ("".join(newString))
