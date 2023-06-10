#!/usr/bin/python3
# print_reversed_list_integer - prints all integers of a list, in reverse
# my_list - is the list containg intergers

def print_reversed_list_integer(my_list=[]):
    for x in my_list[::-1]:
        print("{:d}".format(x))
