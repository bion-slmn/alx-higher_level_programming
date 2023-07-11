#!/usr/bin/python3
'''Thif modules reads contents of a file'''


def read_file(filename=""):
    '''read_file open a file an prints its content
    Args:
        filename(file) it a file
    '''
    with open(filename, encoding='utf-8') as myfile:
        for line in myfile:
            print(line, end="")
