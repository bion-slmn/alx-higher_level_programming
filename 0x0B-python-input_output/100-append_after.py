#!/usr/bin/python3
'''search and update a text'''


def append_after(filename="", search_string="", new_string=""):
    '''searches for a given string an add new string after it'''

    with open(filename, encoding='utf-8') as f:
        newlist = f.readlines()

    list2 = []
    for line in newlist:
        if search_string in line:
            list2.append(line)
            list2.append(new_string)
        else:
            list2.append(line)

    with open(filename, 'w', encoding='utf-8') as f:
        for line in list2:
            f.write(line)
