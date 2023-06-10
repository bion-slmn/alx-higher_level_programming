#!/usr/bin/python3

# delete_at - deletes the item at a specific position in a list.
# my_list : is the list provided
# idx: is the index of the item to delete

def delete_at(my_list=[], idx=0):
    length = len(my_list)

    if idx >= length:
        return my_list
    else:
        del my_list[idx]

    return (my_list)
