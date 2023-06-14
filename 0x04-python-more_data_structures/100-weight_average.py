#!/usr/bin/python3
def weight_average(my_list=[]):
    length = len(my_list)
    if length == 0:
        return 0
    else:
        top = 0
        low = 0
        for x, y in my_list:
            top = top + (x * y)
            low = low + y

    return top / low
