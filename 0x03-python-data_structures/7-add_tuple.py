#!/usr/bin/python3

# add_tuple - adds  the first 2 tuples values
# If a tuple is smaller than 2, use the value 0 for each missing integer
# If a tuple is bigger than 2, use only the first 2 integers

def add_tuple(tuple_a=(), tuple_b=()):
    result = []
    list_tuple_a = list(tuple_a)
    list_tuple_b = list(tuple_b)

    for x in range(2):
        if x >= len(list_tuple_a):
            list_tuple_a.append(0)

        if x >= len(list_tuple_b):
            list_tuple_b.append(0)

        result.append(list_tuple_b[x] + list_tuple_a[x])

    tuple_c = tuple(result)
    return (tuple_c)
