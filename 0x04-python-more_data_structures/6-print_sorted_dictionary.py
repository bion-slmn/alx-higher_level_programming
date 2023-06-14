#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new1 = [[x, y] for x, y in a_dictionary.items()]

    for x in sorted(new1):
        print("{}: {}".format(x[0], x[1]))
