#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    ''' prints x elements of a list.'''
    index = 0
    try:
        for item in range(x):
            print("{}".format(my_list[item]), end="")
            index += 1
    except IndexError:
        pass
    finally:
        print()
        return index
