#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    '''prints the first x elements of a list and only integers.'''
    index = 0
    for item in range(x):
        try:
            print("{:d}".format(my_list[item]), end="")
            index += 1
        except IndexError:
            raise
        except Exception:
            continue
    print()
    return index
