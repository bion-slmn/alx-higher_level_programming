#!/usr/bin/python3

# divisible_by_2 -  finds all multiples of 2 in a list.
# Return a new list with True or False

def divisible_by_2(my_list=[]):
    newList = []

    for x in my_list:
        if (x % 2) == 0:
            newList.append(True)

        else:
            newList.append(False)

    return newList
